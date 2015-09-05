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

author = 'dante'

f = open('./text files/'+author+'_nolines.txt', 'r')
text = f.read()
f.close()

counts = np.zeros(27)

n = len(text)
for c in text:
    i = ord(c) - 97 if ord(c) >= 97 else 26
    counts[i] += 1

print counts

# Convert counts to cdf
cdf = np.zeros_like(counts)
cdfij = counts/sum(counts)
cdf[0] = cdfij[0]
for k in range(1,27):
    cdf[k] = cdfij[k]+cdf[k-1]

print cdf

np.save('./data files/'+author+'1',cdf)
