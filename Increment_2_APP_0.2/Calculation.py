
global n
n = 1

import Tkinter
import math
from math import *


def answer(gap, offset, wavelength):
    global root
    root = Tkinter.Tk()
    root.title('Single Slit calculation')
    root.geometry("450x300")
    root.resizable(False, False)
    
    frame = Tkinter.Frame(root, width = 450, height = 300, bg = 'black')
    frame.place(x = 0, y = 0)
    
    global Answer, Answer_1, Answer_2, answ
    A = float(gap/1000)
    D = float(offset)
    LAMBDA = float(wavelength)
    Answer = (((math.asin(float((((n*LAMBDA)/A)/1000000000))))))
    Answer_1 = ((((math.asin(float(((n*LAMBDA)/A)/1000000000)))))*D)
    Answer_2 = ((((math.asin(float(((n+(0.5)*LAMBDA)/A)/1000000000)*D)))))
   
    answ = ('Theta:' , Answer , 'Bright Fringes: ', Answer_1, 'Dark Fringes: ', Answer_2)
    
    theta = Tkinter.Label(frame, text = ('Theta', Answer), fg = 'white', bg = 'black')
    theta.place(x = 0, y = 0)
    
    Bright_frindge = Tkinter.Label(frame, text = ('Distance between bright fringes', Answer_1), 
                                   fg = 'white', bg = 'black')
    Bright_frindge.place(x = 0, y = 20)
    
    dark_frindge = Tkinter.Label(frame, text = ('Distance between dark fringes', Answer_2),
                                 fg = 'white', bg = 'black')
    dark_frindge.place(x = 0, y = 40)
    
    
    
    Home = Tkinter.Button(frame, text = 'Home', command = get_home, 
                              state = 'normal', pady = 2, padx = 5, bd = 3)
    Home.place(x = 250, y = 270)


    quiz = Tkinter.Button(frame, text = 'Proceed to quiz', command = get_quiz, 
                              state = 'normal', pady = 2, padx = 5, bd = 3)
    quiz.place(x = 330, y = 270)


    back_button = Tkinter.Button(frame, text = 'Back to animation', command = get_back,
                             state = 'normal', pady = 2, padx = 5, bd = 3)
    back_button.place(x = 0, y = 270)
    
    
    
    root.mainloop()
    
def get_back():
    global root
    root.destroy()
    execfile ('SS_Animation1.py',globals())
    
def get_quiz():
    global root
    root.destroy()
    execfile ('INS_QUIZ.py',globals())
    
def get_home():
    global root
    root.destroy()
    execfile ('MainPage.py',globals())

