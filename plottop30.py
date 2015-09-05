# Vim command to count occurrences of pattern
# :%s/pattern//gn

import numpy as np
import pylab as plt

lookup = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']

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
# ' ' - 26

f = open('./text files/twain_nolines.txt', 'r')
text = f.read()
f.close()

counts = np.zeros((27,27,27))

n = len(text)
for i in range(n-2):
    j = ord(text[i]) - 97 if ord(text[i]) >= 97 else 26
    k = ord(text[i+1]) - 97 if ord(text[i+1]) >= 97 else 26
    l = ord(text[i+2]) - 97 if ord(text[i+2]) >= 97 else 26
    counts[j,k,l] += 1

#for i in range(27):
#    print lookup[i] + ": %d"%counts[26][26][i]

max_count = 0
letters = []
for i in range(27):
    for j in range(27):
        for k in range(27):
            letters.append((counts[i,j,k],lookup[i]+lookup[j]+lookup[k]))
            if counts[i,j,k] > max_count:
                max_count = counts[i,j,k]
#print max_count
letters.sort(reverse=True)
freq = []
lets = []
for i in range(27**3):
    freq.append(letters[i][0])
    lets.append(letters[i][1])

print len(freq)

x = np.arange(27**3)
freq = np.array(freq)
plt.plot(x, freq)
plt.fill_between(x,freq,0)
plt.axis([0,27**3,0,35000])
#plt.xticks(x+.4, tuple(lets))
plt.xlabel('Three-letter combinations')
plt.ylabel('Count')
plt.title('Twain - all three letter combinations')
plt.show()
