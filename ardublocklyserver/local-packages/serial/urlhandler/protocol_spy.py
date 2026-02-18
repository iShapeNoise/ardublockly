#! python
#
# This module implements a special URL handler that wraps an other port,
# print the traffic for debugging purposes. With this, it is possible
# to debug the serial port traffic on every application that uses
# serial_for_url.
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# (C) 2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause
#
# URL format:    spy://port[?option[=value][&option[=value]]]
# options:
# - dev=X   a file or device to write to
# - color   use escape code to colorize output
# - raw     forward raw bytes instead of hexdump
#
# example:
#   redirect output to an other terminal window on Posix (Linux):
#   python -m serial.tools.miniterm spy:///dev/ttyUSB0?dev=/dev/pts/14\&color

import sys
import time

import serial

