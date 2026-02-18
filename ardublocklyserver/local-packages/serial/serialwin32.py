#! python
#
# backend for Windows ("win32" incl. 32/64 bit support)
#
# (C) 2001-2015 Chris Liechti <cliechti@gmx.net>
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# SPDX-License-Identifier:    BSD-3-Clause
#
# Initial patch to use ctypes by Giovanni Bajo <rasky@develer.com>

# pylint: disable=invalid-name,too-few-public-methods
import ctypes
import time
from serial import win32

import serial
from serial.serialutil import SerialBase, SerialException, to_bytes, portNotOpenError, writeTimeoutError


class Serial(SerialBase):
    """Serial port implementation for Win32 based on ctypes."""

    BAUDRATES = (50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                 9600, 19200, 38400, 57600, 115200)

    def __init__(self, *args, **kwargs):
        self._port_handle = None
        self._overlapped_read = None
        self._overlapped_write = None
        super(Serial, self).__init__(*args, **kwargs)

    def open(self):
        """\
        Open port with current settings. This may throw a SerialException
        if the port cannot be opened.
        """
        if self._port is None:
            raise SerialException("Port must be configured before it can be used.")
        if self.is_open:
            raise SerialException("Port is already open.")
        # the "\\.\COMx" format is required for devices other than COM1-COM8
        # not all versions of windows seem to support this properly
        # so that the first few ports are used with the DOS device name
        port = self.name
