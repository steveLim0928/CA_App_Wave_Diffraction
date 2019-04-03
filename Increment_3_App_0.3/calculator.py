import SS_Animation
global n
n = 1
def answer():
    A = float(gap_slider.get())
    D = float(screen_offset_slider.get())
    LAMBDA = float(colour_choice.get())
    Answer = (((math.asin(float(((n*LAMBDA)/A))))))
    Answer_1 = (((math.asin(float(((n+(0.5)*LAMBDA)/A))))))
    tkMessageBox.showinfo('Answer','Bright Fringes:',Answer,\n'Dark Fringes:',Answer_1)
    

def answer_1():
    A = float(gap_slider.get())
    D = float(screen_offset_slider.get())
    LAMBDA = float(colour_choice.get())
    Answer_2 = ((((math.asin(float(((n*LAMBDA)/A))))))*D)
    tkMessageBox.showinfo('Answer','Theta = ',Answer_2)

###############################################################
def answer_2():
    A = float(gap_slider.get())
    D = float(screen_offset_slider.get())
    LAMBDA = float(colour_choice.get())
    Answer_2 = (((math.asin(float(((n+(0.5)*LAMBDA)/A))))))
    Answer_3 = (((math.asin(float(((n*LAMBDA)/A))))))
    tkMessageBox.showinfo('Answer','Bright Fringes:',Answer_2,\n\
                          'Dark Fringes:',Answer_3)

def answer_4():
    A = float(gap_slider.get())
    D = float(screen_offset_slider.get())
    LAMBDA = float(colour_choice.get())
    Answer_4 = ((((math.asin(float(((n*LAMBDA)/A))))))*D)
    tkMessageBox.showinfo('Answer','Theta = ',Answer_4)
    
    
