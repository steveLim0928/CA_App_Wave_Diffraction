#import matplotlib
#import matplotlib.pyplot as plt
import Tkinter as tk
#import numpy as np

from numpy import arange, sin, pi 
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib.figure import Figure
root = tk.Tk()
root.wm_title("Graph of Single slit Diffraction")



f = Figure(figsize=(4,4),dpi=100)
a = f.add_subplot(111)

#Fs = 5000#rate
fr = 5 #frequency 
#sample = -5000
#x = arange(sample)
#y = sin(2*pi*fr*x/Fs)

#gap size
z = 40 # <--------- For all changes


x0 = arange(0-z,51-z)#50
def smallamplitude1(x):
    Fs = 500
    y = 0.02*(sin(2*pi*fr*(x-(-z))/Fs))
    a.plot(-y,x0,color='orange')
    a.set_title('Single Slit Diffraction')
    a.set_ylim(-z,340+z)
    a.set_xlim(-0.5,0)
    a.axis('off')
smallamplitude1(x0)

x1 = arange(50-z,121-z)#70
def smallamplitude1(x):
    Fs = 700
    y = 0.07*(sin(2*pi*fr*(x-(50-z))/Fs))
    a.plot(-y,x1,color='orange')
smallamplitude1(x1)


x2 = arange(120-z,221+z)#100
def smallamplitude1(x):
    Fs = 1000+(z*20)
    y = 0.3*(sin(2*pi*fr*(x-(120-z))/Fs))
    a.plot(-y,x2,color='orange')
smallamplitude1(x2) 

x4 = arange(220+z,291+z)#70
def smallamplitude1(x):
    Fs = 700
    y = 0.07*(sin(2*pi*fr*(x-(220+z))/Fs)) 
    a.plot(-y,x4,color='orange')
smallamplitude1(x4)

x5 = arange(290+z,341+z)#50
def smallamplitude1(x):
    Fs = 500
    y = 0.02*(sin(2*pi*fr*(x-(290+z))/Fs))
    a.plot(-y,x5,color='orange')
smallamplitude1(x5)


canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

tk.mainloop()

