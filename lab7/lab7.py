from tkinter import *
from collections import Counter
def func(var):
    word = var.get()
    count_A = 0
    count_B = 0

    for (key, value) in Counter(word).items():
        if value.isalpha():
            count_A+=1
        else :
            count_B+=1
    L1['text'] = "Count alpha : " + str(count_A)  + "count not alpha: " + str(count_B)


top = Tk()
L1 = Label(top, text="Count: 0")
L1.pack(side=TOP)


sv = StringVar()
sv.trace('w', lambda nm, idx, mode, var=sv: func(var))

input = Entry(top, bd=5, textvariable=sv)
input.pack(side=LEFT)

bVar_1 = BooleanVar()
bVar_1.trace('w', lambda nm, idx, mode, var=sv: func(var))

bVar_2 = BooleanVar()
bVar_2.trace('w', lambda nm, idx, mode, var=sv: func(var))


radio1 = Checkbutton(top, text="2", variable=bVar_1)
radio2 = Checkbutton(top, text="+", variable=bVar_2)
radio1.pack(side=BOTTOM)
radio2.pack(side=BOTTOM)
top.mainloop()
