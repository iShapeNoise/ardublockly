#! python
#
# Constants and types for use with Windows API, used by serialwin32.py
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# (C) 2001-2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause

# pylint: disable=invalid-name,too-few-public-methods,protected-access,too-many-instance-attributes

from ctypes import c_ulong, c_void_p, c_int64, c_char, \
                   WinDLL, sizeof, Structure, Union, POINTER
from ctypes.wintypes import HANDLE
from ctypes.wintypes import BOOL
from ctypes.wintypes import LPCWSTR
from ctypes.wintypes import DWORD
from ctypes.wintypes import WORD
from ctypes.wintypes import BYTE
_stdcall_libraries = {}
_stdcall_libraries['kernel32'] = WinDLL('kernel32')

INVALID_HANDLE_VALUE = HANDLE(-1).value


# some details of the windows API differ between 32 and 64 bit systems..
def is_64bit():
    """Returns true when running on a 64 bit system"""
    return sizeof(c_ulong) != sizeof(c_void_p)

# ULONG_PTR is a an ordinary number, not a pointer and contrary to the name it
# is either 32 or 64 bits, depending on the type of windows...
# so test if this a 32 bit windows...
if is_64bit():
    ULONG_PTR = c_int64
else:
    ULONG_PTR = c_ulong


class _SECURITY_ATTRIBUTES(Structure):
    pass
LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)


