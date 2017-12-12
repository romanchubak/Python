import cgi
def isVowel(char):
    return char.lower() in 'aeiou'

form = cgi.FieldStorage()
word = form.getfirst("word", "Missing a argument.")
count = 0;
for ch in word:
    if isVowel(ch):
        count+=1
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Result</title>
        </head>
        <body>
		word : 
		""")
print(word)
print("<br>include <br>" + str(count) + " - vowel leters")
print("""</body>
        </html>""")