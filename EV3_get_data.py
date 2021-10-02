#!/usr/bin/env python3
from ev3dev.ev3 import *
import time

motorA = LargeMotor('outA')

for v in range(-100, 101):
    if v == 0: continue
    res = []
    motorA.run_direct(duty_cycle_sp=v)
    timeStart = time.time()
    startValue = motorA.position
    while time.time() - timeStart < 1:
        res.append(tuple([time.time() - timeStart, motorA.position - startValue, motorA.speed]))
    motorA.run_direct(duty_cycle_sp=0)
    time.sleep(1.2)
    with open('out_speed_{}.txt'.format(str(v)), 'w') as f:
        f.write("time angle speed\n")
        for row in res:
            f.write(' '.join(map(str, row)))
            f.write('\n')
