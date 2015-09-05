def naivesearch(pattern, text):
	return pattern in text

infile = open('shakespeare.txt', 'r')
text = infile.read()

pattern = 'What I should do again for such a sake'
#pattern = 'adsfahjgdfg'
#print pattern in text

#count = 0
#for i in range(1):
#	if pattern in text:
#		count += 1
#print count

#count = 0
#for i in range(1):
#	if naivesearch(pattern, text):
#		count += 1
#print count

#count = 0
#for i in range(100):
#	if BMH(pattern, text):
#		count += 1
#print count
