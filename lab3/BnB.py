from TestingEssentials import EvaluateCmax, EvaluateC, GetListOfTasks
from Johnson import JohnsonCmax, JohnsonFLM
import copy 

#wersja prosta: UB to bardzo dużo, LB to pierwszy lepszy wzorek
#Wersja na 5: UB szacujemy np johnsonem, LB to jakis konkretny wzorek tak aby złożoność obliczneniowa nie byla jeszcze bezsensownie duza i aby nie obcinało optymalnego rozwiązania (pewnie trzeba bedzie potestować)

#LB: Cmax w tej gałęzi nie będzie lepszy ( mniejszy ) niż LB
#UB: nie przeszukujemy gałęzi której LB jest większe niż UB
# Jeżeli LB < UB to rozwijamy tą gałąź

UB = float('inf')
piBest = []

# BnB:   
def BnB(_J):
    global UB 
    global piBest
    UB = JohnsonCmax(_J)
    for j in _J:
        ProcedureBnB(_J,j,[])
    if not piBest:
        piBest = GetListOfTasks(_J,JohnsonFLM(_J))
    return UB, piBest

# Procedura BnB: 
def ProcedureBnB(_J,_j,_pi): 
    global UB
    global piBest
    N = copy.deepcopy(_J)
    pi = copy.deepcopy(_pi)
    pi.append(_j)
    N.remove(_j)
    if N:
       LB = Bound1(pi,N)
       if LB < UB:
            for j in N:
                ProcedureBnB(N,j,pi)
    else:
        Cmax = EvaluateCmax(pi)
        if Cmax < UB:
            UB = Cmax
            piBest = pi


# Oszacowanie LB: 
def Bound0(_pi, _N):
    l = len(_N)
    m = len(_N[0])
    times = [_N[n][m-1] for n in range(0,l)]
    lb = EvaluateCmax(_pi) + sum(times)
    return lb

def Bound1(_pi, _N):
    l = len(_N)
    m = len(_N[0])
    sums = []
    Cmaxs = EvaluateC(_pi)[-1]
    for i in range(m):
        times = [_N[n][i] for n in range(0,l)]
        sums.append(sum(times)+Cmaxs[i])
    lb = max(sums)
    return lb