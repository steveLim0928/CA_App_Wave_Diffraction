
global n
n = 1

import math


def answer(gap, offset, wavelength, canvas):

    
    global n, A, D, LAMBDA
    A = float(gap/1000)
    D = float(offset)
    LAMBDA = float(wavelength)
    
    
    
    theta_value = (((math.asin(float((((n*LAMBDA)/A)/1000000000))))))
    bright_value = ((((math.asin(float(((n*LAMBDA)/A)/1000000000)))))*D)
    dark_value = ((((math.asin(float(((n+(0.5)*LAMBDA)/A)/1000000000)*D)))))
    
    bright_value = bright_value * 1000
    dark_value = dark_value * 1000
    
    theta_value = str(round(theta_value, 4))
    bright_value = str(round(bright_value, 2))  
    dark_value = str(round(dark_value, 2))
    
    n1 = str(n)
    
    canvas.create_text(130, 20, text = ('Value of n = ' + n1), fill = 'red')
    
    canvas.create_text(68, 40, text = ('Theta = ' + theta_value + ' rad'), fill = 'black')
    
    canvas.create_text(145, 60, text = ('Distance between bright fringes = ' + bright_value + ' mm'), fill = 'black')
    
    canvas.create_text(140, 80, text = ('Distance between dark fringes = ' + dark_value + ' mm'), fill = 'black')
    

    


