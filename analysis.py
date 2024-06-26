#!/usr/bin/python3

import copy
from collections import defaultdict
import itertools
import random
import sys
import math
from operations import Operations
from schedulers import random_scheduler, shortest_job_first, maximum_throughput
import generate_data

def run(ops, num_clients, scheduler):
    time =  0

    while(scheduler(ops, num_clients)):
        time +=  180
    return time

# 2kr experiment
def experiment_one():

    #parametro
    num_clients = 10
    num_experiments = 5
    num_rounds = 1

    #fator
    num_prefixes = 4
    total_pfx_available = 12

    dataset = generate_data.clients(num_clients, num_experiments, num_rounds, num_prefixes, total_pfx_available)
    ops_heuristic = Operations(dataset, num_clients)

    fd = open('heuristic_AB.csv', 'a')
    final_time = run(ops_heuristic, num_clients, maximum_throughput)
    print(final_time*num_rounds, file=fd)
    fd.close()
    '''
    A (prx)  B (avail_pfx)
    2        8

    4        12

    '''

# System comparison
def experiment_two():

    #parametro
    num_clients = 10
    num_experiments = random.randint(2, 4)
    num_rounds = 1

    #fator
    num_prefixes = 5
    total_pfx_available = 6

    dataset = generate_data.clients(num_clients, num_experiments, num_rounds, num_prefixes, total_pfx_available)

    ops = Operations(dataset, num_clients)
    ops_random = copy.deepcopy(ops)
    ops_sjf = copy.deepcopy(ops)
    ops_heuristic = copy.deepcopy(ops)

    row = list()
    fd = open('random.csv', 'a')
    final_time = run(ops_random, num_clients, random_scheduler)
    row.append(str(final_time*num_rounds))
    print(final_time*num_rounds, file=fd)
    fd.close()


    fd = open('sjf.csv', 'a')
    final_time = run(ops_sjf, num_clients, shortest_job_first)
    row.append(str(final_time*num_rounds))
    print(final_time*num_rounds, file=fd)
    fd.close()

    fd = open('heuristic.csv', 'a')
    final_time = run(ops_heuristic, num_clients, maximum_throughput)
    row.append(str(final_time*num_rounds))
    print(final_time*num_rounds, file=fd)
    fd.close()

    fd = open('experiment.csv', 'a')
    string = ','.join(row)
    print(string, file=fd)
    fd.close()

def main():
    experiment_two()

if __name__ == '__main__':
    sys.exit(main())
