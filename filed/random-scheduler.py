#!/usr/bin/python3

from collections import defaultdict
import itertools
import random
import sys


number_of_choices = [1,2,3,4]

def generate_data_client(num_experiments, num_rounds, num_prefixes):
    experiment = list()
    for exp in range(num_experiments):
        experiment.append(random.choice(number_of_choices))
    return experiment

def clients(num_clients, num_exp, num_rounds, num_pfx):
    clients = defaultdict(list)

    for cli in range(num_clients):
        clients[f'client {str(cli)}'] = generate_data_client(num_exp,num_rounds,num_pfx)

    print(clients)

    return clients

# criar um arquivo separado para os schedulers
def priority(clients):  #lower-index clients have higher priority
    experiments = list()
    prefixes_available  = ['A', 'B', 'C', 'D']
    prefixes_in_use = list()
    for idx in clients:
        if clients[idx]:
            flatten_exp_num = int(clients[idx][0])
            if len(prefixes_available) >= flatten_exp_num:
                prefixes_in_use.extend(random.choices(prefixes_available, k=flatten_exp_num))
                experiments.append(clients[idx].pop(0))
    print(experiments)
    return experiments

def run(clients, num_r):
    time =  0
    while(priority(clients)):
        time += num_r * 90
    print(time)

def main():
    num_rounds = 3
    num_experiments = 1
    num_clients = 5
    num_prefixes = 2

    clients_list = clients(num_clients, num_experiments, num_rounds, num_prefixes)
    run(clients_list, num_rounds)

if __name__ == '__main__':
    sys.exit(main())


#rever corretude do código
