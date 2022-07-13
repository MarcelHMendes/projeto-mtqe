#!/usr/bin/python3
from collections import defaultdict
import math
import os
import random
import sys
from matplotlib import pyplot
import re
import numpy as np

files = list()
for f in range(1, len(sys.argv)):
    files.append(sys.argv[f])

print(files)

y_list = defaultdict(float)
replications = defaultdict(list)


for arq in files:
    data = list()
    fd = open(arq, 'r')
    for i in fd:
        data.append(float(i))
    index = arq.split('.')[0]

    replications[index] = np.sqrt(data)

    #calculo y's
    soma = 0
    for y in replications[index]:
        soma += y


    y_list[index] = soma/len(replications[index])
    fd.close()

print(y_list)

assert len(y_list) == len(files)

q0 = y_list['heuristic_ab'] + y_list['heuristic_Ab'] + y_list['heuristic_aB'] + y_list['heuristic_AB']

qA = (-1 * y_list['heuristic_ab']) +  y_list['heuristic_Ab'] + (-1 *  y_list['heuristic_aB']) + y_list['heuristic_AB']

qB = (-1 * y_list['heuristic_ab']) +  (-1 * y_list['heuristic_Ab']) + y_list['heuristic_aB'] + y_list['heuristic_AB']

qAB =  y_list['heuristic_ab'] + (-1 * y_list['heuristic_Ab']) + (-1 * y_list['heuristic_aB']) + y_list['heuristic_AB']

q0 = q0/4
qA = qA/4
qB = qB/4
qAB = qAB/4

#calculo erro
SSE = 0    #variacao total
for j in y_list:
    for yi in replications[j]:
        SSE += (yi - y_list[j])**2

SSA = 4 * 500 * (qA**2)
SSB = 4 * 500 * (qB**2)
SSAB = 4 * 500 * (qAB**2)

SST = SSA + SSB + SSAB + SSE

print(q0, qA, qB, qAB)
print(SSA, SSB, SSAB, SST)
print(SSE)

print('Variação explicada por A (# prefixes):')
print(round((SSA/SST)*100, 2), end='%\n')

print('Variação explicada por B (# available prefixes):')
print(round((SSB/SST)*100, 2), end='%\n')

print('Variação explicada pela interação AB:')
print(round((SSAB/SST)*100, 2), end='%\n')

print('Variação não explicada:')
print(round((SSE/SST)*100, 2), end='%\n')



#Intervalo de confiança para os efeitos

Se = math.sqrt(SSE/(4 * 499))
print('Desvio padrão do erro')
print(Se)

Sqi = Se/math.sqrt((4 * 500))

print('Desvio padrão dos efeitos')
print(Sqi)

print("Intervalo para 95% de confiança para os efeitos dof(1999)")
print(f'q0: {q0} +- {0.062715 * Sqi }')
print(f'qA: {qA} +- {0.062715 * Sqi }')
print(f'qB: {qB} +- {0.062715 * Sqi }')
print(f'qAB: {qAB} +- {0.062715 * Sqi }')

'''
ab
Ab
aB
AB
'''
