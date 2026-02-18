#! python
#
# This module implements a RFC2217 compatible client. RF2217 descibes a
# protocol to access serial ports over TCP/IP and allows setting the baud rate,
# modem control lines etc.
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# (C) 2001-2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause

# TODO:
# - setting control line -> answer is not checked (had problems with one of the
#   severs). consider implementing a compatibility mode flag to make check
#   conditional
# - write timeout not implemented at all

# ###########################################################################
# observations and issues with servers
# ===========================================================================
# sredird V2.2.1
# - http://www.ibiblio.org/pub/Linux/system/serial/   sredird-2.2.2.tar.gz
# - does not acknowledge SET_CONTROL (RTS/DTR) correctly, always responding
#   [105 1] instead of the actual value.
# - SET_BAUDRATE answer contains 4 extra null bytes -> probably for larger
#   numbers than 2**32?
# - To get the signature [COM_PORT_OPTION 0] has to be sent.
# - run a server: while true; do nc -l -p 7000 -c "sredird debug /dev/ttyUSB0 /var/lock/sredir"; done
# ===========================================================================
# telnetcpcd (untested)
# - http://ftp.wayne.edu/kermit/sredird/telnetcpcd-1.09.tar.gz
# - To get the signature [COM_PORT_OPTION] w/o data has to be sent.
# ===========================================================================
# ser2net
# - does not negotiate BINARY or COM_PORT_OPTION for his side but at least
#   acknowledges that the client activates these options
# - The configuration may be that the server prints a banner. As this client
#   implementation does a flushInput on connect, this banner is hidden from
#   the user application.
# - NOTIFY_MODEMSTATE: the poll interval of the server seems to be one
#   second.
# - To get the signature [COM_PORT_OPTION 0] has to be sent.
# - run a server: run ser2net daemon, in /etc/ser2net.conf:
#     2000:telnet:0:/dev/ttyS0:9600 remctl banner
# ###########################################################################

# How to identify ports? pySerial might want to support other protocols in the
# future, so lets use an URL scheme.
# for RFC2217 compliant servers we will use this:
#    rfc2217://<host>:<port>[?option[&option...]]
#
# options:
# - "logging" set log level print diagnostic messages (e.g. "logging=debug")
# - "ign_set_control": do not look at the answers to SET_CONTROL
# - "poll_modem": issue NOTIFY_MODEMSTATE requests when CTS/DTR/RI/CD is read.
#   Without this option it expects that the server sends notifications
#   automatically on change (which most servers do and is according to the
#   RFC).
# the order of the options is not relevant

import logging
import socket
import struct
import threading
import time
