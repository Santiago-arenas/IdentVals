from _multiprocessing import flags
import sys
import Adafruit_BBIO.GPIO as GPIO
import time
from IdentVals import *

class Pruebas(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnP8_26.clicked.connect(lambda: self.digitalOut("P8_26", self.ui.btnP8_26))
        self.ui.btnP8_18.clicked.connect(lambda: self.digitalOut("P8_18", self.ui.btnP8_26))
        self.ui.btnP8_17.clicked.connect(lambda: self.digitalOut("P8_17", self.ui.btnP8_26))
        self.ui.btnP8_16.clicked.connect(lambda: self.digitalOut("P8_16", self.ui.btnP8_26))
        self.ui.btnP8_15.clicked.connect(lambda: self.digitalOut("P8_15", self.ui.btnP8_26))
        self.ui.btnP8_14.clicked.connect(lambda: self.digitalOut("P8_14", self.ui.btnP8_26))
        self.ui.btnP8_12.clicked.connect(lambda: self.digitalOut("P8_12", self.ui.btnP8_26))
        self.ui.btnP8_11.clicked.connect(lambda: self.digitalOut("P8_11", self.ui.btnP8_26))
        self.ui.btnP8_10.clicked.connect(lambda: self.digitalOut("P8_10", self.ui.btnP8_26))
        self.ui.btnP8_9.clicked.connect(lambda: self.digitalOut("P8_9", self.ui.btnP8_26))


    def digitalOut(self, port, btn):
        check = btn.isChecked()
        GPIO.setup(port, GPIO.OUT)
        if(check):
            GPIO.output(port, GPIO.HIGH)
        else:
            GPIO.output(port, GPIO.LOW)

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = Pruebas()
        myapp.show()
        sys.exit(app.exec_())