1#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:38:48 2019

@author: argus
"""

import Utarget as u

TTargetList = []

print ('   Model    ')
print('-------------')
print('input type of target')

while True:
 i = 0
 while i == 0 :
  print('input type of target')
  print('1 - plane , 2 - missle , 3 - next step')
  TargetType = input() 
  if TargetType == '1':
      print('input X of plane')
      Xn = float(input())
      print('input Y of plane')
      Yn = float(input())
      print('input Velocity of plane')
      V = float(input())
      print('input course angle for plane')
      Kangle = float(input())
      #TargetType = 1
      Plane = u.Taircraft(Xn,Yn,V,Kangle,TargetType)
      u.TTargetList.append(Plane)
  elif TargetType == '2':
      print('input X of missle')
      Xn = float(input())
      print('input Y of missle')
      Yn = float(input())
      print('input Velocity of missle')
      V = float(input())
      print('input acceleration of missle')
      Accel = float(input())
      print('input course angle for missle')
      Kangle = float(input())
      missle = u.Tmissle(Xn,Yn,V,Kangle,TargetType)
      missle.addAccel(Accel)
      u.TTargetList.append(missle)
  elif TargetType == '3':
      i = 3
  else :
      print('try again')
 print('input RLS coord ')
 print('input X of RLS')
 RLSx = float(input())
 print('input Y of RLS')
 RLSy = float(input())
 print('input detection radius')
 RLSrad = float(input())
 RLS1 = u.TRLS(RLSx,RLSy,RLSrad)
 print('input t0 , then t')
 try :
  t0 = float(input())
  t1 = float(input())
  dt = float(input())
 except:
     print('error')
 print ('start modeling - 1, reset setings - 2 , exit - 3')
 status = int(input())
 if status == 1 :    
     RLS1.Pelling(t0,t1,dt)
     print('1-exit, 2-new model')
     status = int(input())
     if status == 1 :
         break
     elif status == 2:
         pass
 elif status == 2 :
    pass
 elif status == 3 :
  break     
 
 