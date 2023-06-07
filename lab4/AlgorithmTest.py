from TestingEssentials import EvaluateCmax, GenerateJ, EvaluateC, EvalPenalty
from BruteForce import BruteForce
from GreedyMethod import GreedyMethod
from DPMethod import DP, DPmod, Backtrack
import time

n = 8
seed = 1


J = GenerateJ(n,seed)


print("n:   ",n,"\nseed:",seed)
print("\nzadania:         ",J)

print(EvaluateC(J))
print(EvalPenalty(J))

BFMinSum , BFtasks = BruteForce(J)
GreedyTasks = GreedyMethod(J)
GreedyMinSum = EvalPenalty(GreedyTasks)
DPMinSum, DPMoveTree = DPmod(J)
DPTasks = Backtrack(DPMoveTree)
print("Greedy",GreedyMinSum)
print("Brute Froce",BFtasks)
print("DP",DPMinSum)
print(DPTasks)

