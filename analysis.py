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

# Convert counts to cdf
cdf = np.zeros_like(counts)
for i in range(27):
    for j in range(27):
        cdfij = counts[i,j,:]/sum(counts[i,j,:])
        cdf[i,j,0] = cdfij[0]
        for k in range(1,27):
            cdf[i,j,k] = cdfij[k]+cdf[i,j,k-1]

np.save('twain3',cdf)
