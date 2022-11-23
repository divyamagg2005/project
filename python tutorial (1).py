'''doubts
quiz
attractive'''
import tkinter as tk
import csv
import webbrowser
import json
#def quiz():
    
def notes(b):
    webbrowser.open_new(b)
def youtube(a):
    webbrowser.open_new(a)
def stacks():#class 12 chapter
    global stacks1
    a = "https://www.youtube.com/watch?v=zwb3GmNAtFk"
    b = "https://www.geeksforgeeks.org/stack-in-python/#:~:text=A%20stack%20is%20a%20linear,often%20called%20push%20and%20pop."
    stacks1 = tk.Tk()
    stacks1.geometry('1100x1000')
    stacks1.config(bg='white')
    stacks1.title('advanced level')
    stacks1.resizable(True,True)
    heading = tk.Label(stacks1,text='stacks',font='pacifico 56 underline',fg='black').place(x=450, y=100,)
    button1 = tk.Button(stacks1,text = 'video lecture', font='helvectica 20',fg='white',bg='#361869',command=lambda:youtube(a)).place(x=150, y=450, width=200, height=70)#video lecture
    button2 = tk.Button(stacks1,text='quiz',fg='white',bg='#361869',font='helvectica 20',command=lambda:quiz()).place(x=350, y=450, width=200, height=70)#quiz to be build
    button3 = tk.Button(stacks1,text='notes',fg='white',bg='#361869',font='helvectica 20',command=lambda:notes(b)).place(x=550, y=450, width=200, height=70)#notes
    button4 = tk.Button(stacks1,text='back',fg='white',bg='#361869',font='helvectica 20',command=lambda:class12()).place(x=750, y=450, width=200, height=70)#back
    class2.destroy()
    stacks1.mainloop()    
def binaryfile():#class 12 chapter
    global binaryfile1
    a = "https://www.youtube.com/watch?v=ufzea-kjA6M"
    b = "https://www.tutorialaicsip.com/cs-xii/binary-files-in-python-class-12/"
    binaryfile1 = tk.Tk()
    binaryfile1.geometry('1100x1000')
    binaryfile1.config(bg='white')
    binaryfile1.title('advanced level')
    binaryfile1.resizable(True,True)
    heading = tk.Label(binaryfile1,text='binary file',font='pacifico 56 underline',fg='black').place(x=350, y=100,)
    button1 = tk.Button(binaryfile1,text = 'video lecture', font='helvectica 20',fg='white',bg='#361869',command=lambda:youtube(a)).place(x=150, y=450, width=200, height=70)#video lecture
    button2 = tk.Button(binaryfile1,text='quiz',fg='white',bg='#361869',font='helvectica 20',command=lambda:quiz()).place(x=350, y=450, width=200, height=70)#quiz to be build
    button3 = tk.Button(binaryfile1,text='notes',fg='white',bg='#361869',font='helvectica 20',command=lambda:notes(b)).place(x=550, y=450, width=200, height=70)#notes
    button4 = tk.Button(binaryfile1,text='back',fg='white',bg='#361869',font='helvectica 20',command=lambda:class12()).place(x=750, y=450, width=200, height=70)#back
    class2.destroy()
    binaryfile1.mainloop()
def pl(): #chapter class11
    global p11
    a = "https://www.bing.com/videos/search?q=python+looping+&&view=detail&mid=C28B8FC9447E7DCA071CC28B8FC9447E7DCA071C&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dpython%2520looping%2520%26qs%3Dn%26form%3DQBVR%26%3D%2525eManage%2520Your%2520Search%2520History%2525E%26sp%3D-1%26pq%3Dpython%2520looping%2520%26sc%3D10-15%26sk%3D%26cvid%3D01CDBEAA3E9249F2B9D03165B61D1C0B%26ghsh%3D0%26ghacc%3D0%26ghpl%3D"
    b = "https://www.geeksforgeeks.org/loops-in-python/"
    p11 = tk.Tk()
    p11.geometry('1100x1000')
    p11.config(bg='white')
    p11.title('beginners level')
    p11.resizable(True,True)
    heading = tk.Label(p11,text='python looping',font='pacifico 56 underline',fg='black').place(x=300, y=100,)
    button1 = tk.Button(p11,text = 'video lecture', font='helvectica 20',fg='white',bg='#361869',command=lambda:youtube(a)).place(x=150, y=450, width=200, height=70)#video lecture
    button2 = tk.Button(p11,text='quiz',fg='white',bg='#361869',font='helvectica 20',command=lambda:quiz()).place(x=350, y=450, width=200, height=70)#quiz to be build
    button3 = tk.Button(p11,text='notes',fg='white',bg='#361869',font='helvectica 20',command=lambda:notes(b)).place(x=550, y=450, width=200, height=70)#notes
    button4 = tk.Button(p11,text='back',fg='white',bg='#361869',font='helvectica 20',command=lambda:class11()).place(x=750, y=450, width=200, height=70)#back
    class1.destroy()
    p11.mainloop()
