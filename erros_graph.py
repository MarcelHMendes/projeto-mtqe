#!/usr/bin/python3
import os
import random
import sys
from matplotlib import pyplot

if os.path.exists("erros.csv"):
    os.remove("erros.csv")
    print("The file has been deleted successfully")

files = list()
for f in range(1, len(sys.argv)):
    files.append(sys.argv[f])

fd_out = open('erros.csv', 'a')

for arq in files:
    data = list()
    fd = open(arq, 'r')
    for i in fd:
        data.append(float(i))


    average = sum(data)/len(data)
    for value in data:
        print(value - average, file=fd_out)

fd_out.close()

e_data = list()
fd = open('erros.csv', 'r')

for error in fd:
    e_data.append(float(error))
print(sum(e_data))

#e_data = random.sample(e_data, k=50)
random.shuffle(e_data)
pyplot.scatter(list(range(len(e_data))), e_data, marker='.')
pyplot.savefig("errors_graph.png")
