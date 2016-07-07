# Engraver protocol etc

import serial

from serialenum import serialenum


def get_serial_ports():
    return serialenum.enumerate()

class Engraver:
    def __init__(self, port):
        self.initialized = False
        self.commPortName = port
        self.commPort = None

    def is_connected(self):
        return self.initialized

    def connect(self):
        if not self.initialized:
            self.commPort = serial.Serial(self.commPortName,
                                          57600)
            assert isinstance(self.commPort, object)
            self.initialized = True

    def disconnect(self):
        if self.initialized:
            self.reset()
            self.commPort.flush()
            self.commPort.close()
            self.initialized = False

    def _perform(self, code):
        if not self.is_connected():
            self.connect()
        self.commPort.write(code.decode("hex"))

    def reset(self):
        self._perform("f9")

    def stop(self):
        self.reset()

    def start(self):
        self._perform("f1")

    def pause(self):
        self._perform("f2")

    def preview(self):
        self._perform("f4")

    def move_up(self):
        self._perform("f5")

    def move_down(self):
        self._perform("f6")

    def move_left(self):
        self._perform("f7")

    def move_right(self):
        self._perform("f8")

    def move_home(self):
        self._perform("f3")

    def set_step(self, value):
        if 0 < value < 0xff:
            self._perform("fa" + chr(value))

    def move_center(self):
        self._perform("fb")

    def adjust_burntime(self, value):
        if 0 < value < 0xf0:
            self._perform(chr(value))
        else:
            print "Value " + value + " is out of range."

            # 0xfc = fast backward <parameter 0x55> fast forward <parameter 0xaa> recarve <parameter 0x77> // Useful???

    def load_image(self, imagedata):
        self._perform("fefefefefefefefe")
        self._perform(imagedata)
