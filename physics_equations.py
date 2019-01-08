#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 00:01:04 2019

@author: kunalsinghramchurn
"""



## Physics equations
'''
These will be divided up into several segments. The first section is temperature, followed by movements.
'''
# fahrenheit to celsius

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

print(f_to_c(100))

#celsius to fahrenheit

def c_to_f(c_temp):
  f_temp = (c_temp * (9/5)) + 32
  return f_temp


c0_in_fahrenheit = c_to_f(0)


# Movement equations


# force
def get_force(mass, acceleration):
  return mass * acceleration

# Energy -- assumption that C = 3x10^8
def get_energy(mass, c = 3*10**8): 
  return mass * c**2

# Pressure
def pressure(force, area):
    return force / area


# Work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

# Speed
def speed(distance, time):
    return distance / time
    
# Acceleration
def acceleration(speed_1, speed_2, time):
    d_speed = speed_2 - speed_1
    return d_speed / time

# Work done 
def work_done(force, distance):
    return force * distance

# Gravitational Potential Energy
def gpe(mass, field_strength, height):
    return mass * field_strength * height

# Wave speed 
def wave_speed(freq, wavelength):
    return freq * wavelength



    