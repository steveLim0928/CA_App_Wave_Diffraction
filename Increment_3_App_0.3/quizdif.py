import Tkinter as tk, ttk


root = tk.Tk()
root.geometry('510x400')
main_frame = ttk.Frame(root)
main_frame.grid(row = 0 , column = 0, sticky = "news")

class Quiz(object):
        def __init__(self, root, t, questions, correctAnswers, responses):
                self.root = root
                self.time = time = t
                self.answers = {}
                self.correctAnswers = correctAnswers
                self.questions = questions
                self.responses = responses
                
                timerValue = ttk.Label(main_frame, text = "{}:{:02d}".format(time // 60, time % 60), anchor = "e")
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
                self.questionHeader = questionHeader = ttk.Label(main_frame, text = "Question {}".format(questionNumber), font = ("Arial", 40), anchor = "center")
                questionHeader.grid(row = 1, column = 0, sticky = "nsew")

                self.question = question = ttk.Label(main_frame, text = questions[questionNumber - 1], anchor = "center")
                question.grid(row = 2, column = 0, sticky = "nsew")

                responseFrame = ttk.Frame(main_frame)
                responseFrame.grid(row = 3, column = 0, sticky = "nsew")

                self.answer = answer = tk.StringVar()
                self.responseButtons = []

                

                for index, text in enumerate(self.responses[self.questionNumber]):
                        def nextQuestion():
                                self.answers[self.questionNumber] = int(float(answer.get()))
                                if self.questionNumber < len(self.questions):
                                        self.questionNumber += 1
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
                        
                timerrun = False
                main_frame.destroy()
                data = "Results:\nNumber or questions correct:"+str(amount)+"\Questions you got wrong:"+str(wrong)
                resultlabel = tk.Label(root,text = data,height = 10,width = 60)
                resultlabel.grid(row=0, column=0, sticky='news')
                home= tk.Button(root,text = 'Home',command = home).grid(row = 1)

              
                
                
##              self.root.quit()

Q1 =  'At what angle is the first minimum for 550nm light falling on a single slit of width 1.00m?'
Q1_ans = ['30.0','33.4','35.7','45.3']
Q2 = 'Calculate angle(SS)...'
Q2_ans = ['1','2','3','4']
Q3 = 'Define (SS)...'
Q3_ans =['A','B','C','D']
Q4 = 'Calculate(SS)...'
Q4_ans =['1','2','3','4']
Q5 = 'Explain(SS)...'
Q5_ans =['A','B','C','D']
Q6 ='Calculate(DS)...'
Q6_ans = ['1','2','3','4']
Q7 = 'Calculate(DS)...'
Q7_ans = ['1','2','3','4']
Q8 = 'Define(DS)...'
Q8_ans = ['A','B','C','D']
Q9 = 'Explain(DS)...'
Q9_ans = ['A','B','C','D']
Q10 = 'Calculate(DS)...'
Q10_ans = ['A','B','C','D']




quiz = Quiz(root, int(10* 60),
            [Q1, Q2, Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10],
            {1: 1, 2: 2, 3: 3,4:4 ,5:4, 6:4 , 7:4 ,8:4, 9:4, 10:4}, {1: Q1_ans, 2: Q2_ans, 3:Q3_ans, 4:Q4_ans,5:Q5_ans,6:Q6_ans,7:Q7_ans,8:Q9_ans,9:Q9_ans,10:Q10_ans})

root.mainloop()

