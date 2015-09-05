import string

f = open('./text files/shake_view.txt', 'r')
text = f.read()
f.close()
n = len(text)

#print '  ' in text

print len(text)

text = text.lower()

for i in range(256):
    if chr(i) == '\'':
        text = text.replace(chr(i),'')
    elif chr(i) != ' ' and chr(i) != '\n' and (i < 97 or i > 122):
        text = text.replace(chr(i),' ')

text = text.replace('\n', ' ')

for i in range(100):
    text = text.replace('  ', ' ')

f = open('./text files/shake_nolines.txt', 'w')
f.write(text)
f.close()
