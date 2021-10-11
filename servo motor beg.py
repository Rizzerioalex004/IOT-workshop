from machine import Pin,PWM
servo = PWM(Pin(14), freq=1)
servo.duty(40)
#duty cycle from 20 to 120 rotate motor from 0 to 180 deg
#no idea about anti clockwise rotation
#sch: orange-14, red- 5v, brown-Gnd
#didn't run bcoz got no external source for motor