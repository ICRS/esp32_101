from machine import Pin
from machine import PWM

max_duty = 1023

class driveBase:
    def __init__(self, pwmOutA, pwmOutB, 
            digitalOutA1, digitalOutA2, 
            digitalOutB1, digitalOutB2):
        self.pwmOutA = PWM(Pin(pwmOutA), 50000)
        self.pwmOutB = PWM(Pin(pwmOutB), 50000)

        self.digitalOutA1 = Pin(digitalOutA1, Pin.OUT)
        self.digitalOutA2 = Pin(digitalOutA2, Pin.OUT)
        self.digitalOutB1 = Pin(digitalOutB1, Pin.OUT)
        self.digitalOutB2 = Pin(digitalOutB2, Pin.OUT)

    def forward(self, speed=1):
        self.pwmOutA.duty(int(speed * max_duty))
        self.pwmOutB.duty(int(speed * max_duty))
        self.digitalOutA1.on()
        self.digitalOutA2.off()
        self.digitalOutB1.on()
        self.digitalOutB2.off()


    def back(self, speed=1):
        self.pwmOutA.duty(int(speed * max_duty))
        self.pwmOutB.duty(int(speed * max_duty))
        self.digitalOutA1.off()
        self.digitalOutA2.on()
        self.digitalOutB1.off()
        self.digitalOutB2.on()
    
    def rotateRight(self, speed=1):
        self.pwmOutA.duty(int(speed * max_duty))
        self.pwmOutB.duty(int(speed * max_duty))
        
        self.digitalOutA1.on()
        self.digitalOutA2.off()
        self.digitalOutB1.off()
        self.digitalOutB2.on()

    def rotateLeft(self, speed=1):
        self.pwmOutA.duty(int(speed * max_duty))
        self.pwmOutB.duty(int(speed * max_duty))
        
        self.digitalOutA1.off()
        self.digitalOutA2.on()
        self.digitalOutB1.on()
        self.digitalOutB2.off()
