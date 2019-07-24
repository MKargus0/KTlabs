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
        print('obj has been created')
    def __del__(self):
        print('object deleted')
        
    def set_x(self,x):
        self.X = x
    def get_x(self):
        return self.X
    def set_y(self,y):
        self.Y = y
    def get_y(self):
        return self.Y
    def set_currentTime(self,time):
        self.currentTime = time
    def get_currentTime(self):
        return self.currentTime
    
    @abc.abstractmethod
    def move(self,time):
        pass
    
class Taircraft(TTarget):
    pass
    def move(self,time):
        t0 = 0
        #self.currentTime = time
        x = self.Xn - self.V * m.cos(self.Kangle)*(time - t0)
        y = self.Yn - self.V * m.sin(self.Kangle)*(time - t0)
        TTarget.set_x(self,x)
        TTarget.set_y(self,y)
        TTarget.set_currentTime(self,time)

class Tmissle(TTarget):
    def addAccel(self,Accel):
        self.Accel = Accel
    def move(self,time):
        t0 = 0
        x = self.Xn - (self.V + self.Accel * (time - t0)) * m.cos(self.Kangle) * (time - t0)
        y = self.Yn - (self.V + self.Accel * (time - t0)) * m.sin(self.Kangle) * (time - t0)
        TTarget.set_x(self,x)
        TTarget.set_y(self,y)
        TTarget.set_currentTime(self,time)
        

class TRLS():
    def __init__(self,RLSx,RLSy,RLSrad):
        self.RLSx = RLSx
        self.RLSy = RLSy
        self.RLSrad = RLSrad
    def Pelling(self,t0,tk,dt):
        print('start pelling')
        f = open('/home/argus/MAI_Study/KT labs python/3d sem/2/text.txt', 'w')
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
                x = TTargetList[j].get_x()
                y = TTargetList[j].get_y()
                currentTime = TTargetList[j].get_currentTime()
                
                f.write('target '+str(j+1)+'\n')
                f.write('time '+str(currentTime) + '\n')
                f.write('X--' + str(x) + '\n')
                f.write('Y--' + str(y) + '\n')
                f.write('azimut  ' + str(Az) + '\n')
                f.write('                           ' + '\n')
                f.write('                           ' + '\n')
        f.close()
    def __dell__(self):
        print('RLS destroyed')
        
        
