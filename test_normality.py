#!/usr/bin/python3
import sys

from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

files = list()
for f in range(1, len(sys.argv)):
    files.append(sys.argv[f])

for arq in files:
    data = list()
    fd = open(arq, 'r')
    for i in fd:
        data.append(int(i))
    # histogram plot
    pyplot.hist(data)
    #pyplot.show()
    pyplot.savefig(f"{arq}.png")
    pyplot.clf()
