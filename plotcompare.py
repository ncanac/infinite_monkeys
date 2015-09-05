import pylab as plt
import numpy as np
from scipy.stats import t

path = './comp logs/'
files = [path+'twaintwaincompare.txt', path+'twainshakecompare.txt', path+'shakeshakecompare.txt', path+'shaketwaincompare.txt']
labels = ['Twain - Twain', 'Twain - Shakespeare', 'Shakespeare - Shakespeare', 'Shakespeare - Twain']

def error_bar(data, conf=.95):
    N = len(data)
    h = ( np.std(data) / (N**(1./2)) ) * t.ppf((1.+conf)/2., N-1)
    return h

avgs = []
error = []
for fname in files:
    data = []
    f = open(fname, 'r')
    for line in f:
        data.append(float(line))
    f.close()
    data = np.array(data)
    avgs.append(np.mean(data))
    error.append(error_bar(data))
avgs = np.array(avgs)
error = np.array(error)
x = np.arange(len(avgs))
plt.bar(x, avgs, .4, color='c', yerr=error)
plt.xticks(x+.2, labels)
plt.title('Comparison between Shakespeare and Twain monkeys of average iterations (n = 17)')
plt.ylabel('Iterations')
plt.grid(True)
plt.show()
