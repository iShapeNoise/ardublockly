#! python
#
# This module implements a special URL handler that allows selecting an
# alternate implementation provided by some backends.
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# (C) 2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause
#
# URL format:    alt://port[?option[=value][&option[=value]]]
# options:
# - class=X used class named X instead of Serial
#
# example:
#   use poll based implementation on Posix (Linux):
#   python -m serial.tools.miniterm alt:///dev/ttyUSB0?class=PosixPollSerial

