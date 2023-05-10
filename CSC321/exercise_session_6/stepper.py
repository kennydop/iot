from machine import Pin
from time import sleep_ms

class Stepper():
    SINGLE_PHASE_FORWARD = 0
    SINGLE_PHASE_BACKWARD = 1
    DOUBLE_PHASE_FORWARD = 2
    DOUBLE_PHASE_BACKWARD = 3
    HALF_STEP_FORWARD = 4
    HALF_STEP_BACKWARD = 5
    
    def __init__(self, p1 = 18, p2 = 19, p3 = 21, p4 = 22):
        self.p1 = Pin(p1)
        self.p2 = Pin(p2)
        self.p3 = Pin(p3)
        self.p4 = Pin(p4)
        self.wait_for_steps = 2
        self.mode = 0
    
    def clrAll(self):
        self.p1.value(0)
        self.p2.value(0)
        self.p3.value(0)
        self.p4.value(0)
        
    def stepMode(self, mode = 0):
        self.mode = mode
    
    def waitAfterSteps(self, dur = 2):
        self.wait_for_steps = dur
        
    def move(self, noOfSteps):
        print(noOfSteps)
        pins = [self.p1, self.p2, self.p3, self.p4]
        
        if self.mode in [1, 3, 5]:
            pins.reverse()
        
        half_turn_two = False
        i = 0                                                                                                                              
        
        while i < noOfSteps:
#           single
            if self.mode in [0, 1]:
                self._turn_on([pins[i % 4]])
                
#           double
            if self.mode in [2, 3]:
                self._turn_on([pins[i % 4], pins[(i + 1) % 4]])

#           half
            if self.mode in [4, 5]:
                if half_turn_two:
                    self._turn_on([pins[i % 4], pins[(i - 1) % 4]])
                    i -= 1
                else:
                    self._turn_on([pins[i % 4]])
                
                half_turn_two = not half_turn_two
            
            i += 1    
            sleep_ms(self.wait_for_steps)
            
    def _turn_on(self, pins_to_turn_on):
        pins = [self.p1, self.p2, self.p3, self.p4]
        for p in pins:
            if p in pins_to_turn_on:
                p.value(1)
            else:
                p.value(0)


stepper = Stepper(18, 19, 21, 22)
stepper.stepMode(stepper.HALF_STEP_FORWARD)
stepper.waitAfterSteps(2)
stepper.clrAll()
stepper.move(4096)