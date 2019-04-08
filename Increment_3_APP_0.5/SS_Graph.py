
import Tkinter as tk


from numpy import arange, sin, pi,cos 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib.figure import Figure



def SS_Graph1 (canvas, a, z, colour):
    

    Fs = 5000#rate
    fr = 5 #frequency 
    sample = -5000
    x = arange(sample)
    y = sin(2*pi*fr*x/Fs)
    
    
    
    
    x0 = arange(0-z,51-z)#50
    def smallamplitude1(x):
        Fs = 500
        y = 0.02*(sin(2*pi*fr*(x-(-z))/Fs))
        a.plot(y,x0,color=colour)
        a.set_ylim(-z,340+z)
        a.set_xlim(0,0.305)
        a.axis('off')
    smallamplitude1(x0)
    
    x1 = arange(50-z,121-z)#70
    def smallamplitude1(x):
        Fs = 700
        y = 0.07*(sin(2*pi*fr*(x-(50-z))/Fs))
        a.plot(y,x1,color=colour)
    smallamplitude1(x1)
    
    
    x2 = arange(120-z,221+z)#100
    def smallamplitude1(x):
        Fs = 1000+(z*20)
        y = 0.3*(sin(2*pi*fr*(x-(120-z))/Fs))
        a.plot(y,x2,color=colour)
    smallamplitude1(x2) 
    
    x4 = arange(220+z,291+z)#70
    def smallamplitude1(x):
        Fs = 700
        y = 0.07*(sin(2*pi*fr*(x-(220+z))/Fs)) 
        a.plot(y,x4,color=colour)
    smallamplitude1(x4)
    
    x5 = arange(290+z,341+z)#50
    def smallamplitude1(x):
        Fs = 500
        y = 0.02*(sin(2*pi*fr*(x-(290+z))/Fs))
        a.plot(y,x5,color=colour)
    smallamplitude1(x5)
    
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



