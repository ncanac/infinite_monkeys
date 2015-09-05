import numpy as np
import pylab as plt
from scipy.stats import t
import math

def error_bar(data, conf=.95):
    N = len(data)
    h = ( np.std(data) / (N**(1./2)) ) * t.ppf((1.+conf)/2., N-1)
    return h

#####################################################
#################### Zeroth #########################

x = []
counts = []
error = []
sd = []
for i in range(2,7):
    data = []
    f = open('./time/time_zeroth_' + str(i), 'r')
    for line in f:
        data.append(float(line))
    f.close()
    data = np.array(data)
    x.append(i)
    counts.append(np.mean(data))
    error.append(error_bar(data))
x = np.array(x,dtype=float)
plt.errorbar(x,counts,error,fmt='o',ecolor='b')

# Fit data
logcounts = []
for i in range(len(counts)):
    if counts[i] > 0:
        logcounts.append(math.log(counts[i]))
    else:
        x = np.delete(x,i)
logcounts = np.array(logcounts)
coeffs = np.polyfit(x,logcounts,1)
x = np.arange(1,21,dtype=float)
y = math.e**(coeffs[0]*x + coeffs[1])
p0 = plt.plot(x, y, 'b')
label0 = 'Zeroth = %.6fe^(%.3fn)' % (math.e**(coeffs[1]), coeffs[0])


#####################################################
##################### First #########################

x = []
counts = []
error = []
sd = []
for i in range(2,9):
    data = []
    f = open('./time/time_first_' + str(i), 'r')
    for line in f:
        data.append(float(line))
    f.close()
    data = np.array(data)
    x.append(i)
    counts.append(np.mean(data))
    error.append(error_bar(data))
x = np.array(x,dtype=float)
plt.errorbar(x,counts,error,fmt='o',ecolor='g')

# Fit data
logcounts = []
for i in range(len(counts)):
    if counts[i] > 0:
        logcounts.append(math.log(counts[i]))
    else:
        x = np.delete(x,i)
logcounts = np.array(logcounts)
coeffs = np.polyfit(x,logcounts,1)
x = np.arange(1,21,dtype=float)
y = math.e**(coeffs[0]*x + coeffs[1])
p1 = plt.plot(x, y, 'g')
label1 = 'First = %.6fe^(%.3fn)' % (math.e**(coeffs[1]), coeffs[0])

#####################################################
#################### Second #########################

x = []
counts = []
error = []
sd = []
for i in range(2,12):
    data = []
    f = open('./time/time_second_' + str(i), 'r')
    for line in f:
        data.append(float(line))
    f.close()
    data = np.array(data)
    x.append(i)
    counts.append(np.mean(data))
    error.append(error_bar(data))
x = np.array(x,dtype=float)
plt.errorbar(x,counts,error,fmt='o',ecolor='r')

# Fit data
logcounts = []
for i in range(len(counts)):
    if counts[i] > 0:
        logcounts.append(math.log(counts[i]))
    else:
        x = np.delete(x,i)
logcounts = np.array(logcounts)
coeffs = np.polyfit(x,logcounts,1)
x = np.arange(1,21,dtype=float)
y = math.e**(coeffs[0]*x + coeffs[1])
p2 = plt.plot(x, y, 'r')
label2 = 'Second = %.6fe^(%.3fn)' % (math.e**(coeffs[1]), coeffs[0])

#####################################################
##################### Third #########################

x = []
counts = []
error = []
sd = []
for i in range(3,15):
    data = []
    f = open('./time/time_third_' + str(i), 'r')
    for line in f:
        data.append(float(line))
    f.close()
    data = np.array(data)
    x.append(i)
    counts.append(np.mean(data))
    error.append(error_bar(data))
x = np.array(x,dtype=float)
plt.errorbar(x,counts,error,fmt='o',ecolor='c')

# Fit data
logcounts = []
for i in range(len(counts)):
    if counts[i] > 0:
        logcounts.append(math.log(counts[i]))
    else:
        x = np.delete(x,i)
logcounts = np.array(logcounts)
coeffs = np.polyfit(x,logcounts,1)
x = np.arange(1,21,dtype=float)
y = math.e**(coeffs[0]*x + coeffs[1])
p3 = plt.plot(x, y, 'c')
label3 = 'Third = %.6fe^(%.3fn)' % (math.e**(coeffs[1]), coeffs[0])

#####################################################
#################### Fourth #########################

x = []
counts = []
error = []
sd = []
for i in range(4,18):
    data = []
    f = open('./time/time_fourth_' + str(i), 'r')
    for line in f:
        data.append(float(line))
    f.close()
    data = np.array(data)
    x.append(i)
    counts.append(np.mean(data))
    error.append(error_bar(data))
x = np.array(x,dtype=float)
plt.errorbar(x,counts,error,fmt='o',ecolor='m')

# Fit data
logcounts = []
for i in range(len(counts)):
    if counts[i] > 0:
        logcounts.append(math.log(counts[i]))
    else:
        x = np.delete(x,i)
logcounts = np.array(logcounts)
coeffs = np.polyfit(x,logcounts,1)
x = np.arange(1,21,dtype=float)
y = math.e**(coeffs[0]*x + coeffs[1])
p4 = plt.plot(x, y, 'm')
label4 = 'Fourth = %.6fe^(%.3fn)' % (math.e**(coeffs[1]), coeffs[0])

#####################################################
##################### Fifth #########################

x = []
counts = []
error = []
sd = []
for i in range(5,20):
    data = []
    f = open('./time/time_fifth_' + str(i), 'r')
    for line in f:
        data.append(float(line))
    f.close()
    data = np.array(data)
    x.append(i)
    counts.append(np.mean(data))
    error.append(error_bar(data))
x = np.array(x,dtype=float)
plt.errorbar(x,counts,error,fmt='o',color='k')

# Fit data
logcounts = []
for i in range(len(counts)):
    if counts[i] > 0:
        logcounts.append(math.log(counts[i]))
    else:
        x = np.delete(x,i)
logcounts = np.array(logcounts)
coeffs = np.polyfit(x,logcounts,1)
x = np.arange(1,21,dtype=float)
y = math.e**(coeffs[0]*x + coeffs[1])
p5 = plt.plot(x, y, 'k')
label5 = 'Fifth = %.6fe^(%.3fn)' % (math.e**(coeffs[1]), coeffs[0])

plt.semilogy()
plt.grid(True)
plt.legend([p0,p1,p2,p3,p4,p5],[label0, label1, label2, label3, label4, label5],loc=4)
plt.xlabel('Number of characters (n)')
plt.xlim(1,20)
plt.xticks(np.arange(1,21,2))
plt.ylabel('Number of iterations')
plt.ylim(.001, 1000000000)
plt.title('Average number of iterations required to produce text of length n')
plt.show()
