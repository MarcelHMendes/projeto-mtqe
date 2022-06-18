#!/usr/bin/python3
import copy
from collections import defaultdict
import itertools
import random
import sys

class Operations:
    rounds_queue = defaultdict(list)

    def __init__(self, clients_data, num_clients):
        self.rounds_queue = clients_data
        self.number_of_clients = num_clients
        self.choices = [item for item in range(0, num_clients)]

    def get_item_random(self, chosed):
        available_choices = list()
        for i in self.choices:
            if not i in chosed and self.rounds_queue[f'client {i}']:
                available_choices.append(i)
        if available_choices:
            choice = random.choice(available_choices)
            return (self.rounds_queue[f'client {choice}'].pop(0), choice)
        return False

    def get_item_short(self, chosed):
        available_choices = list()
        for i in self.choices:
            if not i in chosed and self.rounds_queue[f'client {i}']:
                available_choices.append(i)
        if available_choices:
            menor = available_choices[0]
            for choice in available_choices:
                flatten_exp_pfx = list(itertools.chain(*self.rounds_queue[f'client {choice}'][0]))
                flatten_exp_menor = list(itertools.chain(*self.rounds_queue[f'client {menor}'][0]))
                if len(flatten_exp_pfx) < len(flatten_exp_menor):
                    menor = choice
            return (self.rounds_queue[f'client {menor}'].pop(0), menor)
        return False


    def add_item(self, item, choice):
        self.rounds_queue[f'client {choice}'].insert(0, item)





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

def random_scheduler(ops, num_clients):
    experiments = list()
    choice_of_the_round = list()
    prefixes_in_use = list()

    for i in range(num_clients):
        item = ops.get_item_random(choice_of_the_round)
        if item:
            flatten_exp_pfx = list(itertools.chain(*item[0]))
            if not any(pfx in flatten_exp_pfx for pfx in prefixes_in_use):
                choice_of_the_round.append(item[1])
                experiments.append(item[0])
                prefixes_in_use.extend(flatten_exp_pfx)
            else:
                ops.add_item(item[0], item[1])

    print(experiments)
    return experiments

def shortest_job_first(ops, num_clients):
    experiments = list()
    choice_of_the_round = list()
    prefixes_in_use = list()

    for i in range(num_clients):
        item = ops.get_item_short(choice_of_the_round)
        if item:
            flatten_exp_pfx = list(itertools.chain(*item[0]))
            if not any(pfx in flatten_exp_pfx for pfx in prefixes_in_use):
                choice_of_the_round.append(item[1])
                experiments.append(item[0])
                prefixes_in_use.extend(flatten_exp_pfx)
            else:
                ops.add_item(item[0], item[1])

    print(experiments)
    return experiments


def add_one(self, array_bit):
    flag = 0
    for b in array_bit:
        if b == 0:
            flag = 1
    if flag:
        for i in range(len(array_bit)-1, -1, -1):
            if array_bit[i] == 0:
                array_bit[i] = 1
                break
            array_bit[i] = 0
        return array_bit
    return False # add one will overflow the array

def run(ops, num_clients, scheduler):
    time =  0

    while(scheduler(ops, num_clients)):
        time +=  90
    return time

def main():
    num_clients = 4
    num_experiments = 2
    num_rounds = 1
    num_prefixes = 3

    dataset = clients(num_clients, num_experiments, num_rounds, num_prefixes)
    ops = Operations(dataset, num_clients)

    ops_random = copy.deepcopy(ops)
    ops_sjf = copy.deepcopy(ops)


    final_time = run(ops_random, num_clients, random_scheduler)
    print(final_time*num_rounds)

    final_time = run(ops_sjf, num_clients, shortest_job_first)
    print(final_time*num_rounds)

if __name__ == '__main__':
    sys.exit(main())


#rever corretude do código
