import Tkinter
import os
import platform
import subprocess
import time

from src import engraver
from src.ui import SerialSelection


# Hack from stackoverflow to raise the window on most platforms.

def raise_app(root):
    root.attributes("-topmost", True)
    if platform.system() == 'Darwin':
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
        script = tmpl.format(os.getpid())
        output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
    root.after(0, lambda: root.attributes("-topmost", False))


if __name__ == "__main__":
    root = Tkinter.Tk()
    raise_app(root)
    root.update()
    serialPort = SerialSelection(root, engraver.get_serial_ports()).returnValue
    if serialPort is None:
        print "Can't operate without a valid serial port"
        exit(1)

    device = engraver.Engraver(serialPort)

    device.reset()
    time.sleep(5)

    device.disconnect()
