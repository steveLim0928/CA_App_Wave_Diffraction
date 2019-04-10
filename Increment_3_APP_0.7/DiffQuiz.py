import Tkinter as tk,ttk


#from PIL import Image,ImageTk

root = tk.Tk()
root.title('Quiz')
root.resizable(False , False)
#root.geometry('800x400')
style = ttk.Style()
style.configure("TRadiobutton", font=("Bahnschrift SemiBold",15),  foreground='darkblue', background = 'grey')
style.configure("TFrame", background = 'grey')
style.configure("TLabel", foreground='black',background = 'grey')

main_frame = ttk.Frame(root)
main_frame.grid(row = 0 , column = 0, sticky = "news")


#my_image1 = Image.open('PhysicsImage1.jpg')
#my_image1 = my_image1.resize((510,400),Image.ANTIALIAS)
#my_image = ImageTk.PhotoImage(my_image1)
#main_frame.create_image(0, 0, image = my_image, anchor= 'nw')


class Quiz(object):
        def __init__(self, root, t, questions, correctAnswers, responses):
                self.root = root
                self.time = time = t
                self.answers = {}
                self.correctAnswers = correctAnswers
                self.questions = questions
                self.responses = responses
                
                timerValue = ttk.Label(main_frame, text = "{}:{:02d}".format(time // 60, time % 60),font=("Bahnschrift SemiBold",20), anchor = "e")
                timerValue.grid(row = 0, column = 0, sticky = "nsew")
                
                def countdown():
                        
                        if self.time > 0:
                                root.after(1000, countdown)
                                self.time -= 1
                                timerValue["text"] = "{}:{:02d}".format((self.time + 1) // 60, (self.time + 1) % 60)
                        else:

                                
                                self.showResults()
                    

                
                        
                countdown()
                self._questionNumber = questionNumber = 1
                self.questionHeader = questionHeader = ttk.Label(main_frame, text = "Question {}".format(questionNumber), font = ("Bahnschrift SemiBold", 40,"underline"), anchor = "center")
                questionHeader.grid(row = 1, column = 0, sticky = "nsew")

                self.question = question = ttk.Label(main_frame, text = questions[questionNumber - 1],font =("Bahnschrift SemiBold",20), anchor = "center")
                question.grid(row = 2, column = 0, sticky = "nsew")

                responseFrame = ttk.Frame(main_frame)
                responseFrame.grid(row =3,column = 0,sticky = "nsew")

                self.answer = answer = tk.StringVar() 
                self.answer.set("")
                self.responseButtons = []
                
                

                for index, text in enumerate(self.responses[self.questionNumber]):
                        def nextQuestion():
                                self.answers[self.questionNumber] = int(float(answer.get()))
                                if self.questionNumber < len(self.questions):
                                        self.questionNumber += 1
                                        self.answer.set("")
                                else:
                                        
                                        self.time = 0
                                        countdown()
                                        
                                        
                                        self.showResults()
                        button = ttk.Radiobutton(responseFrame, text = text, value = index + 1, variable = answer, command = nextQuestion)
                        self.responseButtons.append(button)
                        button.pack(anchor = "w")

        @property
        def questionNumber(self):
                return self._questionNumber
        @questionNumber.setter
        def questionNumber(self, val):
                self._questionNumber = val
                self.questionHeader["text"] = "Question {}".format(self.questionNumber)
                self.question["text"] = self.questions[self.questionNumber - 1]

                for index, text in enumerate(self.responses[self.questionNumber]):
                        self.responseButtons[index].config(text = text)

        def showResults(self):
                amount = 0
                wrong = []
                for key in self.correctAnswers.keys():
                        if key in self.answers.keys():
                                if self.answers[key] == self.correctAnswers[key]:
                                        amount += 1
                                else:
                                        wrong.append(key)
                        else:
                                wrong.append(key)
                        
                        
                print amount, wrong
                def home():
                        global root
                        root.destroy()
                        execfile('MainPage.py',globals())
                def again():
                        global root
                        root.destroy()
                        execfile('INS_QUIZ.py',globals())
                        
                timerrun = False
                main_frame.destroy()
                
                dataC = "Number of questions correct:"+str(amount)+ "|10"
                dataW = "Questions you got wrong:"+str(wrong)
                resultlabel_1 = tk.Label(root,text = "Result:",font=("Bahnschrift SemiBold",25),fg='black',height = 1,width = 60,bg = 'grey')
                resultlabel_1.grid(row=0,column=0,sticky='news')
                resultlabel_2 = tk.Label(root,text = dataC,font=("Bahnschrift SemiBold",20),fg='darkblue',height = 5,width = 60,bg = 'grey')
                resultlabel_2.grid(row=1,column=0,sticky='news')
                resultlabel_3 = tk.Label(root,text = dataW,font=("Bahnschrift SemiBold",20),fg='red',height = 5,width = 60,bg = 'grey')
                resultlabel_3.grid(row=2,column=0,sticky='news')
                home= tk.Button(root,text = 'Home',font = ('Bahnschrift'),command = home).grid(row=3,sticky='e')
                quizb = tk.Button(root,text = 'Retry',font=(' Bahnschrift'),command = again).grid(row=3,sticky='w') 
                
                
              
                
                
##              self.root.quit()

Q1 =  'At what angle is the first minimum for 550nm light falling on a single slit of width 1.00m?'
Q1_ans = ['30.0','33.4','35.7','45.3']#B
Q2 = 'Fill in the blank:\nDestructive interference occurs when the crest of one wave lines up with\nthe _______ of another wave.'
Q2_ans = ['trough','crest','wavelength','amplitude'] #A
Q3 = 'In a single-slit diffraction experiment, the width of the slit through which light passes\n is reduced.\
What happens to the width of the central bright fringe?'
Q3_ans =['It stays the same','It becomes narrower','It becomes wider','Its behavior depends on the wavelength of the light']#C
Q4 = 'A single-slit diffraction pattern is formed on a distant screen. Assuming the angles\n\
involved are small, by what factor will the width of the central bright spot on the screen\n\
changes if the slit width is doubled?'#B
Q4_ans =['It will be cut to one quarter of its original size','It will be cut in half','It will double','It will become four times as large']
Q5 = 'Light from a monochromatic source  shines through a double slit onto a screen 5.00m away.\n\
The slits are 180mm apart. The dark bands on the screen are measured to be 1.70cm apart.\n\
What is the wavelength of the incident light?'
Q5_ans =['457nm','306nm','392nm','612nm']#D
Q6 ='In a double slit exxperiment, if the seperation between the two slits is 0.050mm and the\n\
distance from the slits to a screen is 2.5m, find the spacing between the first-order and\n\
second-order bright fringes when coherent light of wavelength 600nm illuminates the slits.'
Q6_ans = ['1.5cm','3.0cm','4.5cm','6.0cm']#B
Q7 = 'In a double-slit experiment, the slit seperation is 2.0 mm, and two wavelengths,\n\
750nm and 900nm,illuminate the slits simultaneously. A screen is placed 2.0 m from the slits.\n\
At what distance from the central maximum on the screen will be a bright fringe from one\n\
pattern first coincide with a bright fringe from the order?'
Q7_ans = ['1.5mm','3.0mm','4.5mm','6.0mm']#C
Q8 = 'What term describes the phenomenon as a wave spreads into the region behind an \nobtruction?'
Q8_ans = ['Superposition','Dispersion','Diffraction','Refraction']#C
Q9 = 'Light of frequency 6.00*10**14 Hz illuminates a soap film (n=1.33)having air both sides of it.\n\
When viewing the film by reflected light, what is the minimum thickness of the film that will\n\
give an interference maximum when the light is incident on it?(c = 3.00*10**8)'
Q9_ans = ['24.0nm','94.0nm','188nm','279nm']#B
Q10 = 'When monochromatic light illuminates a grating with 7000 lines per centimeter, its second\n\
order maximum is at 62.4.What is the wavelength of the light?'
Q10_ans = ['336nm','363nm','452nm','752nm']#D




quiz = Quiz(root, int(8* 60),
            [Q1,Q2,
             Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10],
            {1: 2, 2: 1, 3:3,4:2 ,5:4, 6:2 , 7:3 ,8:3, 9:2, 10:4}, {1: Q1_ans, 2: Q2_ans, 3:Q3_ans, 4:Q4_ans,5:Q5_ans,6:Q6_ans,7:Q7_ans,8:Q8_ans,9:Q9_ans,10:Q10_ans})

root.mainloop()
