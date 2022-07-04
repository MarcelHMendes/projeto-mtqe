#!/usr/bin/python3
import copy
from collections import defaultdict
import itertools
import random
import sys
import math
import string
from operations import Operations
from schedulers import random_scheduler, shortest_job_first, maximum_throughput



def generate_data_client(num_experiments, num_rounds, num_prefixes, prefixes_available):
    experiment = list()
    for exp in range(num_experiments):
        rounds = list()
        for ro in range(num_rounds):
            prefixes = random.sample(prefixes_available, k=num_prefixes) # or random.choices allowing repetition
            rounds.append(list(set(prefixes)))
        experiment.append(rounds)
    return experiment

def clients(num_clients, num_exp, num_rounds, num_pfx, available_pfx):
    clients = defaultdict(list)

    prefixes_available = list(string.ascii_uppercase)
    prefixes_available = prefixes_available[0:available_pfx]

    for cli in range(num_clients):
        clients[f'client {str(cli)}'] = generate_data_client(num_exp,num_rounds,num_pfx, prefixes_available)

    print(clients)
    return clients
