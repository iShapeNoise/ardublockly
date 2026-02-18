#! python
#
# This module implements a special URL handler that uses the port listing to
# find ports by searching the string descriptions.
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause
#
# URL format:    hwgrep://<regexp>&<option>
#
# where <regexp> is a Python regexp according to the re module
#
# violating the normal definition for URLs, the charachter `&` is used to
# separate parameters from the arguments (instead of `?`, but the question mark
# is heavily used in regexp'es)
#
# options:
# n=<N>     pick the N'th entry instead of the first one (numbering starts at 1)
# skip_busy tries to open port to check if it is busy, fails on posix as ports are not locked!

import serial
import serial.tools.list_ports

