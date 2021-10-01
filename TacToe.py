from tkinter import *
import tkinter as tk

global p
p ='O'
global P
P = ["_","_","_","_","_","_","_","_","_"]

def przelicz(i,b,l):
    global p
    global P
    if P[i] == "_":
        l.config(text = 'teraz gracz: '+p)  
        if p != 'O':
            p = 'O'
        else:
            p = 'X'
        P[i] = p
        print(str(i)+" "+p+" ")
        b.config(text = p)
    wygrana(l)    
    
def wygrana(l):
    global P
    bo = False
    if P[0]==P[4] and P[0]==P[8]: 
        bo = True
    elif P[2]==P[4] and P[2]==P[6]:
        bo = True
    elif P[0]==P[3] and P[0]==P[6]: 
        bo = True
    elif P[1]==P[4] and P[1]==P[7]:
        bo = True
    elif P[2]==P[5] and P[2]==P[8]:
        bo = True
    elif P[0]==P[1] and P[0]==P[2]:
        bo = True
    elif P[3]==P[4] and P[3]==P[5]:
        bo = True
    elif P[6]==P[7] and P[6]==P[8]:
        bo = True    
    if  bo == True :
        l.config(text = "wygrał gracz "+p)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('kółko i krzyżyk')

    label= Label(root, text = "zaczyna gracz: O")
    label.pack(side = TOP, fill = 'both')

    frame1 = Frame(root)
    frame1.pack(fill = 'both', expand = 'true', )      

    b1 = tk.Button(frame1, text = "_", command =  lambda: przelicz(0,b1,label), height = 6, width = 6)
    b1.grid(column = 1, row = 1)

    b2 = tk.Button(frame1, text = "_", command =  lambda: przelicz(1,b2,label), height = 6, width = 6)
    b2.grid(column = 2, row = 1)

    b3 = tk.Button(frame1, text = "_", command =  lambda: przelicz(2,b3,label), height = 6, width = 6)
    b3.grid(column = 3, row = 1)

    b4 = tk.Button(frame1, text = "_", command =  lambda: przelicz(3,b4,label), height = 6, width = 6)
    b4.grid(column = 1, row = 2)

    b5 = tk.Button(frame1, text = "_", command =  lambda: przelicz(4,b5,label), height = 6, width = 6)
    b5.grid(column = 2, row = 2)

    b6 = tk.Button(frame1, text = "_", command =  lambda: przelicz(5,b6,label), height = 6, width = 6)
    b6.grid(column = 3, row = 2)

    b7 = tk.Button(frame1, text = "_", command =  lambda: przelicz(6,b7,label), height = 6, width = 6)
    b7.grid(column = 1, row = 3)

    b8 = tk.Button(frame1, text = "_", command =  lambda: przelicz(7,b8,label), height = 6, width = 6)
    b8.grid(column = 2, row = 3)

    b9 = tk.Button(frame1, text = "_", command =  lambda: przelicz(8,b9,label), height = 6, width = 6)
    b9.grid(column = 3, row = 3)
        
    root.mainloop()