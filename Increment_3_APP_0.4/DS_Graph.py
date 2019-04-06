import Tkinter as tk




from numpy import arange, sin, pi





def DS_Graph1 (canvas, a, z, colour):

    fr = 5 #frequency



    
    x1 = arange(0-z,51-z)#50
    def smallamplitude1(x):
        Fs = 500
        y = 0.2*(sin(2*pi*fr*(x-(-z))/Fs))
        a.plot(y,x1,color='red')
        a.set_title('Double Slit Diffraction')
        a.set_ylim(-z,605+9*z)
        a.set_xlim(0,4)
        a.axis('off')
        
    smallamplitude1(x1)
    
    x2 = arange(50-z,112.6-z)#
    def smallamplitude1(x):
        Fs = 625
        y = 0.35*(sin(2*pi*fr*(x-(50-z))/Fs) )
        a.plot(y,x2,color='red')
    smallamplitude1(x2)
    
    x3 = arange(112.5-z,137.6-z)
    def smallamplitude1(x):
        Fs = 250
        y = 0.15*(sin(2*pi*fr*(x-(112.5-z))/Fs))
        a.plot(y,x3,color='red')
    smallamplitude1(x3)
    
    x4 = arange(137.5-z,162.6-z)
    def smallamplitude1(x):
        Fs = 250
        y = 0.15*(sin(2*pi*fr*(x-(137.5-z))/Fs))
        a.plot(y,x4,color='red')
    smallamplitude1(x4)
    
    x5 = arange(162.5-z,212.5+z)
    def smallamplitude1(x):
        Fs = 500 +(z*20)
        y = 0.8*(sin(2*pi*fr*(x-(162.5-z))/Fs))
        a.plot(y,x5,color='red')
    smallamplitude1(x5)
    
    x6 = arange(212.5+z,267.6+3*z)
    def smallamplitude1(x):
        Fs = 550 + (z*20)
        y = 2.5*(sin(2*pi*fr*(x-(212.5+z))/Fs))
        a.plot(y,x6,color='red')
    smallamplitude1(x6)
    
    x7 = arange(267.5+3*z,337.6+5*z)
    def smallamplitude1(x):
        Fs= 700 + (z*20)
        y = 4*(sin(2*pi*fr*(x-(267.5+3*z))/Fs))
        a.plot(y,x7,color='red')
    smallamplitude1(x7)
    
    x8 = arange(337.5+5*z,392.6+7*z)
    def smallamplitude1(x):
        Fs = 550 + (z*20)
        y = 2.5*(sin(2*pi*fr*(x-(337.5+5*z))/Fs))
        a.plot(y,x8,color='red')
    smallamplitude1(x8)
    
    x9 = arange(392.5+7*z,442.6+9*z)
    def smallamplitude1(x):
        Fs = 500 + (z*20)
        y = 1*(sin(2*pi*fr*(x-(392.5+7*z))/Fs))
        a.plot(y,x9,color='red')
    smallamplitude1(x9)
    
    x10 = arange(442.5+9*z,467.6+9*z)
    def smallamplitude1(x):
        Fs = 250 
        y = 0.15*(sin(2*pi*fr*(x-(442.5+9*z))/Fs))
        a.plot(y,x10,color='red')
    smallamplitude1(x10)
    
    x11 = arange(467.5+9*z,492.6+9*z) 
    def smallamplitude1(x):
        Fs = 250
        y = 0.15*(sin(2*pi*fr*(x-(467.5+9*z))/Fs))
        a.plot(y,x11,color='red')
    smallamplitude1(x11)
    
    
    x12 = arange(492.5+9*z,555+9*z)
    def smallamplitude1(x):
        Fs = 625
        y = 0.35*(sin(2*pi*fr*(x-(492.5+9*z))/Fs))
        a.plot(y,x12,color='red')
    smallamplitude1(x12)
    
    x13 = arange(555+9*z,605+9*z)
    def smallamplitude1(x):
        Fs = 500
        y = 0.2*(sin(2*pi*fr*(x-(555+9*z))/Fs))
        a.plot(y,x13,color='red')
    smallamplitude1(x13)


    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



