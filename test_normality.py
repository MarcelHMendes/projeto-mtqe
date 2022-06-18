#!/usr/bin/python3

from numpy.random import seed
from numpy.random import randn
from matplotlib import pyplot

for arq in ['random.csv', 'sjf.csv', 'heuristic.csv']:
    data = list()
    fd = open(arq, 'r')
    for i in fd:
        data.append(int(i))
    # histogram plot
    pyplot.hist(data)
    #pyplot.show()
    pyplot.savefig(f"{arq}.png")
    pyplot.clf()
