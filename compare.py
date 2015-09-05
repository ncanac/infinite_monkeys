import numpy as np
import sys
import multiprocessing as mp
import time

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
# SPACE - 26

lookup = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def gettext(words):
    text = ''
    for i in range(len(words)-1):
        text += words[i] + ' '
    text += words[len(words)-1]
    return text

# Returns a word of length n where each character is
# drawn from a uniform distribution
def zeroth_monkey(n, cdf):
    np.random.seed()
    pattern = ''
    for i in range(n):
        pattern += lookup[np.random.randint(0,27)]
    return pattern

# Returns a word of length n where each character is
# drawn with probability based on the frequency with which
# that character appears in some text with given cdf.
def first_monkey(n, cdfs):
    np.random.seed()
    pattern = ''
    for i in range(n):
        pattern += lookup[np.where(np.random.rand()<=cdfs[0])[0][0]]
    return pattern

def second_monkey(n, cdfs):
    np.random.seed()
    l1 = np.where(np.random.rand()<=cdfs[0])[0][0]
    pattern = lookup[l1]
    for i in range(n-1):
        l2 = np.where(np.random.rand()<=cdfs[1][l1,:])[0][0]
        pattern += lookup[l2]
        l1 = l2
    return pattern

# Returns a word of length n where each character is
# drawn with probability based on the previous two letters
# using cumulative distribution function given by cdf
def third_monkey(n, cdfs):
    np.random.seed()
    l1 = np.where(np.random.rand()<=cdfs[0])[0][0]
    pattern = lookup[l1]
    l2 = np.where(np.random.rand()<=cdfs[1][l1,:])[0][0]
    pattern += lookup[l2]
    for i in range(n-2):
        l3 = np.where(np.random.rand()<=cdfs[2][l1,l2,:])[0][0]
        pattern += lookup[l3]
        l1 = l2
        l2 = l3
    return pattern

def fourth_monkey(n, cdfs):
    np.random.seed()
    l1 = np.where(np.random.rand()<=cdfs[0])[0][0]
    pattern = lookup[l1]
    l2 = np.where(np.random.rand()<=cdfs[1][l1,:])[0][0]
    pattern += lookup[l2]
    l3 = np.where(np.random.rand()<=cdfs[2][l1,l2,:])[0][0]
    pattern += lookup[l3]
    for i in range(n-3):
        l4 = np.where(np.random.rand()<=cdfs[3][l1,l2,l3,:])[0][0]
        pattern += lookup[l4]
        l1 = l2
        l2 = l3
        l3 = l4
    return pattern

def fifth_monkey(n, cdfs):
    np.random.seed()
    l1 = np.where(np.random.rand()<=cdfs[0])[0][0]
    pattern = lookup[l1]
    l2 = np.where(np.random.rand()<=cdfs[1][l1,:])[0][0]
    pattern += lookup[l2]
    l3 = np.where(np.random.rand()<=cdfs[2][l1,l2,:])[0][0]
    pattern += lookup[l3]
    l4 = np.where(np.random.rand()<=cdfs[3][l1,l2,l3,:])[0][0]
    pattern += lookup[l4]
    for i in range(n-4):
        l5 = np.where(np.random.rand()<=cdfs[4][l1,l2,l3,l4,:])[0][0]
        pattern += lookup[l5]
        l1 = l2
        l2 = l3
        l3 = l4
        l4 = l5
    return pattern

def monkey(order, n, mtype, texttype):
    dpath = './data files/'
    f = open('./text files/' + texttype + '_nolines.txt', 'r')
    text = f.read()
    f.close()
    switch = {
        0: (zeroth_monkey, []),
        1: (first_monkey, [np.load(dpath+mtype+'1.npy')]),
        2: (second_monkey, [np.load(dpath+mtype+'first.npy'),np.load(dpath+mtype+'2.npy')]),
        3: (third_monkey, [np.load(dpath+mtype+'first.npy'),np.load(dpath+mtype+'2.npy'),np.load(dpath+mtype+'3.npy')]),
        4: (fourth_monkey, [np.load(dpath+mtype+'first.npy'),np.load(dpath+mtype+'2.npy'),np.load(dpath+mtype+'3.npy'),np.load(dpath+mtype+'4.npy')]),
        5: (fifth_monkey, [np.load(dpath+mtype+'first.npy'),np.load(dpath+mtype+'2.npy'),np.load(dpath+mtype+'3.npy'),np.load(dpath+mtype+'4.npy'),np.load(dpath+mtype+'5.npy')])}
    monkey, cdfs = switch.get(order)
    pattern = monkey(n,cdfs)
    count = 0
    while not (pattern in text):
        count += 1
        pattern = monkey(n,cdfs)
    return count

def main():
    N = 100
    
#    print '1'
#    log = open('./comp logs/twaintwaincompare.txt','w')
#    for i in range(N):
#        log.write(str(monkey(5,17,'twain','twain'))+'\n')
#    log.close()
#    
#    print '2'
#    log = open('./comp logs/twainshakecompare.txt','w')
#    for i in range(N):
#        log.write(str(monkey(5,17,'twain','shake'))+'\n')
#    log.close()
#    
#    print'3'
#    log = open('./comp logs/shakeshakecompare.txt','w')
#    for i in range(N):
#        log.write(str(monkey(5,17,'shake','shake'))+'\n')
#    log.close()
#    
#    print'4'
#    log = open('./comp logs/shaketwaincompare.txt','w')
#    for i in range(N):
#        log.write(str(monkey(5,17,'shake','twain'))+'\n')
#    log.close()
    
    print'5'
    log = open('./comp logs/dantedantecompare.txt','w')
    for i in range(N):
        log.write(str(monkey(5,10,'dante','dante'))+'\n')
    log.close()
#    
#    N = 100
#    
#    print '6'
#    log = open('./comp logs/dantetwaincompare5.txt','w')
#    for i in range(N):
#        log.write(str(monkey(5,10,'dante','twain'))+'\n')
#    log.close()
#    
#    print '7'
#    log = open('./comp logs/danteshakecompare5.txt','w')
#    for i in range(N):
#        log.write(str(monkey(5,10,'dante','shake'))+'\n')
#    log.close()
#    
#    print '8'
#    log = open('./comp logs/shakedantecompare5.txt','w')
#    for i in range(N):
#        log.write(str(monkey(5,10,'shake','dante'))+'\n')
#    log.close()
#    
#    print '9'
#    log = open('./comp logs/twaindantecompare5.txt','w')
#    for i in range(N):
#        log.write(str(monkey(5,10,'twain','dante'))+'\n')
#    log.close()

main()
