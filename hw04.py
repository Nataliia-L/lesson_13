import string
from collections import Counter

text = input('Please, enter some text: ')
text = ''.join(text.split())
new_text = ''
for i in text:
    while 'a'<= i <='z' or 'A'<= i <='Z':
        new_text += i
        break


print(dict(Counter(new_text.lower())))
