from machine import Pin
from machine import PWM

max_duty = 1023
pwm_frequency = 50000

class driveBase:
    def __init__(self, pwmOutA, pwmOutB, 
            digitalOutA1, digitalOutA2, 
            digitalOutB1, digitalOutB2):
        self.pwmOutA = PWM(Pin(pwmOutA), pwm_frequency)
        self.pwmOutB = PWM(Pin(pwmOutB), pwm_frequency)

        self.digitalOutA1 = Pin(digitalOutA1, Pin.OUT)
        self.digitalOutA2 = Pin(digitalOutA2, Pin.OUT)
        self.digitalOutB1 = Pin(digitalOutB1, Pin.OUT)
        self.digitalOutB2 = Pin(digitalOutB2, Pin.OUT)

    def setPower(self, speed):
        self.pwmOutA.duty(int(speed * max_duty))
        self.pwmOutB.duty(int(speed * max_duty))
        
    def forward(self, speed=1):
        self.setPower(speed)
        self.digitalOutA1.on()
        self.digitalOutA2.off()
        self.digitalOutB1.on()
        self.digitalOutB2.off()


    def backward(self, speed=1):
        self.setPower(speed)
        self.digitalOutA1.off()
        self.digitalOutA2.on()
        self.digitalOutB1.off()
        self.digitalOutB2.on()
    
    def rotateRight(self, speed=1):
        self.setPower(speed)        
        self.digitalOutA1.on()
        self.digitalOutA2.off()
        self.digitalOutB1.off()
        self.digitalOutB2.on()

    def rotateLeft(self, speed=1):
        self.setPower(speed)        
        self.digitalOutA1.off()
        self.digitalOutA2.on()
        self.digitalOutB1.on()
        self.digitalOutB2.off()
