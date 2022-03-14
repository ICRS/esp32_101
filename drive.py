from machine import Pin
from machine import PWM
import machine

import time

max_duty = 1023
pwm_frequency = 50000

class DriveBase:
    def __init__(self, pwmOutA, pwmOutB, 
            digitalOutA1, digitalOutA2, 
            digitalOutB1, digitalOutB2):
        self.pwmOutA = PWM(Pin(pwmOutA), pwm_frequency)
        self.pwmOutB = PWM(Pin(pwmOutB), pwm_frequency)

        self.digitalOutA1 = Pin(digitalOutA1, Pin.OUT)
        self.digitalOutA2 = Pin(digitalOutA2, Pin.OUT)
        self.digitalOutB1 = Pin(digitalOutB1, Pin.OUT)
        self.digitalOutB2 = Pin(digitalOutB2, Pin.OUT)

    def __getDuty(self, speed):
        return int(abs(speed) * max_duty)

    def setPower(self, speed):
        duty = self.__getDuty(speed)
        self.pwmOutA.duty(duty)
        self.pwmOutB.duty(duty)
        
    def setLeft(self, speed):
        self.pwmOutA.duty(self.__getDuty(speed))
        if(speed >= 0):
            self.digitalOutA1.on()
            self.digitalOutA2.off()
        else:
            self.digitalOutA1.off()
            self.digitalOutA2.on()

    def setRight(self, speed):
        self.pwmOutB.duty(self.__getDuty(speed))
        if(speed >= 0):
            self.digitalOutB1.on()
            self.digitalOutB2.off()
        else:
            self.digitalOutB1.off()
            self.digitalOutB2.on()

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

    def initLeftSensor(self, trig, echo):
        self.leftUltraSound = UltraSoundSensor(trig, echo)

    def initRightSensor(self, trig, echo):
        self.rightUltraSound = UltraSoundSensor(trig, echo)

    def getLeftDistance(self):
        return self.leftUltraSound.getDistance()

    def getRightDistance(self):
        return self.rightUltraSound.getDistance()

class UltraSoundSensor:
    def __init__(self, trig, echo):
        self.trig = Pin(trig, Pin.OUT)
        self.echo = Pin(echo, Pin.IN)

    def getDistance(self):
        self.trig.value(0)
        time.sleep_us(5)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)

        try:
            pulse = machine.time_pulse_us(self.echo, 1, 500*2*30)
            return pulse * 100 / 582 
        except OSError as ex:
            raise OSError("OUT OF RANGE")

