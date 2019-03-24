from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
get_ipython().run_line_magic('matplotlib', 'qt')

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

constQ=30
datne="jautajumi_2017b.csv"
questions = pd.read_csv(datne, delimiter=';', encoding = 'utf-8')
root=Tk()
cities= ['DAU', 'JEK', 'JEL', 'JUR', 'LIE', 'REZ', 'VAL', 'VEN']
cities2=cities
cities3=[]


root.title("OpenDataUser")


var=[ IntVar() for j in range(constQ) ]


def data():
    for i, row in questions.iterrows():
       Checkbutton(frame,text=str(questions["Jautajums"][i]), variable=var[i]).grid(row=i,column=0)
       
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=950,height=200)


sizex = 1000
sizey = 600
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(root,relief=GROOVE,width=50,height=100,bd=3)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data()

b=0
lencities=len(cities)
cvar=[ IntVar() for j in range(lencities) ]

for k in range (lencities):
    Checkbutton(root, text=cities[k], variable = cvar[k]).place(x=20+75*b, y=230)
    b=b+1
    

######################################################
def execute66(): #on Button click - atlasa derīgos jautājumus
    for j in range(lencities):
        if (cvar[j].get()==1):
            cities3.append(cities[j])
    #print(cities3)        
    boot=Tk()
    boot.title("Winow Extra")
    Label(boot, text="1 = Ļoti apmierināts").pack()
    Label(boot, text="2 = Drīzāk apmierināts").pack()
    Label(boot, text="3 = Drīzāk neapmierināts").pack()
    Label(boot, text="4 = Ļoti neapmierināts").pack()
    Label(boot, text="9 = Neattiecas / nav viedokļa").pack()
    statt="individualie_dati.csv"
    stats = pd.read_csv(statt, encoding = 'utf-8')
    #print(stats.iloc[:, 5])
    
    for i in range(constQ):
        if (var[i].get()==1):
            plt.clf
            qname=questions.iloc[i,0]
            br = (stats.loc[:, [qname, 'pilseta']])
            #plt.figure()
            #plt.new_figure_manager(2)
            for city in (cities3):
                plt.clf
                filtrs_pils = (br["pilseta"] == str(city))
                cr=()
                cr = ( br.loc[filtrs_pils][:] )  # only what we need
                #print(questions.iloc[i,1])
                values=()
                counts=()
                objects=()
                
                
                values = cr[qname].value_counts().sort_index().keys().tolist()
                counts = cr[qname].value_counts().sort_index().tolist()
                #print(values)
                #print(counts)

                objects = (values)
                y_pos = np.arange(len(objects))
                performance = counts
                
                plt.bar(y_pos, performance, alpha=0.5)
                plt.xticks(y_pos, objects)
                plt.ylabel('Skaits')
                plt.title(questions.iloc[i,1] + " " + str(city))
               # plt.figure(i)

                plt.show()
                
                #plt.savefig('foob.png')
                #iccon = PhotoImage(file = "foob.png")
                #label = Label(boot, image = iccon)
                #label.pack()
                
                
                
                
                
            Label(boot, text=questions["Jautajums"][i]).pack()
           



            Label(boot, text="--------------------------------------").pack()       
    plt.clf

    boot.mainloop()
     
#########################################################
btn1=Button(root, text="GO",bg="green",fg="black" , command=execute66).place(height=40, width=65, x=20, y=270)
plt.clf
root.mainloop()