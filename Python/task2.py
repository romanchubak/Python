import re 
def task2():
    text = input("input your text: ")
    word1 = input("input word that you want to replace: ")
    word2 = input("input word that have to revlaced firt word: ")
    text = re.sub('\s'+word1+'\s?', ' ' + word2 + ' ', text).strip()
    return text