from machine import Pin
from machine import PWM


class driveBase:
    def __init__(self, pwmOutA, pwmOutB, 
            digitalOutA1, digitalOutA2, 
            digitalOutB1, digitalOutB2):
        self.pwmOutA = PWM(Pin(pwmOutA), 50)
        self.pwmOutB = PWM(Pin(pwmOutB), 50)

        self.digitalOutA1 = Pin(digitalOutA1, Pin.Out)
        self.digitalOutA2 = Pin(digitalOutA2, Pin.Out)
        self.digitalOutB1 = Pin(digitalOutB1, Pin.Out)
        self.digitalOutB2 = Pin(digitalOutB2, Pin.Out)

    def forward(self, speed=1):
        self.pwmOutA.duty_ns(speed * 2000)
        self.pwmOutB.duty_ns(speed * 2000)
        self.digitalOutA1.on()
        self.digitalOutA2.off()
        self.digitalOutB1.on()
        self.digitalOutB2.off()


    def back(self, speed=1):
        self.pwmOutA.duty_ns(speed * 2000)
        self.pwmOutB.duty_ns(speed * 2000)
        self.digitalOutA1.off()
        self.digitalOutA2.on()
        self.digitalOutB1.off()
        self.digitalOutB2.on()
