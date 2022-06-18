#!/usr/bin/python3
import copy
from collections import defaultdict
import itertools
import random
import sys
from operations import Operations
from schedulers import random_scheduler, shortest_job_first, maximum_throughput

prefixes_available = ['A', 'B', 'C', 'D', 'E', 'F']

def generate_data_client(num_experiments, num_rounds, num_prefixes):
    experiment = list()
    for exp in range(num_experiments):
        rounds = list()
        for ro in range(num_rounds):
            prefixes = random.choices(prefixes_available, k=random.randint(1, num_prefixes))
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
    num_clients = 4
    num_experiments = random.randint(2,5) # int(random.normalvariate(3, 2))
    num_rounds = 1
    num_prefixes = random.randint(1,5) #int(random.normalvariate(3, 2)) %

    dataset = clients(num_clients, num_experiments, num_rounds, num_prefixes)
    ops = Operations(dataset, num_clients)

    ops_random = copy.deepcopy(ops)
    ops_sjf = copy.deepcopy(ops)
    ops_heuristic = copy.deepcopy(ops)

    fd = open('random.csv', 'a')
    final_time = run(ops_random, num_clients, random_scheduler)
    print(final_time*num_rounds, file=fd)
    fd.close()


    fd = open('sjf.csv', 'a')
    final_time = run(ops_sjf, num_clients, shortest_job_first)
    print(final_time*num_rounds, file=fd)
    fd.close()

    fd = open('heuristic.csv', 'a')
    final_time = run(ops_heuristic, num_clients, maximum_throughput)
    print(final_time*num_rounds, file=fd)
    fd.close()

if __name__ == '__main__':
    sys.exit(main())


#verificar corretude heuristic
