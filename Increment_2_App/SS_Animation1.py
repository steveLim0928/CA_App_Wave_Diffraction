import Tkinter
import tkMessageBox
from PIL import ImageTk, Image
import Single_slit_red1 as SSr
import Single_slit_orange1 as SSo

import Calculation


root = Tkinter.Tk()
root.title('Single Slit Animation')
root.geometry("950x450")
root.resizable(False, False)

# Values --------------------------------------------------------------------
global x
x = 50

global status
status = True

global reset
reset = False

# To allow the animation z value be resetted
global reset_z
reset_z = False

# ---------------------------------------------------------------------------

def start_animation():
    global reset, reset_z, num, gap, x, offset
    
    v_value()
    
    reset = True
    
    start_button.config(state = 'disable')
    pause_button.config(state = 'normal')
    reset_button.config(state = 'normal')
    result_button.config(state = 'normal')
    gap_slider.config(state = 'disable')
    screen_offset_slider.config(state = 'disable')
    
    
    gap_calculation_value()
    offset_calculation_value()
    

    gap = gap * 100
    

    offset = ((offset * 100) - 100) * 2
    
    for i in range(1, 8):
        colour_choice[i].config(state = 'disable')
    
    while reset == True:
        if reset == True and status == True:
            if num == 1:
                canvas2.delete('all')
                # barrier(canvas, gap_size)
                SSr.barrier(canvas2, gap)
                # screen(canvas)
                SSr.screen(canvas2, offset)
                # screen2(canvas, colour)
                SSr.screen2(canvas2, 'red')
                if x == 50:
                    x = 70
                if x <= 250:
                    # red_scene_1(canvas, wavelength, colour, x)
                    SSr.red_scene_1(canvas2, 60, 'red', x)
                    
                    canvas2.create_text(102, 75, text = '665nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(71, 80, 71, 90, fill = 'black')
                    canvas2.create_line(131, 80, 131, 90, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(71, 85, 131, 85, fill = 'black')
                    #Arrow
                    canvas2.create_line(71, 85, 78, 88, fill = 'black')
                    canvas2.create_line(71, 85, 78, 82, fill = 'black')
                    canvas2.create_line(124, 88, 131, 85, fill = 'black')
                    canvas2.create_line(124, 82, 131, 85, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    # red_scene_2(canvas, colour, gap_size, a)
                    SSr.red_scene_2(canvas2, 'red', gap, reset_z, offset)
                    
                    canvas2.create_text(102, 75, text = '665nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(71, 80, 71, 90, fill = 'black')
                    canvas2.create_line(131, 80, 131, 90, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(71, 85, 131, 85, fill = 'black')
                    #Arrow
                    canvas2.create_line(71, 85, 78, 88, fill = 'black')
                    canvas2.create_line(71, 85, 78, 82, fill = 'black')
                    canvas2.create_line(124, 88, 131, 85, fill = 'black')
                    canvas2.create_line(124, 82, 131, 85, fill = 'black')
                    
                    
                    reset_z = False
                    
                # Window ---------------------------------------------------------
                root.after(7)
                
                
                canvas2.update()

            elif num == 2:
                canvas2.delete('all')
                # barrier(canvas, gap_size)
                SSo.barrier(canvas2, gap)
                # screen(canvas)
                SSo.screen(canvas2, offset)
                # screen2(canvas, colour)
                SSo.screen2(canvas2, 'orange')

                if x <= 250:
                    # red_scene_1(canvas, wavelength, colour, x)
                    SSo.orange_scene_1(canvas2, 60, 'orange', x)
                    
                    canvas2.create_text(62, 75, text = '630nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(31, 80, 31, 90, fill = 'black')
                    canvas2.create_line(91, 80, 91, 90, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(31, 85, 91, 85, fill = 'black')
                    #Arrow
                    canvas2.create_line(31, 85, 38, 88, fill = 'black')
                    canvas2.create_line(31, 85, 38, 82, fill = 'black')
                    canvas2.create_line(84, 88, 91, 85, fill = 'black')
                    canvas2.create_line(84, 82, 91, 85, fill = 'black')
                    
                    x+= 1
                elif x > 250:
                    # red_scene_2(canvas, colour, gap_size, a)
                    SSo.orange_scene_2(canvas2, 'orange', gap, reset_z, offset)
                    
                    canvas2.create_text(62, 75, text = '630nm', fill = 'black')
                    # Vertical lines
                    canvas2.create_line(31, 80, 31, 90, fill = 'black')
                    canvas2.create_line(91, 80, 91, 90, fill = 'black')
                    
                    # Horizontal Line
                    canvas2.create_line(31, 85, 91, 85, fill = 'black')
                    #Arrow
                    canvas2.create_line(31, 85, 38, 88, fill = 'black')
                    canvas2.create_line(31, 85, 38, 82, fill = 'black')
                    canvas2.create_line(84, 88, 91, 85, fill = 'black')
                    canvas2.create_line(84, 82, 91, 85, fill = 'black')
                    reset_z = False
                
                # Window --------------------------------------------------------
                root.after(7)
                canvas2.update()
            else:
                reset_animation()
                return tkMessageBox.showinfo('Colour Error', 'Please choose a colour')
            
        else:
            break

def pause_animation():
    global status

    if status:
            status = False
            pause_button.config(text = "Resume" , bg = "lime", \
                                state = 'normal', fg = "black")
        
    else:
        status = True
        pause_button.config(text = "Pause" , bg = "yellow", \
                                state = 'normal', fg = "black")

        # continue the animation
        start_animation()
        

def reset_animation():
    global reset, status, x, reset_z

    status = True

    reset = False

    canvas2.delete('all')

    x = 50

    reset_z = True
    
    v.set(1)
    
    for i in range(1, 8):
        colour_choice[i].config(state = 'normal')

    SSr.barrier(canvas2, gap)
    SSr.screen(canvas2, offset)
    SSr.screen2(canvas2, 'red')

    start_button.config(state = 'normal', fg = 'black', bg = 'lime')
    pause_button.config(text = 'Pause', state = 'disable', bg = 'yellow')
    reset_button.config(state = 'disable')
    result_button.config(state = 'disable')
    gap_slider.config(state = 'normal')
    screen_offset_slider.config(state = 'normal')

    
def offset_value(x):

    global offset, gap
    
    gap_calculation_value()
    gap = gap * 100
    offset_calculation_value()
    offset = ((offset * 100) - 100) * 2
    animation_base()

def gap_value(x):
    global gap, reset, status, offset
    gap_calculation_value()
    gap = gap * 100
    offset_calculation_value()
    offset = ((offset * 100) - 100) * 2
    if reset == True and status == True:
        start_animation()
        
    else:    
        animation_base()

def gap_calculation_value():
    global gap, calculation_gap
    calculation_gap = gap_slider.get()
    gap = gap_slider.get()
    
    return gap, calculation_gap


def offset_calculation_value():
    global offset, calculation_offset
    calculation_offset = screen_offset_slider.get()
    offset = screen_offset_slider.get()
    
    return offset, calculation_offset
    
def get_result():
    global calculation_gap, calculation_offset, wavelength, root
    root.destroy()
    Calculation.answer(calculation_gap, calculation_offset, wavelength)
    
    
def get_back():
    global root
    root.destroy()
    execfile ('Theory.py',globals())
    
# Frames and canvas----------------------------------------------------------------------

# Frame that contain animation
upper_frame = Tkinter.Frame(root, width = 950, height = 450, bg = 'grey')
upper_frame.place(x = 0, y = 0)

image = Image.open('animation_background4.jpg')
image = image.resize((950, 450), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

photo2 = Tkinter.Label(upper_frame, image = photo)
photo2.place(x = 0, y = 0)

# Main animation canvas
canvas2 = Tkinter.Canvas(upper_frame, width = 650, height = 350, bg = 'light grey', 
                         highlightbackground = 'black')
canvas2.place(x = 25, y = 50)

# Option canvas
option_canvas = Tkinter.Canvas(upper_frame, width = 230, height = 380, bg = 'sky blue', highlightbackground = 'black')
option_canvas.place(x = 710, y = 20)

# ------------------------------------------------------------------------------------
# Colour selection radio button settings.

MODES = [
        ('Red', "Red\n (665nm)", 1, 665),
        ('Dark Orange', "Orange\n (630nm)", 2, 630),
        ('Yellow', "Yellow\n (600nm)", 3, 600),
        ('teal', "Green\n (550nm)", 4, 550),
        ('Blue', "Blue\n (470nm)", 5, 470),
        ('Indigo', "Indigo\n (425nm)", 6, 425),
        ('Violet', "Violet\n (400nm)", 7, 400)
    ]

v = Tkinter.IntVar()
v.set(0) # initialize

colour_choice = dict()

for colour, text, mode, wavelength in MODES:
     
     colour_choice[mode] = Tkinter.Radiobutton(upper_frame, text=text, variable=v, state = 'normal', 
                                         value=mode, fg = colour, bg = 'sky blue', activebackground = colour, 
                                         activeforeground = colour, selectcolor = 'light grey')
     if mode < 5:
         mode = mode - 1
         colour_choice[mode + 1].place(x = 740, y = 200 + (mode * 35))


     else:
         mode = mode - 5
         colour_choice[mode + 5].place(x = 829, y = 218 + (mode * 35))

def v_value():
     global v
     global num, wavelength
     a = MODES[v.get() - 1]

     wavelength = a[3]
     num = a[2]

# adjusted so that when slider moves, animation changes
def animation_base():
    global offset, gap
    canvas2.delete('all')
    
    SSr.barrier(canvas2, gap)
    SSr.screen(canvas2, offset)
    SSr.screen2(canvas2, 'red')
     
# Buttons -------------------------------------------------------------------------------------

   
# Start button
start_button = Tkinter.Button(upper_frame, text = 'Start', command = start_animation, 
                              state = 'normal', pady = 2, padx = 5, bd = 3, bg = 'lime')
start_button.place(x = 730, y = 360)

# Pause button
pause_button = Tkinter.Button(upper_frame, text = 'Pause', command = pause_animation, 
                              state = 'disable', pady = 2, padx = 5, bd = 3, bg = 'yellow')
pause_button.place(x = 790, y = 360)

# Reset button
reset_button = Tkinter.Button(upper_frame, text = 'Reset', command = reset_animation, 
                              state = 'disable', pady = 2, padx = 5, bd = 3, bg = 'red', fg = 'white')
reset_button.place(x = 860, y = 360)

# To go to graph page
result_button = Tkinter.Button(upper_frame, text = 'Results', command = get_result, 
                              state = 'disable', pady = 2, padx = 5, bd = 3)
result_button.place(x = 870, y = 415)

back_button = Tkinter.Button(upper_frame, text = 'Back', command = get_back,
                             state = 'normal', pady = 2, padx = 5, bd = 3)
back_button.place(x = 820, y = 415)


# Gap size slider and label
gap_label = Tkinter.Label(upper_frame, text = 'Gap size (mm)', bg = 'sky blue')
gap_label.place(x = 770, y = 30)
gap_slider = Tkinter.Scale(upper_frame, from_ = 0.10, to = 0.50, resolution = 0.01, 
                           bg = 'sky blue', command = gap_value, state = 'normal', 
                           orient = 'horizontal', length = 150)
gap_slider.place(x = 750, y = 50)

# screen distance slider and label
offset_label = Tkinter.Label(upper_frame, text = 'Distance from barrier\n to screen (m)',
                             bg = 'sky blue')
offset_label.place(x = 770, y = 110)
screen_offset_slider = Tkinter.Scale(upper_frame, from_ = 1.00, to = 1.20, 
                                     resolution = 0.01, bg = 'sky blue', 
                                     command = offset_value, state = 'normal', 
                                     orient = 'horizontal', length = 150)
screen_offset_slider.place(x = 750, y = 150)

# -------------------------------------------------------------------------

# main display for animation (won't be empty initially)
SSr.barrier(canvas2, gap_slider.get() * 100)
SSr.screen(canvas2, ((screen_offset_slider.get() * 100)- 100) * 2)
SSr.screen2(canvas2, 'red')

root.mainloop()

