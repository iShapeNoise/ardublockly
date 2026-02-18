#! python
#
# Backend for .NET/Mono (IronPython), .NET >= 2
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# (C) 2008-2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause

import System
import System.IO.Ports
from serial.serialutil import *

# must invoke function with byte array, make a helper to convert strings
# to byte arrays
sab = System.Array[System.Byte]


def as_byte_array(string):
    return sab([ord(x) for x in string])  # XXX will require adaption when run with a 3.x compatible IronPython


class Serial(SerialBase):
    """Serial port implementation for .NET/Mono."""

    BAUDRATES = (50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                 9600, 19200, 38400, 57600, 115200)

    def open(self):
        """\
        Open port with current settings. This may throw a SerialException
        if the port cannot be opened.
        """
        if self._port is None:
            raise SerialException("Port must be configured before it can be used.")
        if self.is_open:
            raise SerialException("Port is already open.")
