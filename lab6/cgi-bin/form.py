import cgi
from collections import Counter

form = cgi.FieldStorage()
word = form.getfirst("word", "Missing a argument.")
count = 0;
for (key, value) in Counter(word).items():
    if value.isalpha():
        count+=1
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Result</title>
        </head>
        <body>""")
print(word)
#print("<br>" + str(count) + " - alpha leters")
print("""</body>
        </html>""")
