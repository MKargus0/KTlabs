#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:29:09 2019

@author: argus
"""

import math as m

dt = 1
Smid = 1
Cx = 1#coef force of front rebelian
Patm = 1

CriticalFuelMass = 1
FuelDraw = 0.00000001
mass = 10
P = 10




def frontForce(self):
    X = Cx * ((Patm * self.V ** 2)/2) * Smid
    print('Xf--',X)
    return X

class IntEuler():
    
    
 def __init__(self,dt):
     global h
     h = dt
 
 def integrate(I,self,time):
    mass = self.Vmass + self.P
    X = frontForce(self)
    if self.TypeOfTarget == 'plane':
        self.V += ((self.P - X) / mass) * h
    elif self.TypeOfTarget == 'missle':
        self.V += (((self.P - X) / mass) + self.Accel) * h
    self.P -= FuelDraw
    print('P--', self.P)
    x = self.get_x()
    y = self.get_y()
    Xc = x
    Yc = y
    Xc = Xc - (self.V * m.cos(self.Kangle) * h)
    Yc = Yc - (self.V * m.sin(self.Kangle) * h)
    self.set_x(Xc)
    self.set_y(Yc)
    print('X--',Xc)
    print('Y--',Yc) 
    print('V--',self.V)
    #return V , Xc , Yc , P ,X
'''
time = 0
totaltime = 100
V = 10
Xc = 111
Yc = 111
K = 1
Vmass = 1000
while time <= totaltime:   
    time += dt
    V,Xc,Yc,P,X = integrate(Xc,Yc,time,V,P,K,Vmass)
'''    
#dt = 0.1
#I = IntEuler()   
    
    