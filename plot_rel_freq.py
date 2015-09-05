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

f = open('./text files/dante_nolines.txt', 'r')
text = f.read()
f.close()

counts = np.zeros(26)

n = len(text)
for c in text:
    if ord(c) >= 97:
        i = ord(c) - 97
        counts[i] += 1

print counts

# Convert counts to cdf
pdf = np.zeros_like(counts)
pdf = counts/sum(counts)

print pdf

x = np.arange(26)
plt.bar(x,pdf,1)
plt.xticks(x+.5, tuple(lookup))
plt.title('Relative frequency of letters in Dante\'s writings')
plt.xlim(0,26)
plt.show()

#np.save('twain3',cdf)
