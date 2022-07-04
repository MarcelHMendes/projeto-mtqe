#!/usr/bin/python3

import numpy as np
import scipy.stats as st
import csv
# define sample data
#gfg_data = np.random.randint(5, 10, 100)
file = open('experiment_differences.csv')
csv_data = csv.reader(file)
next(csv_data)


random_sjf = list()
random_maxt = list()
sjf_maxt = list()

for row in csv_data:
    random_sjf.append(int(row[0]))
    random_maxt.append(int(row[1]))
    sjf_maxt.append(int(row[2]))

# create 95% confidence interval
# for population mean weight
resp = st.norm.interval(alpha=0.95,
                 loc=np.mean(sjf_maxt),
                 scale=st.sem(sjf_maxt))

print(resp)
print(sum(resp)/2)
