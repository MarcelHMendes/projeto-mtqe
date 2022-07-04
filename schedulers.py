#!/usr/bin/python3
import copy
from collections import defaultdict
import itertools
import random
import sys

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

def maximum_throughput(ops, num_clients):
    experiments = list()
    choices_of_the_round = list()
    prefixes_in_use = list()
    bitmap = [0] * num_clients

    maximum = []
    for _ in range(2**num_clients):
        experiments.clear()
        prefixes_in_use.clear()
        bitmap = _add_one(bitmap)
        itens = ops.get_itens(bitmap)

        for item in itens:
            flatten_exp_pfx = list(itertools.chain(*item[0]))
            if not any(pfx in flatten_exp_pfx for pfx in prefixes_in_use):
                experiments.append(item)
                prefixes_in_use.extend(flatten_exp_pfx)
            else:
                experiments.clear()
                break

        if len(experiments) > len(maximum):
            maximum = copy.deepcopy(experiments)
    ops.remove_itens(maximum)
    #print(maximum)
    return maximum

def _add_one(array_bit):
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
    return [] #overflow
