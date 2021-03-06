import Tkinter

# gap function
def barrier(canvas, gap_size):
    above_gap = 170 - gap_size
    below_gap = 170 + gap_size
    canvas.create_rectangle(250, 5, 260, above_gap, fill = 'sky blue', outline = 'black')
    canvas.create_rectangle(250, below_gap, 260, 345, fill = 'sky blue', outline = 'black')

#black screen
def screen(canvas, screen_offset):
    # Mac
#   canvas.create_rectangle(550 + screen_offset, 5, 600 +screen_offset, 345, fill = 'black', outline = 'black')
#   canvas.create_text((575 + screen_offset, 170), text = 'Screen', fill = 'white', angle = -90)
    
    # Window
    canvas.create_rectangle(550 + screen_offset, 5, 600 +screen_offset, 345, fill = 'black', outline = 'black')
    canvas.create_text((575 + screen_offset, 170), text = 'Screen', fill = 'white')

#screen where light is emitted
def screen2(canvas, colour):
    # Mac
#    canvas.create_rectangle(50, 5, 70, 345, fill = colour, outline = 'black')
#    canvas.create_text((60, 170), text = 'Light Generator', fill = 'black', angle = -90)
    
    # Window
    canvas.create_rectangle(50, 5, 70, 345, fill = colour, outline = 'black' )
    canvas.create_text((60, 170), text = 'L\nI\nG\nH\nT\n\nG\nE\nN\nE\nR\nA\nT\nO\nR', fill = 'black')

#initial value of the wave
global x
x = 70

def waves(canvas, colour, x):
    canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)

## ---------------------------------------------------------------------------

global wavelength
wavelength = 60

# when x is < 550, to create a list of waves
def red_scene_1(canvas, wavelength, colour, x):
    
    
    if x <= (70 + wavelength):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        x += 1


    elif x <= (70 + (2 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        x += 1

    elif x <= (70 + (3 * wavelength)):
        canvas.create_rectangle(x, 90, x + 1, 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - (wavelength - 1), 90, x - (wavelength - 2), 250, fill = colour, outline = colour)
        canvas.create_rectangle(x - ((2 * wavelength ) - 1), 90, x - ((2 * wavelength ) - 2), 250, fill = colour, outline = colour)
        x += 1

## -----------------------------------------------------------------------------------



# All is to set the wave value when x > 550        
global x1
x1 = 70

global x2
x2 = (71 + wavelength)

global x3
x3 = (71 + (2 * wavelength))

## ------------------------------------------------------------------------------------------------


# The diffraction waves after the slit
def diffracted_waves(canvas, colour, z, gap_size, screen_offset):
    above_gap = 170 - gap_size
    below_gap = 170 + gap_size

    canvas.create_arc(253 + z, above_gap - (z - 4) , 258 + 2 * z, below_gap + (z - 4), style = Tkinter.ARC, start = -90, extent = 180, width = 2, fill = colour, outline = colour)
    screen(canvas, screen_offset)
    
## --------------------------------------------------------------------------------------


# The parameter to create moving diffracted waves
global z1
z1 = 0

global z2
z2 = 0

global z3
z3 = 0

global z4
z4 = 0

global z5
z5 = 0

global z6
z6 = 0

global z7
z7 = 0
global z8
z8 = 0


## ----------------------------------------------------------------------------------------------------

# keep repeating, after x > 550
def red_scene_2(canvas, colour, gap_size, a, screen_offset):
    global x1
    global x2
    global x3

    global z1
    global z2
    global z3
    global z4
    global z5
    global z6
    global z7
    global z8

    if a == True:
        z1 = 0
        z2 = 0
        z3 = 0
        z4 = 0
        z5 = 0
        z6 = 0
        z7 = 0
        z8 = 0
        x1 = 70
        x2 = (71 + wavelength)
        x3 = (71 + (2 * wavelength))
    
    waves(canvas, colour, x1)
    waves(canvas, colour, x2)
    waves(canvas, colour, x3)
    

    # Start to create diffracted waves

    # if the repeated waves starts
    if x1 == 71:
        # initial z1 to 1
        z1 = 1
    # if z1 is 1
    if z1 >= 1:
        # start creating the diffracted waves
        diffracted_waves(canvas, colour, z1, gap_size, screen_offset)
        z1 += 0.5
    # out of the screen

    if z1 >= 91.5 - screen_offset + (screen_offset/3):
        # reset it back to 0 and wait to see if the wave have repeated
        z1 = 0
        z2 = 91.5 - screen_offset + (screen_offset/3)

    
    if z2 >= 91.5 - screen_offset + (screen_offset/3):
        diffracted_waves(canvas, colour, z2, gap_size, screen_offset)
        z2 += 0.5

    if z2 >= 181.5 - screen_offset + (screen_offset/3):
        z2 = 91.5 - screen_offset + (screen_offset/3)



    # gap from screen to barrier divide 2 = value for diffracted waves

    ######
    if x2 > 249:
        z3 = 1
    if z3 >= 1:
        diffracted_waves(canvas, colour, z3, gap_size, screen_offset)
        z3 += 0.5
    if z3 >= 91.5 - screen_offset + (screen_offset/3):
        z4 = 91.5 - screen_offset + (screen_offset/3)
        z3 = 0

    if z4 >= 91.5 - screen_offset + (screen_offset/3):
        diffracted_waves(canvas, colour, z4, gap_size, screen_offset)
        z4 += 0.5

    if z4 >= 181.5 - screen_offset + (screen_offset/3):
        z4 = 91.5 - screen_offset + (screen_offset/3)



    #####
        
    if x3 > 249:
        z5 = 1
    if z5 >= 1:
        diffracted_waves(canvas, colour, z5, gap_size, screen_offset)
        z5 += 0.5
    if z5 >= 91.5 - screen_offset + (screen_offset/3):
        z6 = 91.5 - screen_offset + (screen_offset/3)
        z5 = 0

    if z6 >= 91.5 - screen_offset + (screen_offset/3):
        diffracted_waves(canvas, colour, z6, gap_size, screen_offset)
        z6 += 0.5

    if z6 >= 181.5 - screen_offset + (screen_offset/3):
        z6 = 91.5 - screen_offset + (screen_offset/3)

    ######

    if x2 > 249:
        z7 = 1
    if z7 >= 1:
        diffracted_waves(canvas, colour, z7, gap_size, screen_offset)
        z7 += 0.5
    if z7 >= 91.5 - screen_offset + (screen_offset/3):
        z8 = 91.5 - screen_offset + (screen_offset/3)
        z7 = 0

    if z8 >= 91.5 - screen_offset + (screen_offset/3):
        diffracted_waves(canvas, colour, z8, gap_size, screen_offset)
        z8 += 0.5

    if z8 >= 181.5 - screen_offset + (screen_offset/3):
        z8 = 91.5 - screen_offset + (screen_offset/3)  

    ## --------------------------------------------------------------------------------------------
        
    x1 += 1
    x2 += 1
    x3 += 1

    
    if x1 > 250:
        x1 = 70
    if x2 > 250:
        x2 = 70
    if x3 > 250:
        x3 = 70
