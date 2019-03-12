


from Tkinter import*
from PIL import Image,ImageTk
#import winsound

#winsound.PlaySound('Directed by Robert B. Weide.wav',winsound.SND_ASYNC|winsound.SND_LOOP)



root = Tk()
root.title("WELCOME!")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = (screen_width/2) - (700/2)
y_coord = (screen_height/2) - (750/2) - 50
#CANVAS
c= Canvas(root,width = 700 ,height = 750).place(x= x_coord, y = y_coord)

#FRAME
f1 = Frame(root, width = 700,height = 750,bg = 'skyblue').pack()
root.resizable(False , False)
root.geometry('%dx%d+%d+%d' % (700, 750, x_coord, y_coord))

def mainpage():
    global root
    root.destroy()
    execfile("MainPage.py", globals())

def helpmessage():
    
    execfile("helpmessage2.py", globals())



#IMAGE
nextb = Image.open('right-arrow.png')
nextb = nextb.resize((75,75))
nextbb = ImageTk.PhotoImage(nextb)

helpb = Image.open('information.png')
helpb = helpb.resize((70,70))
helpbb = ImageTk.PhotoImage(helpb)



#LABEL

text1 = Label(root, text = 'Welcome to this workshop!', font =('algerian',30), bg = 'skyblue')
text1.place(x = 700/2 - 280, y = 50)
text2 = Label(root, text = '''The topic that will be discussed in this workshop is \nlight diffraction!\n
We will be touching on single slit and double slit diffraction.\nHope you guys enjoy!''',font = ('algerian',15),bg = 'skyblue',justify= LEFT)
text2.place(x=700/2 -320, y = 300)
text3 = Label(root, text= 'LIGHT\nDIFFRACTION',font = ('algerian',40,'bold','underline')).place(x= 700/2-180,y=125)





#BUTTON
Button(root, image = nextbb,height=75,width=75,borderwidth = 0,bg = 'skyblue', activebackground = 'skyblue',command = mainpage).place(x= 600, y = 600)
Button(root, image=helpbb,height=75, width = 75,borderwidth = 0,bg = 'skyblue', activebackground = 'skyblue', command = helpmessage).place(x=20, y =600)

root.mainloop()
