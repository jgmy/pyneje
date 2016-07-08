import Tkinter
import os
import platform
import subprocess
import time
import hal.engraver
import ui_widgets.serialdialog


# Hack from stackoverflow to raise the window on most platforms.
from pyneje_gui.main import GUI


def raise_app(root_tk):
    root_tk.attributes("-topmost", True)
    if platform.system() == 'Darwin':
        tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
        script = tmpl.format(os.getpid())
        output = subprocess.check_call(['/usr/bin/osascript', '-e', script])
    root_tk.after(0, lambda: root_tk.attributes("-topmost", False))


if __name__ == "__main__":
    root = Tkinter.Tk()
    raise_app(root)
    root.update()
    serialPort = ui_widgets.serialdialog.SerialSelection(root, hal.engraver.get_serial_ports()).returnValue

    if serialPort is None:
        print "Can't operate without a valid serial port"
        exit(1)

    device = hal.engraver.Engraver(serialPort)
    device.reset()
    ui = GUI(root, device).run()

    device.disconnect()
