import smbus2
import random

LM75_ADDRESS = 0x48

LM75_TEMP_REGISTER = 0
LM75_CONF_REGISTER = 1
LM75_THYST_REGISTER = 2
LM75_TOS_REGISTER = 3

LM75_CONF_SHUTDOWN = 0
LM75_CONF_OS_COMP_INT = 1
LM75_CONF_OS_POL = 2
LM75_CONF_OS_F_QUE = 3


class LM75(object):
    def __init__(self, mode=LM75_CONF_OS_COMP_INT, address=LM75_ADDRESS, busnum=1):
        self._mode = mode
        self._address = address
        self._bus = smbus2.SMBus(busnum)

    def regdata2float(self, regdata):
        return (regdata / 32.0) / 8.0

    def to_fah(self, temp):
        return (temp * (9.0 / 5.0)) + 32.0

    def to_celsius(self, temp):
        f = self.to_fah(temp)
        return (f - 32) * 5 / 9

    def get_temp(self, celsius=True):
        raw = self._bus.read_word_data(self._address, LM75_TEMP_REGISTER) & 0xFFFF
        raw = ((raw << 8) & 0xFF00) + (raw >> 8)
        return self.to_celsius(self.regdata2float(raw))


class MockupLM75:

    def get_temp(self, celsius=True):
        return random.randrange(2500, 2790) / 100
