from TestingEssentials import EvaluateCmax, GenerateJ, GetNumeration, GetListOfTasks, EvaluateC
from Johnson import JohnsonFLM, JohnsonVM
from BruteForce import BruteForce
from BnB import BnB
import time

n = 6
M = 4
seed = 1


J = GenerateJ(n,M,seed)

print("n:   ",n,"\nM:   ",M,"\nseed:",seed)
print("\nzadania:         ",J)

# your code here



start_time = time.time()
JFLMTasksNumeration = JohnsonFLM(J)
JFLMTasks = GetListOfTasks(J, JFLMTasksNumeration)
JFLMCmax = EvaluateCmax(JFLMTasks)
JFLMC = EvaluateC(JFLMTasks)
end_time = time.time()
timeJFLM = end_time - start_time

start_time = time.time()
JVMTasksNumeration = JohnsonVM(J) #zapytać prowadzącego czy na pewno jest ok bo coś dziwnie liczy
JVMTasks = GetListOfTasks(J, JVMTasksNumeration)
JVMCmax = EvaluateCmax(JVMTasks)
JVMC = EvaluateC(JVMTasks)
end_time = time.time()
timeJVM = end_time - start_time

start_time = time.time()
BruteForceCmax, BruteForceTasks = BruteForce(J)
BruteForceTasksNumeration = GetNumeration(J, BruteForceTasks)
BruteForceC = EvaluateC(BruteForceTasks)
end_time = time.time()
timeBF = end_time - start_time

start_time = time.time()
BnBCmax, BnBTasks = BnB(J)
BnBTasksNumeration = GetNumeration(J, BnBTasks)
BnBC = EvaluateC(BnBTasks)
end_time = time.time()
timeBnB = end_time - start_time

print("\nJohnson (rozszerzenie: bierze pod uwagę pierwszą i ostatnią maszynę):")
print("kolejność zadań: ", JFLMTasksNumeration)
print("zadania:         ", JFLMTasks)
print("Cmax:            ", JFLMCmax)
print("C:               ", JFLMC)
print("time:               ", timeJFLM)

print("\nJohnson (rozszerzenie: virtualne maszyny):")
print("kolejność zadań: ", JVMTasksNumeration)
print("zadania:         ", JVMTasks)
print("Cmax:            ", JVMCmax)
print("C:               ", JVMC)
print("time:               ", timeJVM)

print("\nBruteForce:")
print("kolejność zadań: ", BruteForceTasksNumeration)
print("zadania:         ", BruteForceTasks)
print("Cmax:            ", BruteForceCmax)
print("C:               ", BruteForceC)
print("time:               ", timeBF)

print("\nBnB:")
print("kolejność zadań: ", BnBTasksNumeration)
print("zadania:         ", BnBTasks)
print("Cmax:            ", BnBCmax)
print("C:               ", BnBC)
print("time:               ", timeBnB)