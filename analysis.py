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

def main():

    num_clients = 10
    num_experiments = 5
    num_rounds = 1
    num_prefixes = 3

    dataset = generate_data.clients(num_clients, num_experiments, num_rounds, num_prefixes)
    ops_heuristic = Operations(dataset, num_clients)

    fd = open('heuristic.csv', 'a')
    final_time = run(ops_heuristic, num_clients, maximum_throughput)
    print(final_time*num_rounds, file=fd)
    fd.close()

if __name__ == '__main__':
    sys.exit(main())
