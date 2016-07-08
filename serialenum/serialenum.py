# Based of https://github.com/djs/serialenum
# I just added OS X support..

# Copyright (c) 2012, Dan Savilonis
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import os.path
import sys
import glob

import serial


def enumerate():
    ports = []

    if sys.platform == 'win32':
        # Iterate through registry because WMI does not show virtual serial ports
        import _winreg

        try:
            key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'HARDWARE\DEVICEMAP\SERIALCOMM')
        except WindowsError:
            return []
        i = 0
        while True:
            try:
                ports.append(_winreg.EnumValue(key, i)[1])
                i = i + 1
            except WindowsError:
                break
    elif sys.platform == 'linux2':
        if os.path.exists('/dev/serial/by-id'):
            entries = os.listdir('/dev/serial/by-id')
            dirs = [os.readlink(os.path.join('/dev/serial/by-id', x))
                    for x in entries]
            ports.extend([os.path.normpath(os.path.join('/dev/serial/by-id', x))
                          for x in dirs])

        for dev in glob.glob('/dev/ttyS*'):
            try:
                port = serial.Serial(dev)
            except:
                pass
            else:
                ports.append(dev)
    elif sys.platform == 'darwin':
        for dev in glob.glob('/dev/cu.*'):
            if dev.find("Bluetooth") == -1:
                try:
                    port = serial.Serial(dev)
                except:
                    pass
                else:
                    ports.append(dev)
    else:
        return []

    return ports


def script():
    for port in enumerate():
        print port


if __name__ == "__main__":
    script()
