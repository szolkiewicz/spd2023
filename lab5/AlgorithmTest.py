<<<<<<< HEAD:lab5/AlgorithmTest.py
from TestingEssentials import GenerateJ, GetListOfTasks, EvaluateC,plot_schedule_fancy, plot_schedule, start_t, tasks_df
from NEH import CalculateCmax, neh
from NEHmod import neh_mod, neh_modminCmax


n = 5
M = 3
seed = 752


J = GenerateJ(n,M,seed)

NEHNumeration = neh_mod(J)
# NEHNumeration = neh_modminCmax(J)
# NEHNumeration = neh(J)
NEHTasks = GetListOfTasks(J, NEHNumeration)

NEHCmax = CalculateCmax(NEHNumeration, J)
NEHC = EvaluateC(NEHTasks)
starts = start_t(NEHTasks,NEHC)
df = tasks_df(NEHNumeration,starts,NEHTasks)
print(df)
plot_schedule_fancy(NEHNumeration,starts,NEHTasks)

print("\n\n\n\n")
print("Permutacja naturalna     ", J)
print("kolejność zadań: ", NEHNumeration)
print("zadania:         ", NEHTasks)
print("Cmax2:       ", NEHCmax)
=======
from TestingEssentials import GenerateJ, GetListOfTasks, EvaluateC,plot_schedule_fancy, plot_schedule, start_t, tasks_df
from NEH import CalculateCmax, neh
from NEHmod import neh_mod, neh_modminCmax


n = 5
M = 3
seed = 752


J = GenerateJ(n,M,seed)

NEHNumeration = neh_mod(J)
# NEHNumeration = neh_modminCmax(J)
# NEHNumeration = neh(J)
NEHTasks = GetListOfTasks(J, NEHNumeration)

NEHCmax = CalculateCmax(NEHNumeration, J)
NEHC = EvaluateC(NEHTasks)
starts = start_t(NEHTasks,NEHC)
df = tasks_df(NEHNumeration,starts,NEHTasks)
print(df)
plot_schedule_fancy(NEHNumeration,starts,NEHTasks)

print("\n\n\n\n")
print("Permutacja naturalna     ", J)
print("kolejność zadań: ", NEHNumeration)
print("zadania:         ", NEHTasks)
print("Cmax2:       ", NEHCmax)
>>>>>>> f88f85437480cd7b1a0f5391407934fbbc6b1a8a:AlgorithmTest.py
print("C:            ", NEHC)