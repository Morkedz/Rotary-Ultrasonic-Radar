#Stepmotor, have motor pins be on GPIO 17,18,19,20.
#Ultrasonic Sensor, have trig pin be 23 and ech 24.
from RpiMotorLib.RpiMotorLib import BYJMotor
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import numpy as np
import time
from gpiozero import DistanceSensor

# --- Setup ---
trig_pin = 23
echo_pin = 24

ultrasonic = DistanceSensor(trigger=trig_pin, echo=echo_pin)

motor = BYJMotor("stepper", "28BYJ48")

# Radar Data
angles = []
distances = []

def live_radar():
    global angles, distances
    plt.ion()
    ax = plt.subplot(111, projection='polar')
    
    total_steps = 256 #180 degree radar
    step_delay = 0.005
    
    try:
        while True:
            for s in range(total_steps):
                motor.motor_run([17, 18, 19, 20], step_delay, 1, False, False, "half", 0)
                
                current_angle = (s / 512) * 2 * np.pi
                dist = ultrasonic.distance * 100
                
                angles.append(current_angle)
                distances.append(dist)
                
                if s % 5 == 0:
                    print(dist)
                    ax.clear()
                    ax.set_thetamin(0)
                    ax.set_thetamax(180)
                    ax.plot(angles, distances)
                    plt.pause(0.001)
            for s in range(total_steps):
                motor.motor_run([17, 18, 19, 20], step_delay, total_steps, True, False, "half", 0.05)
                current_angle = ((512-s)/512)*2*np.pi
                dist = ultrasonic.distance * 100
                angles.append(current_angle)
                distances.append(dist)

    except KeyboardInterrupt:
        print("Radar Stopped.")
    finally:
        GPIO.cleanup()
        plt.ioff()
        plt.show()
        ultrasonic.close()

if __name__ == "__main__":
    live_radar()