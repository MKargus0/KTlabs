#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:40:04 2019

@author: argus
"""
import math as m
import abc 

TTargetList = []

class TTarget():
    #@abc.abstractmethod
    def __init__(self,Xn,Yn,V,Kangle,TypeOfTarget):
        self.Xn = Xn
        self.Yn = Yn
        self.V = V
        self.Kangle = Kangle
        self.TypeOfTarget = TypeOfTarget
        self.currentTime = 0
        self.X = 0
        self.Y = 0
        #print(TypeOfTarget, 'has been created')
    def __del__(self):
        print('object deleted')
    @abc.abstractmethod
    def move(self,time):
        pass
    
class Taircraft(TTarget):
    pass
    def move(self,time):
        t0 = 0
        self.currentTime = time
        self.X = self.Xn - self.V * m.cos(self.Kangle)*(time - t0)
        self.Y = self.Yn - self.V * m.sin(self.Kangle)*(time - t0)


class Tmissle(TTarget):
    def addAccel(self,Accel):
        self.Accel = Accel
    def move(self,time):
        t0 = 0
        self.currentTime = time
        self.X = self.Xn - (self.V + self.Accel * (time - t0)) * m.cos(self.Kangle) * (time - t0)
        self.Y = self.Yn - (self.V + self.Accel * (time - t0)) * m.sin(self.Kangle) * (time - t0)
        
        

class TRLS():
    def __init__(self,RLSx,RLSy,RLSrad):
        self.RLSx = RLSx
        self.RLSy = RLSy
        self.RLSrad = RLSrad
    def Pelling(self,t0,tk,dt):
        f = open('/home/argus/MAI_Study/KT labs python/3d sem/1/text.txt', 'w')
        t = t0
        while t != tk :
            for j in range (len(TTargetList)):
             TTargetList[j].move(t)
             t = t + dt
             if t >= tk :
                 break
             else:
              D = m.sqrt((TTargetList[j].X - self.RLSx) ** 2 + (TTargetList[j].Y - self.RLSy) ** 2)
              if D <= self.RLSrad :
                Az = m.atan((TTargetList[j].Y - self.RLSy)/(TTargetList[j].X-self.RLSx))
                f.write('target '+str(j+1)+'\n')
                f.write('time '+str(TTargetList[j].currentTime) + '\n')
                f.write('X--' + str(TTargetList[j].X) + '\n')
                f.write('Y--' + str(TTargetList[j].Y) + '\n')
                f.write('azimut  ' + str(Az) + '\n')
                f.write('                           ' + '\n')
                f.write('                           ' + '\n')
        f.close()
    def __dell__(self):
        print('RLS destroyed')
        
        
