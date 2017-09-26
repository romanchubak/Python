import random
x = 0
y = 0
row = ""
while(y<10):
    if random.random() < 0.5:
        row+="/" 
        x+=1
    else:
        row+="\\"
        x+=1
    if x > 10:
        print(row)
        y += 1
        x = 0
        row = ""