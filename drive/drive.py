import machine
from machine import Pin
from machine import

class driveBase:
    def __init__(self, pwmOutA, pwmOutB, 
            digitalOutA1, digitalOutA2, 
            digitalOutB1, digitalOutB2):
        self.pwmOutA = Pin(pwmOutA, Pin.Out)
        self.pwmOutB = Pin(pwmOutB, Pin.Out)

        self.digitalOutA1 = Pin(digitalOutA1, Pin.Out)
        self.digitalOutA2 = Pin(digitalOutA2, Pin.Out)
        self.digitalOutB1 = Pin(digitalOutB1, Pin.Out)
        self.digitalOutB2 = Pin(digitalOutB2, Pin.Out)
