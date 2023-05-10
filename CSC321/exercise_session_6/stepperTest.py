# from time import sleep_ms
# from zstepper import Stepper
# stepper = Stepper(18, 19, 21, 22)
# 
# stepper.stepMode(stepper.SINGLE_PHASE_FORWARD)
# stepper.waitAfterSteps(2)
# stepper.clrAll()
# stepper.move(100000)
# sleep_ms(1000)
# 
# stepper.stepMode(stepper.SINGLE_PHASE_BACKWARD)
# stepper.waitAfterSteps(2)
# stepper.clrAll()
# stepper.move(100000)
# sleep_ms(1000)
# 
# stepper.stepMode(stepper.DOUBLE_PHASE_FORWARD)
# stepper.waitAfterSteps(2)
# stepper.clrAll()
# stepper.move(100000)
# sleep_ms(1000)
# stepper.stepMode(stepper.DOUBLE_PHASE_BACKWARD)
# stepper.waitAfterSteps(2)
# stepper.clrAll()
# stepper.move(100000)
# sleep_ms(1000)
# 
# stepper.stepMode(stepper.HALF_STEP_FORWARD)
# stepper.waitAfterSteps(2)
# stepper.clrAll()
# stepper.move(100000)
# sleep_ms(1000)
# 
# stepper.stepMode(stepper.HALF_STEP_BACKWARD)
# stepper.waitAfterSteps(2)
# stepper.clrAll()
# stepper.move(100000)
# sleep_ms(1000)

from stepper import steppingMotor 
stepper = steppingMotor(18, 19, 21, 22)
stepper.stepMode(stepper.SINGLE_PHASE_FORWARD)
stepper.waitAfterSteps(2)
stepper.clrAll()
stepper.move(4096)
