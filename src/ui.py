import Tkinter

import tkSimpleDialog


class SerialSelection(tkSimpleDialog.Dialog):
    def __init__(self, parent, serial_list, callback=None, title=None):
        self.dropdown_selection = None
        self.serial_list = serial_list
        self.returnValue = None
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
        if self.dropdown_selection:
            self.returnValue = self.dropdown_selection.get()

