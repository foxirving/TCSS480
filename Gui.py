'''
Created on Jan 16, 2017

@author: amy
'''

from Tkinter import *

class Window(Frame):
    
    totalNumber = 0
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text = "QUIT")
        quitButton.place(x=0,y=0)
        
       
        
        button1 = Button(self, text = "1", command=self.client_one)
        button2 = Button(self, text = "2"command=self.client_two)
        button3 = Button(self, text = "3"command=self.client_three)
        button4 = Button(self, text = "4"command=self.client_four)
        button5 = Button(self, text = "5"command=self.client_five)
        button6 = Button(self, text = "6"command=self.client_six)
        button7 = Button(self, text = "7"command=self.client_seven)
        button8 = Button(self, text = "8"command=self.client_eight)
        button9 = Button(self, text = "9"command=self.client_nine)
        button0 = Button(self, text = "0"command=self.client_zero)
        
#         button1 
        
        button1.place(x=100,y=0)
        
    def changeTotal(number):
        if Window.totalNumber == 0:
            Window.totalNumber = number;
        else:
            Window.totalNumber += number;
        
    def client_one(self):
        Window.changeTotal(1)
    def client_two(self):
        Window.changeTotal(2)        
    def client_three(self):
        Window.changeTotal(3)        
    def client_four(self):
        Window.changeTotal(4)    
    def client_five(self):
        Window.changeTotal(5)        
    def client_six(self):
        Window.changeTotal(6)
    def client_seven(self):
        Window.changeTotal(7)
    def client_eight(self):
        Window.changeTotal(8)
    def client_nine(self):
        Window.changeTotal(9)
    def client_zero(self):
        Window.changeTotal(0)
               
        
root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()