def datatype(): #chapter clas11
    global datatype1
    a = "https://www.bing.com/videos/search?q=python+all+data+types+videos&&view=detail&mid=EB509457B7CA764B9932EB509457B7CA764B9932&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dpython%2520all%2520data%2520types%2520videos%26qs%3Dn%26form%3DQBVR%26%3D%2525eManage%2520Your%2520Search%2520History%2525E%26sp%3D-1%26pq%3Dpython%2520all%2520data%2520types%2520video%26sc%3D0-27%26sk%3D%26cvid%3D184C657ED6064797AE835FBACF5EB1D8%26ghsh%3D0%26ghacc%3D0%26ghpl%3D"
    b = "https://mycstutorial.in/python-data-types/#:~:text=Python%20has%20following%20built-in%20data%20types%3A%201%20Numbers,%28String%2C%20List%2C%20and%20Tuples%29%20and%204%20Mapping%20%28Dictionary%29"
    datatype1 = tk.Tk()
    datatype1.geometry('1100x1000')
    datatype1.config(bg='white')
    datatype1.title('beginners level')
    datatype1.resizable(True,True)
    heading = tk.Label(datatype1,text='data types',font='pacifico 56 underline',fg='black').place(x=350, y=100,)
    button1 = tk.Button(datatype1,text = 'video lecture', font='helvectica 20',fg='white',bg='#361869',command=lambda:youtube(a)).place(x=150, y=450, width=200, height=70)#video lecture
    button2 = tk.Button(datatype1,text='quiz',fg='white',bg='#361869',font='helvectica 20',command=lambda:quiz()).place(x=350, y=450, width=200, height=70)#quiz to be build
    button3 = tk.Button(datatype1,text='notes',fg='white',bg='#361869',font='helvectica 20',command=lambda:notes(b)).place(x=550, y=450, width=200, height=70)#notes
    button4 = tk.Button(datatype1,text='back',fg='white',bg='#361869',font='helvectica 20',command=lambda:class11()).place(x=750, y=450, width=200, height=70)#back
    class1.destroy()
    datatype1.mainloop()    
def class12():
    global class2
    class2 = tk.Tk()
    class2.geometry('1100x1000')
    class2.config(bg='white')
    class2.title('advanced level')
    class2.resizable(True,True)

    heading = tk.Label(class2,text='welcome this package contains all python advance teaching',font='pacifico 30 underline',fg='black').place(x=25, y=100,)

    button1 = tk.Button(class2,text = 'stacks', font='helvectica 20',fg='white',bg='#361869',command=lambda:stacks()).place(x=150, y=450, width=200, height=70)
    button2 = tk.Button(class2,text='binary file',fg='white',bg='#361869',font='helvectica 20',command=lambda:binaryfile()).place(x=450, y=450, width=200, height=70)

    button4 = tk.Button(class2,text='back',fg='white',bg='#361869',font='helvectica 20',command=lambda:homepage()).place(x=750, y=450, width=200, height=70)#back
    home.destroy()
    class2.mainloop()
def class11():
    global class1
    class1 = tk.Tk()
    class1.geometry('1100x1000')
    class1.config(bg='white')
    class1.title('beginners level')
    class1.resizable(True,True)

    heading = tk.Label(class1,text='welcome this package contains all python basics teaching',font='pacifico 30 underline',fg='black').place(x=50, y=100,)

    button1 = tk.Button(class1,text = 'python looping', font='helvectica 20',fg='white',bg='#361869',command=lambda:pl()).place(x=200, y=450, width=200, height=70)
    button2 = tk.Button(class1,text='data types',fg='white',bg='#361869',font='helvectica 20',command=lambda:datatype()).place(x=450, y=450, width=200, height=70)
    button4 = tk.Button(class1,text='back',fg='white',bg='#361869',font='helvectica 20',command=lambda:homepage()).place(x=700, y=450, width=200, height=70)#back
    home.destroy()
    class1.mainloop()
  
def homepage():
    global home
    home = tk.Tk()
    home.geometry('1100x1000')
    bg = tk.PhotoImage(file = "chris-ried-ieic5Tq8YMk-unsplash.png")
    label1 = tk.Label( home, image = bg)
    label1.place(x = 0, y = 0)
    home.title('python tutorial')
    home.resizable(True,True)

    heading = tk.Label(home,text='welcome to python tutorial',font='pacifico 56 underline',fg='black').place(x=100, y=100,)
    
    button1 = tk.Button(home,text = 'beginnners level', font='helvectica 20',fg='white',bg='#361869',command=lambda:class11()).place(x=250, y=450, width=200, height=70)
    
    or_label = tk.Label(home,text = 'OR',font='Arial 15 bold',bg='black',fg='white').place(x=450, y=450, width=100, height=70)
    
    button2 = tk.Button(home,text='advanced level',fg='white',bg='#361869',font='helvectica 20',command=lambda:class12()).place(x=550, y=450, width=200, height=70)
    
    home.mainloop()
    
homepage()
