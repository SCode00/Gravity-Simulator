# Gravity Simulator
A simple 2D simulation of gravitational interactions between planets using Newton's Law

## Features
 - Add new planets instantly by clicking anywhere on the screen
 - Visual history of each body's path to see trajectories
 - Uses NumPy for position and velocity calculations

## How it works
 - Physics: Calculates F = G(m1*m2/(d**2)) for all pairs
 - Updates speed, position and acceleration via Euler Method at 60 FPS
 - Each planet is a Body class instance
