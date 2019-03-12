
from Tkinter import*
from PIL import Image, ImageTk


root = Tk()
root.title("Main Page")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = (screen_width/2) - (700/2)
y_coord = (screen_height/2) - (750/2) - 50

root.resizable(False , False)
#CANVAS
c= Canvas(root,width = 700 ,height = 750).place(x= x_coord, y = y_coord)
#FRAME
f1 = Frame(root, width = 700,height = 750,bg = 'skyblue').pack()
root.resizable(False , False)
root.geometry('%dx%d+%d+%d' % (700, 750, x_coord, y_coord))

def back():
    global root
    root.destroy()
    
    execfile('welcomemessage.py',globals())
def quiz_ins():
    global root
    root.destroy()
    
    execfile('INS_QUIZ.py',globals())
def helpB():
    
    execfile('helpmessage1.py',globals())
def theory():
    global root
    root.destroy()
    
    execfile('Theory.py',globals())
def theory2():
    global root
    root.destroy()

    execfile('theory2.py',globals())
text3 = Label(root, text= 'LIGHT\nDIFFRACTION',font = ('algerian',60,'bold','underline')).place(x= 700/2-250,y=125)  

#IMAGE
backb = Image.open('left-arrow.png')
backb = backb.resize((75,75))
backbb = ImageTk.PhotoImage(backb)


helpb = Image.open('information.png')
helpb = helpb.resize((70,70))
helpbb = ImageTk.PhotoImage(helpb)

#BUTTON
Button(root, image=backbb,height=75, width = 75,borderwidth=0,bg='skyblue',activebackground='skyblue',command = back).place(x=30,y=610)

Button(root, image=helpbb,height=75, width=75,borderwidth=0,bg='skyblue',activebackground='skyblue',command = helpB).place(x= 600,y=600)
Button(root, text="Quiz",font=('algerian'),height=3, width=20, command = quiz_ins).place(x= 230,y = 600)
Button(root, text="Single Slit",font=('algerian'),height=3,width=20, command = theory).place(x=230,y=400)
Button(root, text="Double Slit",font=('algerian'),height=3,width=20, command = theory2).place(x=230,y=500)

root.mainloop()

