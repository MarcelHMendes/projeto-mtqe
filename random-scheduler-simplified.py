#!/usr/bin/python3
import copy
from collections import defaultdict
import itertools
import random
import sys

class Operations:
    rounds_queue = defaultdict(list)

    def __init__(self, clients_data, num_clients)
        self.rounds_queue = clients_data
        self.number_of_clients = num_clients

    def get_item_random(self):
        choice = random.randint(1, num_clients)
        return (rounds_queue[f'client {choice}'].pop(0), choice)

    def add_item(self, choice, item):
        self.round_candidates[f'client {choice}'].insert(0, item)



prefixes_available = ['A', 'B', 'C', 'D']

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

# criar um arquivo separado para os schedulers
def priority_scheduler(clients):  #lower-index clients have higher priority
    experiments = list()
    prefixes_in_use = list()
    for idx in clients:
        if clients[idx]:
            flatten_exp_pfx = list(itertools.chain(*clients[idx][0]))
            if not any(item in flatten_exp_pfx for item in prefixes_in_use):
                experiments.append(clients[idx].pop(0))
                prefixes_in_use.extend(flatten_exp_pfx)
    print(experiments)
    return experiments


def shuffle_experiments(clients):
    rodada = 0
    shuffled_experiments = defaultdict(list)

    for i in range(len(clients['client 0'])):   #number of experiments
        round_candidates = list()
        for idx in clients:
            round_candidates.append(clients[idx][rodada])
        #print(round_candidates)
        random.shuffle(round_candidates)
        rodada += 1
        for c in range(len(round_candidates)):
            shuffled_experiments[f'stack {c}'].append(round_candidates[c])

    print(shuffled_experiments)
    return shuffled_experiments

def random_scheduler(shuffled_experiments):
    experiments = list()
    prefixes_in_use = list()

    for idx in shuffled_experiments:    #errado
        if shuffled_experiments[idx]:
            flatten_exp_pfx = list(itertools.chain(*shuffled_experiments[idx][0]))
            if not any(item in flatten_exp_pfx for item in prefixes_in_use):
                experiments.append(shuffled_experiments[idx].pop(0))
                prefixes_in_use.extend(flatten_exp_pfx)
    print(experiments)
    return experiments


def run(clients, scheduler):
    time =  0
    while(scheduler(clients)):
        time +=  90
    return time

def main():
    num_clients = 5
    num_experiments = 3
    num_rounds = 3
    num_prefixes = 3

    dataset = clients(num_clients, num_experiments, num_rounds, num_prefixes)

    dataset_priority = copy.deepcopy(dataset)
    dataset_random = copy.deepcopy(dataset)

    final_time = run(dataset_priority, priority_scheduler)
    print(final_time*num_rounds)

    final_time = run(shuffle_experiments(dataset_random), random_scheduler)
    print(final_time*num_rounds)

if __name__ == '__main__':
    sys.exit(main())


#rever corretude do código
