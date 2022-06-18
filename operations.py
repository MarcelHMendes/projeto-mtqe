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

    def get_item(self, item_id):
        if self.rounds_queue[f'client {item_id}']:
            return (self.rounds_queue[f'client {item_id}'].pop(0), item_id)
        return False

    def get_itens(self, id_list):
        return_list = list()
        for id in range(len(id_list)):
            if id_list[id]==1 and self.rounds_queue[f'client {id}']:
                return_list.append((self.rounds_queue[f'client {id}'][0], id))
        return return_list

    def remove_itens(self, item_id_list):
        for item in item_id_list:
            if self.rounds_queue[f'client {item[1]}']:
                self.rounds_queue[f'client {item[1]}'].pop(0)

    def add_itens(self, item_id_list):
        for item in item_id_list:
            self.rounds_queue[f'client {item[1]}'].insert(0, item[0])

    def add_item(self, item, choice):
        self.rounds_queue[f'client {choice}'].insert(0, item)
