from tkinter import *

def isVowel(char):
    return char.lower() in 'aeiou'

def func(var):
	word = var.get()
	count_A = 0
	count_B = 0
	for ch in word:
		if isVowel(ch) and ch.isalpha():
			count_A+=1
		else :
			count_B+=1
	output = "Count: "
	count = 0
	if vowelON.get():
		 count += count_A
	if consonantON.get():
		count += count_B
	L1['text'] = output + str(count)


top = Tk()
L1 = Label(top, text="Count: 0")
L1.pack(side=TOP)


word = StringVar()
word.trace('w', lambda nm, idx, mode, var=word: func(var))

input = Entry(top, bd=5, textvariable=word)
input.pack(side=LEFT)

vowelON = BooleanVar()
vowelON.trace('w', lambda nm, idx, mode, var=word: func(var))

consonantON = BooleanVar()
consonantON.trace('w', lambda nm, idx, mode, var=word: func(var))


radio1 = Checkbutton(top, text="vowel", variable=vowelON)
radio2 = Checkbutton(top, text="consonant", variable=consonantON)
radio1.pack(side=BOTTOM)
radio2.pack(side=BOTTOM)
top.mainloop()
