# Radar Project
Raspberry Pi design utilizing 28BYJ-48 stepper motor and HC-SR04 ultrasonic sensor to perform 180 degree environment scanning, projected onto a live update polar graph.

## Trouble Shooting
**April 10, 2026:** Modified code to use built-in gpiozero distance getting method, however, failed return echo signal. Need work on distance graphing.
**April 18, 2026:** Hardware: Electromagnetic Interference is causing innacurate distance readings. Crude method of "bundling and unbundling" motor and sensor wires to determine cause. Motor pulses interference with echo readings through Inductive Coupling.