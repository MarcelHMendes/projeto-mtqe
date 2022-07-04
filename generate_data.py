#!/usr/bin/python3
import copy
from collections import defaultdict
import itertools
import random
import sys
import math
from operations import Operations
from schedulers import random_scheduler, shortest_job_first, maximum_throughput

prefixes_available = ['A', 'B', 'C', 'D', 'E', 'F']

def generate_data_client(num_experiments, num_rounds, num_prefixes):
    experiment = list()
    for exp in range(num_experiments):
        rounds = list()
        for ro in range(num_rounds):
            prefixes = random.sample(prefixes_available, k=num_prefixes) #or random.choices allowing repetition
            rounds.append(list(set(prefixes)))
        experiment.append(rounds)
    return experiment

def clients(num_clients, num_exp, num_rounds, num_pfx):
    clients = defaultdict(list)

    for cli in range(num_clients):
        clients[f'client {str(cli)}'] = generate_data_client(num_exp,num_rounds,num_pfx)

    print(clients)
    return clients

def run(ops, num_clients, scheduler):
    time =  0

    while(scheduler(ops, num_clients)):
        time +=  90
    return time

def main():

    num_clients = 10
    num_experiments = 4
    num_rounds = 1
    num_prefixes = 3

    dataset = clients(num_clients, num_experiments, num_rounds, num_prefixes)
    ops_random = Operations(dataset, num_clients)

    ops_sjf = Operations(dataset, num_clients)
    ops_heuristic = Operations(dataset, num_clients)

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
    '''
    scheduler = maximum_throughput
    num_clients = 10
    num_experiments = 2
    num_rounds = 2
    num_prefixes = 1

    #if num_experiments == 0 or num_prefixes == 0:
    #    return

    dataset = clients(num_clients, num_experiments, num_rounds, num_prefixes)
    ops_lowA_lowB = Operations(dataset, num_clients)

    fd = open('-A-B.csv', 'a')
    final_time = run(ops_lowA_lowB, num_clients, scheduler)
    print(math.log10(final_time*num_rounds), file=fd)

    num_clients = 10
    num_experiments = 4 #A
    num_rounds = 2
    num_prefixes = 1 #B

    dataset = clients(num_clients, num_experiments, num_rounds, num_prefixes)
    ops_A_lowB = Operations(dataset, num_clients)

    fd = open('A-B.csv', 'a')
    final_time = run(ops_A_lowB, num_clients, scheduler)
    print(math.log10(final_time*num_rounds), file=fd)

    num_clients = 10
    num_experiments = 2 #A
    num_rounds = 2
    num_prefixes = 3 #B

    dataset = clients(num_clients, num_experiments, num_rounds, num_prefixes)
    ops_lowA_B = Operations(dataset, num_clients)

    fd = open('-AB.csv', 'a')
    final_time = run(ops_lowA_B, num_clients, scheduler)
    print(math.log10(final_time*num_rounds), file=fd)

    num_clients = 10
    num_experiments = 4 #A
    num_rounds = 2
    num_prefixes = 3 #B

    dataset = clients(num_clients, num_experiments, num_rounds, num_prefixes)
    ops_A_B = Operations(dataset, num_clients)

    fd = open('AB.csv', 'a')
    final_time = run(ops_A_B, num_clients, scheduler)
    print(math.log10(final_time*num_rounds), file=fd)

'''

if __name__ == '__main__':
    sys.exit(main())
