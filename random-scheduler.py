from collections import defaultdict
import itertools
import random
import sys


prefixes_available = ['A', 'B', 'C', 'D']

def generate_data_client(num_experiments, num_rounds, num_prefixes):
    experiment = list()
    for exp in range(num_experiments):
        rounds = list()
        for ro in range(num_rounds):
            prefixes = random.choices(prefixes_available, k=num_prefixes)
            rounds.append(list(set(prefixes)))
        experiment.append(rounds)
    return experiment

def clients(num_clients, num_exp, num_rounds, num_pfx):
    clients = defaultdict(list)

    for cli in range(num_clients):
        clients[f'client {str(cli)}'] = generate_data_client(num_exp,num_rounds,num_pfx)

    return clients

# criar um arquivo separado para os schedulers
def priority(clients):  #lower idx clients has priority
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

def run(clients, num_r):
    time =  0
    while(priority(clients)):
        time += num_r * 90
    print(time)

def main():
    num_rounds = 1
    clients_list = clients(3, 1, num_rounds, 1)
    run(clients_list, num_rounds)

if __name__ == '__main__':
    sys.exit(main())


#rever corretude do código
