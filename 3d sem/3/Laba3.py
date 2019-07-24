#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:38:48 2019

@author: argus
"""

import Utarget as u
from tkinter import *
from tkinter.ttk import *

TTargetList = u.TargetList(100,1)


def StartSimulation():
    '''
    
    for i in range  (len(u.TTargetList)):
        u.TTargetList[i-1].addTarget(cpost)
        u.TTargetList[i-1].set_id(i+1)
    RLS.Pelling(t0,tk,dt,c,cpost)
    #del RLS
    for i in range (len(u.TTargetList)):
       del u.TTargetList[i-1]
    #del RLS
    '''
    t0 = float(t0_entry.get())
    tk = float(t_entry.get())
    dt = float(dt_entry.get())
    for i in range  (len(TTargetList.Items)):
        TTargetList.Items[i-1].addTarget(cpost)
    sim = u.TSimulator(cpost,RLS,t0,tk,TTargetList,c)
    sim.Run(dt)
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
        #u.TTargetList.append(plane)
        TTargetList.AddTarget(plane)
    elif var.get() == 1 :
        X = float(Xn.get())
        Y = float(Yn.get())
        Vel = float(V.get())
        K = float(Kangle.get())
        Accel = float(A.get())
        missle = u.Tmissle(X,Y,Vel,K,'missle')
        missle.addAccel(Accel)
        TTargetList.AddTarget(missle)
    elif var.get() == 2 :
        Rad = float(DetectRad.get())
        X = float(Xn.get())
        Y = float(Yn.get())
        global RLS
        RLS = u.TRLS(X,Y,Rad)
        c.create_oval(X-Rad+300, -Y-Rad+200, X+Rad+300, -Y+Rad+200, width=3, outline='green')
    elif var.get() == 3 :
        X = float(Xn.get())
        Y = float(Yn.get())
        Drad = float(DangerRadOfCP_entery.get())
        DestRad = float(DestroyRadOfCP_entery.get())
        global cpost
        cpost = u.TcomandPost(Drad,DestRad)
        cpost.InitPosition(X,Y)
        c.create_oval(X-Drad+300, -Y-Drad+200, X+Drad+300, -Y+Drad+200, width=3, outline='black')
        c.create_oval(X-DestRad+300, -Y-DestRad+200, X+DestRad+300, -Y+DestRad+200, width=3, outline='red')
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
        DangerRadOfCP_entery.place_forget()
        DestroyRadOfCP_entery.place_forget()
        DangerRadOfCP_label.place_forget()
        DestroyRadOfCP_label.place_forget()
    elif var.get() == 1 :
        V.place(relx=.2, rely=.4)
        Kangle.place(relx=.2, rely=.5)
        A.place(relx=.2, rely=.6)
        VLabel.place(relx=.2, rely=.35)
        KangleLabel.place(relx=.2, rely=.45)
        ALabel.place(relx=.2, rely=.55)
        DetectRadLabel.place_forget()
        DetectRad.place_forget
        DangerRadOfCP_entery.place_forget()
        DestroyRadOfCP_entery.place_forget()
        DangerRadOfCP_label.place_forget()
        DestroyRadOfCP_label.place_forget()
    elif var.get() == 2 :
        V.place_forget()
        A.place_forget()
        Kangle.place_forget()
        VLabel.place_forget()
        ALabel.place_forget()
        KangleLabel.place_forget()
        DetectRadLabel.place(relx=.2, rely=.35)
        DetectRad.place(relx=.2, rely=.4)
        DangerRadOfCP_entery.place_forget()
        DestroyRadOfCP_entery.place_forget()
        DangerRadOfCP_label.place_forget()
        DestroyRadOfCP_label.place_forget()
    elif var.get() == 3 :
        Kangle.place_forget()
        VLabel.place_forget()
        ALabel.place_forget()
        KangleLabel.place_forget()
        DetectRadLabel.place_forget()
        DetectRad.place_forget()
        V.place_forget()
        A.place_forget()
        DangerRadOfCP_entery.place(relx=.2, rely=.40)
        DestroyRadOfCP_entery.place(relx=.2, rely=.50)
        DangerRadOfCP_label.place(relx=.2, rely=.35)
        DestroyRadOfCP_label.place(relx=.2, rely=.45)
        
        
        
root = Tk()
root.title("Simulator")
root.geometry('800x500')

tab_parent = Notebook(root)
tab1 = Frame(tab_parent)
tab2 = Frame(tab_parent)
tab_parent.add(tab1,text="input")
tab_parent.add(tab2,text="visualization")

#button
Create_btn = Button(tab1,text = 'Create obj', command = NewTarget)
SartSim_btn = Button(tab2,text = 'Start ', command = StartSimulation)


var = IntVar()
#var.set(0)
#radiobutton
Aircraft = Radiobutton(tab1,text="Plane", variable = var, value = 0, command = hidewidget )
Missle = Radiobutton(tab1,text="Missle", variable = var, value = 1, command = hidewidget)
RLS = Radiobutton(tab1,text="RLS", variable = var, value = 2, command = hidewidget)
Cpost = Radiobutton(tab1,text="Cpost", variable = var, value = 3, command = hidewidget)
#entry
Xn = Entry(tab1)
Yn = Entry(tab1)
V  = Entry(tab1)
Kangle = Entry(tab1)
A = Entry(tab1)
DetectRad = Entry(tab1)
t0_entry = Entry(tab1)
t_entry = Entry(tab1)
dt_entry = Entry(tab1)
DangerRadOfCP_entery = Entry(tab1)
DestroyRadOfCP_entery = Entry(tab1)


#label
XnLabel = Label(tab1, text = 'X')
YnLabel = Label(tab1, text = 'Y')
VLabel  = Label(tab1, text = 'V')
KangleLabel = Label(tab1, text = 'K')
ALabel = Label(tab1, text = 'A')
DetectRadLabel = Label(tab1, text = 'Detection radius')

t0_label = Label(tab1, text = 't0')
t_label = Label(tab1, text = 't')
dt_label = Label(tab1, text = 'dt')
DangerRadOfCP_label = Label(tab1, text = 'Danger radius')
DestroyRadOfCP_label = Label(tab1, text = 'Destroy radius')
#
tab_parent.pack(expand=1, fill='both')

#label place
XnLabel.place(relx=.2, rely=.15)
YnLabel.place(relx=.2, rely=.25)
VLabel.place(relx=.2, rely=.35)
KangleLabel.place(relx=.2, rely=.45)
t0_label.place(relx=.4, rely=.25)
t_label.place(relx=.4, rely=.35)
dt_label.place(relx=.4, rely=.45)

#canvas
c = Canvas(tab2, width=600, height=400, bg='white')
c.create_line(300, 0, 300, 400)
c.create_line(0, 200, 600, 200)

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
Cpost.place(relx=.0, rely=.35)
#btn place
Create_btn.place(relx=.0, rely=.7)
SartSim_btn.place(relx=.0, rely=.8)

#canvas place
c.place(relx=.1, rely=.0)

root.mainloop()
 
 