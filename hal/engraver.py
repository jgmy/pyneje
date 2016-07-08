# Engraver protocol etc
from time import sleep

import serial

from serialenum import serialenum


def get_serial_ports():
    return serialenum.enumerate()


def tohex(value):
    return "%0.2x" % value

class Engraver:
    def __init__(self, port):
        self.bytesWritten = 0
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
      #  print "Sending " + code
        if self.commPort.out_waiting > 200:
            self.commPort.flush()
        res = self.commPort.write(code.decode("hex"))
        print "Wrote " + str(res) + " bytes, total " + str(self.bytesWritten) + " waiting " + str(self.commPort.out_waiting)

        self.bytesWritten += res

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
            self._perform("fa" + tohex(value))

    def move_center(self):
        self._perform("fb")

    def adjust_burntime(self, value):
        print "burn time"
        if 0 < value < 0xf0:
            self._perform(tohex(value))
        else:
            print "Value " + value + " is out of range."

            # 0xfc = fast backward <parameter 0x55> fast forward <parameter 0xaa> recarve <parameter 0x77> // Useful???

    def load_image(self, imagedata):
        bmp = self.generate_bmp(imagedata)
        for x in range(8):
            self._perform("fe")
        self.commPort.flush()
        # give some time for the flash to erase.
        sleep(5)

        for i in range(len(bmp)):
            self._perform(bmp[i])

        if False:
            # debug to verify the image output, saves a file called out.bmp in the app folder for visual verification
            newfile = open("out.bmp", 'wb')
            for i in range(len(bmp)):
                value = bmp[i].decode("hex")
                newfile.write(value)
            newfile.close()

    # probably a lot better ways to do this...
    @staticmethod
    def generate_bmp(image):
        image_array = list(image)
        bmp = ["42", "4D", "3E", "80", "00", "00", "00", "00", "00", "00",
               "3E", "00", "00", "00", "28", "00", "00", "00", "00", "02",
               "00", "00", "00", "02", "00", "00", "01", "00", "01", "00",
               "00", "00", "00", "00", "00", "00", "00", "00", "00", "00",
               "00", "00", "00", "00", "00", "00", "00", "00", "00", "00",
               "00", "00", "00", "00", "00", "00", "00", "00", "FF", "FF",
               "FF", "00"];
        byte = 0
        bit = 0
        total = 0
        for index in range(len(image_array)):
            if image_array[index] != 0:
                byte |= 1 << (7 - bit)
            bit += 1
            if bit > 7:
                total += 1
                bmp.append(tohex(byte))
                bit = 0
                byte = 0
        bmp.append(tohex(byte))
        print "Wrote " + str(total) + " bytes, with header " + str(len(bmp))
        return bmp
