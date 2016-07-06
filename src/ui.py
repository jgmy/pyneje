import Tkinter

import engraver
import tkSimpleDialog


class SerialSelection(tkSimpleDialog.Dialog):
    def __init__(self, parent, serial_list, callback=None, title=None):
        self.dropdown_selection = None
        self.serial_list = serial_list
        tkSimpleDialog.Dialog.__init__(self, parent, callback, title)

    def body(self, master):
        if len(self.serial_list) > 0:
            Tkinter.Label(master, text="Select the engraver device:").grid(row=0)
            self.dropdown_selection = Tkinter.StringVar(master)
            self.dropdown_selection.set(self.serial_list[0])

            return Tkinter.OptionMenu(master, self.dropdown_selection, *self.serial_list).grid()
        else:
            return Tkinter.Label(master, text="No suitable devices detected.").grid(row=0)

    def apply(self):
        if self.dropdown_selection is not None:
            return self.dropdown_selection.get()
        else:
            return None


def print_it(var):
    if var:
        print "result " + var
    else:
        print "No serial port detected"
        Tkinter.Message(root, text="this is a message")


root = Tkinter.Tk()
root.update()

d = SerialSelection(root, engraver.getSerialPorts(), print_it)
root.wait_window(d)

# Tkinter.mainloop();
