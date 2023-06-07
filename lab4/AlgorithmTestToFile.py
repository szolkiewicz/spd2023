from TestingEssentials import EvaluateCmax, GenerateJ, EvaluateC, EvalPenalty
from BruteForce import BruteForce
from GreedyMethod import GreedyMethod
from DPMethod import DP, DPmod, Backtrack
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# n = 8
# seed = 1
# print(EvaluateC(J))
# print(EvalPenalty(J))
# print("n:   ",n,"\nseed:",seed)
# print("\nzadania:         ",J)

BFTimes = []
GreedyTimes = []
DPTimes =[]

n = 18
seed = 1
#df = pd.DataFrame(columns=['data_size', 'greedy', 'brute_force', 'dynamic_programing', 'dynamic_programing_backtrack'])
df = pd.DataFrame(columns=['data_size', 'greedy', 'dynamic_programing', 'dynamic_programing_backtrack'])


for i in range(1,n+1):
    data = list(range(i))

    J = GenerateJ(i,seed)
    # start_time = time.time()
    # BFMinSum , BFtasks = BruteForce(J)
    # end_time = time.time()
    # bf_time = end_time - start_time

    start_time = time.time()
    GreedyTasks = GreedyMethod(J)
    end_time = time.time()
    greedy_time = end_time - start_time

    start_time = time.time()
    DPMinSuma = DP(J)
    end_time = time.time()
    dp_time = end_time - start_time

    start_time = time.time()
    DPMinSum, DPMoveTree = DPmod(J)
    DPTasks = Backtrack(DPMoveTree)
    end_time = time.time()
    dpbck_time = end_time - start_time
 

    df = df.append({'data_size' : i,
                     'greedy': greedy_time, 
                     #'brute_force' : bf_time, 
                     'dynamic_programing' : dp_time,
                     'dynamic_programing_backtrack' : dpbck_time}, ignore_index = True)


    print(i,"/",n)
    print(df)
    df.to_csv('wyniki.csv', index=False)


plt.close("all")
#df.plot(x='data_size', y=['greedy', 'brute_force', 'dynamic_programing', 'dynamic_programing_backtrack'], kind='line')
df.plot(x='data_size', y=['greedy', 'dynamic_programing', 'dynamic_programing_backtrack'], kind='line')

# Ustawienia wykresu
plt.title('times for different data sizes')
plt.xlabel('Data size')
plt.ylabel('Time (s)')

# Wyświetlenie wykresu
plt.show()
