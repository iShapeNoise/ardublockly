#!jython
#
# Backend Jython with JavaComm
#
# This file is part of pySerial. https://github.com/pyserial/pyserial
# (C) 2002-2015 Chris Liechti <cliechti@gmx.net>
#
# SPDX-License-Identifier:    BSD-3-Clause

from serial.serialutil import *


def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def detect_java_comm(names):
    """try given list of modules and return that imports"""
    for name in names:
