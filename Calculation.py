
global n
n = 1
import tkMessageBox
import math
from math import *


def answer(gap, offset, wavelength):
    global Answer, Answer_1, Answer_2, answ
    A = float(gap/1000)
    D = float(offset)
    LAMBDA = float(wavelength)
    print A
    print D
    print LAMBDA
    Answer = (((math.asin(float((((n*LAMBDA)/A)/1000000000))))))
    Answer_1 = ((((math.asin(float(((n*LAMBDA)/A)/1000000000)))))*D)
    Answer_2 = ((((math.asin(float(((n+(0.5)*LAMBDA)/A)/1000000000)*D)))))
   
    answ = ('Theta:' , Answer , 'Bright Fringes: ', Answer_1, 'Dark Fringes: ', Answer_2)
    return tkMessageBox.showinfo('Answer',answ)


