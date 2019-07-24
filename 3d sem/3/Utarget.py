#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:40:04 2019

@author: argus
"""
import math as m
import abc 
import Int
import time as t



#cp = TcomandPost() 

class Tlist():
    
    
    def __init__(self,cap,ct):
        self.capacity = cap
        self.count  = ct
        self.Items = []
        
class TargetList(Tlist):
    
    def set_id(self,n):
        self.ID = n
        print('for target:',self.TypeOfTarget,'ID set to : ',n)
    def get_id(self):
        return self.ID
    def del_id(self):
        self.ID = 'no'
    ID = property(get_id,set_id,del_id)
    
    def Insert(self,target,i):
        self.Items.insert(i,target)
    def Delite(self,target):
        self.Items.remove(target)
    def AddTarget(self,target):
        self.Items.append(target)
    
class Tpoint():
    #property()
    def set_x(self,x):
        self.X = x
    def get_x(self):
        return self.X
    def del_x(self):
        self.X = 'no'
    x = property(set_x,get_x,del_x)
    
    def set_y(self,y):
        self.Y = y
    def get_y(self):
        return self.Y
    def del_y(self):
        self.Y = 'no'
    y = property(set_y,get_y,del_y)

class TPosObject(Tpoint):
    def InitPosition(self,x,y):
        self.X = x
        self.Y = y
        self.currentTime = 0
    def set_currentTime(self,time):
        self.currentTime = time
    def get_currentTime(self):
        return self.currentTime
   


class TcomandPost(TPosObject):
    def __init__(self,DangerRad,DestroyRad):
           self.DangerRad = DangerRad
           self.DestroyRad = DestroyRad
    def check(TTarget):
        pass

        
class TTarget(TPosObject):
    #@abc.abstractmethod
    def __init__(self,Xn,Yn,V,Kangle,TypeOfTarget):
        self.set_x(Xn)
        self.set_y(Yn)
        self.V = V
        self.Kangle = 0
        self.TypeOfTarget = TypeOfTarget
        self.P = 10
        self.Vmass = 10
        #self.currentTime = 0
        #self.X = 0
        #self.Y = 0
        print('obj has been created')
        
        
        
    def addTarget(self,target):
        self.DeligateTarget = target
        print('target add for :', self.TypeOfTarget, ', with ID:')
    def __del__(self):
        print('object deleted')
          
    @abc.abstractmethod
    def move(self,time):
        pass
    
class Taircraft(TTarget):
    
    
    
    def move(self,time,I):
        X = self.DeligateTarget.get_x()
        Y = self.DeligateTarget.get_y()
        tx = X
        ty = Y
        X = self.get_x()
        Y = self.get_y()
        
        if X > 0 :
            if Y >0 :
                self.Kangle =( m.atan((ty-Y)/(tx-X)))
            elif Y < 0 :
                self.Kangle =  (m.atan((ty-Y)/(tx-X)))
        elif X < 0 :
            if Y < 0 :
                self.Kangle = (-m.pi + m.atan((ty-Y)/(tx-X)))
            elif Y > 0 :
                self.Kangle = (m.pi + m.atan((ty-Y)/(tx-X)))
        
        I.integrate(self,time)  
        TTarget.set_currentTime(self,time)

class Tmissle(TTarget):
    def addAccel(self,Accel):
        self.Accel = Accel
    
    def move(self,time,I):
        
        
        X = self.DeligateTarget.get_x()
        Y = self.DeligateTarget.get_y()
        tx = X
        ty = Y
        X = self.get_x()
        Y = self.get_y()
        
        if X > 0 :
            if Y >0 :
                self.Kangle = m.atan((ty-Y)/(tx-X))
            elif Y < 0 :
                self.Kangle = m.atan((ty-Y)/(tx-X))
        elif X < 0 :
            if Y < 0 :
                self.Kangle = -m.pi + m.atan((ty-Y)/(tx-X))
            elif Y > 0 :
                self.Kangle = m.pi + m.atan((ty-Y)/(tx-X))
        
        I.integrate(self,time)  
        TTarget.set_currentTime(self,time)

        #t0 = 0
        #x = self.Xn - (self.V + self.Accel * (time - t0)) * m.cos(self.Kangle) * (time - t0)
        #y = self.Yn - (self.V + self.Accel * (time - t0)) * m.sin(self.Kangle) * (time - t0)
#        TTarget.set_x(self,x)
#        TTarget.set_y(self,y)
#        TTarget.set_currentTime(self,time)
        

class TsamMissle(Tmissle):
    def addTsamParams(self,target):
         pass






class TRLS():
    def __init__(self,RLSx,RLSy,RLSrad):
        self.RLSx = RLSx
        self.RLSy = RLSy
        self.RLSrad = RLSrad
    def Pelling(self,curTime,TTarget,canvas,f):
             print('start pelling')
        #f = open('/home/argus/MAI_Study/KT labs python/3d sem/2/text.txt', 'w')
        #t = t0
        #global cp
        #cp = cpost
        #global I
        #I = Int.IntEuler(dt)
       # while t <= tk :
        #    for j in range (len(TTargetList)):
         #    TTargetList[j].move(t)
          #   t = t + dt
             D = m.sqrt((TTarget.X - self.RLSx) ** 2 + (TTarget.Y - self.RLSy) ** 2)
             if D <= self.RLSrad :
                try:
                 Az = m.atan((TTarget.Y - self.RLSy)/(TTarget.X-self.RLSx))
                except :
                    Az = 0
                x = TTarget.get_x()
                y = TTarget.get_y()
                if TTarget.TypeOfTarget == 'plane' :
                    canvas.create_oval(x-2+300, -y-2+200, x+2+300, -y+2+200, width=1, outline='blue')
                elif TTarget.TypeOfTarget == 'missle' :
                    canvas.create_oval(x-2+300, -y-2+200, x+2+300, -y+2+200, width=1, outline='orange')
                
                
                f.write('target '+str(j+1)+'\n')
                f.write('time '+str(curTime) + '\n')
                f.write('X--' + str(x) + '\n')
                f.write('Y--' + str(y) + '\n')
                f.write('azimut  ' + str(Az) + '\n')
                f.write('                           ' + '\n')
                f.write('                           ' + '\n')
        
    def __dell__(self):
        print('RLS destroyed')
        
        
class TSimulator():
    def __init__(self,cpost,RLS,t0,tk,TTargetList,canvas):
        self.CountDeligateSam = 0
        self.CountLoseTarget = 0
        self.CountTarget = 0
        self.CP = cpost
        self.TextFile = open('/home/argus/MAI_Study/KT labs python/3d sem/3/text.txt', 'w')
        self.RlS = RLS
        self.SamMissleList = TargetList(100,1)
        self.T0 = t0
        self.Tk = tk
        self.Targets = TTargetList.Items
        self.canvas = canvas
        
        
        
    def Run(self,dt):
        I = Int.IntEuler(dt) 
        curTime = self.T0
        while curTime <= self.Tk :
            for j in range (len(self.Targets)):
                self.RlS.Pelling(curTime,self.Targets[j],self.canvas,self.TextFile)
                self.Targets[j].move(curTime,I)
            curTime += dt
            
        self.TextFile.close()        
                
                