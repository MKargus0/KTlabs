#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:38:48 2019

@author: argus
"""

import Utarget as u
from tkinter import *



def StartSimulation():
    t0 = float(t0_entry.get())
    tk = float(t_entry.get())
    dt = float(dt_entry.get())
    RLS.Pelling(t0,tk,dt)
    
    

def NewTarget():
    '''
    X = float(Xn.get())
    Y = float(Yn.get())
    Vel = float(V.get())
    K = float(Kangle.get())
    Accel = float(A.get())
    '''
    if var.get() == 0 :
        X = float(Xn.get())
        Y = float(Yn.get())
        Vel = float(V.get())
        K = float(Kangle.get())
        plane = u.Taircraft(X,Y,Vel,K,'plane')
        u.TTargetList.append(plane)
    elif var.get() == 1 :
        X = float(Xn.get())
        Y = float(Yn.get())
        Vel = float(V.get())
        K = float(Kangle.get())
        Accel = float(A.get())
        missle = u.Tmissle(X,Y,Vel,K,'plane')
        missle.addAccel(Accel)
        u.TTargetList.append(missle)
    elif var.get() == 2 :
        Rad = float(DetectRad.get())
        X = float(Xn.get())
        Y = float(Yn.get())
        global RLS
        RLS = u.TRLS(X,Y,Rad)
    
def hidewidget():
    if var.get() == 0 :
        V.place(relx=.2, rely=.4)
        Kangle.place(relx=.2, rely=.5)
        VLabel.place(relx=.2, rely=.35)
        KangleLabel.place(relx=.2, rely=.45)
        A.place_forget()
        ALabel.place_forget()
        DetectRadLabel.place_forget()
        DetectRad.place_forget
    elif var.get() == 1 :
        V.place(relx=.2, rely=.4)
        Kangle.place(relx=.2, rely=.5)
        A.place(relx=.2, rely=.6)
        VLabel.place(relx=.2, rely=.35)
        KangleLabel.place(relx=.2, rely=.45)
        ALabel.place(relx=.2, rely=.55)
        DetectRadLabel.place_forget()
        DetectRad.place_forget
    elif var.get() == 2 :
        V.place_forget()
        A.place_forget()
        Kangle.place_forget()
        VLabel.place_forget()
        ALabel.place_forget()
        KangleLabel.place_forget()
        DetectRadLabel.place(relx=.2, rely=.35)
        DetectRad.place(relx=.2, rely=.4)

root = Tk()
root.title("Simulator")
root.geometry('800x500')

#button
Create_btn = Button(text = 'Create obj', command = NewTarget)
SartSim_btn = Button(text = 'Start ', command = StartSimulation)


var = IntVar()
#var.set(0)
#radiobutton
Aircraft = Radiobutton(text="Plane", variable = var, value = 0, command = hidewidget )
Missle = Radiobutton(text="Missle", variable = var, value = 1, command = hidewidget)
RLS = Radiobutton(text="RLS", variable = var, value = 2, command = hidewidget)
#entry
Xn = Entry(root)
Yn = Entry(root)
V  = Entry(root)
Kangle = Entry(root)
A = Entry(root)
DetectRad = Entry(root)
t0_entry = Entry(root)
t_entry = Entry(root)
dt_entry = Entry(root)
#label
XnLabel = Label(root, text = 'X')
YnLabel = Label(root, text = 'Y')
VLabel  = Label(root, text = 'V')
KangleLabel = Label(root, text = 'K')
ALabel = Label(root, text = 'A')
DetectRadLabel = Label(root, text = 'Detection radius')

t0_label = Label(root, text = 't0')
t_label = Label(root, text = 't')
dt_label = Label(root, text = 'dt')
#label place
XnLabel.place(relx=.2, rely=.15)
YnLabel.place(relx=.2, rely=.25)
VLabel.place(relx=.2, rely=.35)
KangleLabel.place(relx=.2, rely=.45)
t0_label.place(relx=.4, rely=.25)
t_label.place(relx=.4, rely=.35)
dt_label.place(relx=.4, rely=.45)

#ALabel.place(relx=.2, rely=.55)
#entryplace
Xn.place(relx=.2, rely=.2)
Yn.place(relx=.2, rely=.3)
V.place(relx=.2, rely=.4)
Kangle.place(relx=.2, rely=.5)
t0_entry.place(relx=.4, rely=.3)
t_entry.place(relx=.4, rely=.4)
dt_entry.place(relx=.4, rely=.5)
#A.place(relx=.2, rely=.6)
#radiobutton place
Aircraft.place(relx=.0, rely=.2)
Missle.place(relx=.0, rely=.25)
RLS.place(relx=.0, rely=.3)

#btn place
Create_btn.place(relx=.0, rely=.7)
SartSim_btn.place(relx=.0, rely=.8)

root.mainloop()
 
 