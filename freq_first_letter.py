import numpy as np
import pylab as plt

lookup = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# A - 0
# B - 1
# C - 2
# D - 3
# E - 4
# F - 5
# G - 6
# H - 7
# I - 8
# J - 9
# K - 10
# L - 11
# M - 12
# N - 13
# O - 14
# P - 15
# Q - 16
# R - 17
# S - 18
# T - 19
# U - 20
# V - 21
# W - 22
# X - 23
# Y - 24
# Z - 25

author = 'dante'

f = open('./text files/'+author+'_nolines.txt', 'r')
text = f.read()
f.close()

counts = np.zeros(26)

n = len(text)
for i in range(len(text)-1):
    if text[i] == ' ':
        i = ord(text[i+1]) - 97
        try:
            counts[i] += 1
        except:
            print i

print counts

# Convert counts to cdf
pdf = np.zeros_like(counts)
pdf = counts/sum(counts)
cdf = np.zeros_like(pdf)
cdf[0] = pdf[0]
for i in range(1,len(cdf)):
    cdf[i] = pdf[i] + cdf[i-1]

#print cdf

#x = np.arange(26)
#plt.bar(x,cdf,1)
#plt.xticks(x+.5, tuple(lookup))
#plt.title('Twain: relative frequency as first letter of word')
#plt.xlim(0,26)
#plt.show()

np.save('./data files/'+author+'first',cdf)
