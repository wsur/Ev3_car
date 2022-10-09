#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import Direction
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port


g = GyroSensor(Port.S1)

# Initialize a motor at port B.
test_motor = Motor(Port.A)
# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
#test_motor.run_target(500, 180)


test1_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
#test1_motor.run_target(500, 180)



#turn = -1
while(True):
    #turn *= -1
    for i in range(1000):
        if g.angle() < -90:
            test_motor.stop()
            test1_motor.stop()
            break
        #test_motor.run_target(500, i*540)
        test_motor.run(400)
        test1_motor.run(400)
        brick.display.clear()
        brick.display.text(g.angle(), (50,50))
    g.reset_angle(0)
    #elif g.angle() < 90

brick.display.clear()
brick.display.text(g.angle(), (50,50))
g.reset_angle(0)
brick.display.text("AAAAAAAAAAAAAAAAAAAA")

