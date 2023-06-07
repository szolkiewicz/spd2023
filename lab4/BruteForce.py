from TestingEssentials import EvaluateCmax, EvalPenalty
import copy 

# BruteForce:   
#               przyjmuje:  _J zbiór wszystkich zadań
#               zwraca:     BestPenalty - najlepszy możliwy czas Cmax wykonywania dla danego zbioru _J
#      Uwaga:   algorytm drzewiasty o bardzo dużej złożoności obliczeniowej (O(n!)), 
#               nie dawać dużego n i M

def BruteForce(_J):     
    BestPenalty = float('inf')
    for j in _J:
        Penalty, BranchPi = ProcedureBruteForce(_J,j,[])
        if BestPenalty > Penalty:
            BestPenalty = Penalty
            BestPi = copy.deepcopy(BranchPi)
    return BestPenalty, BestPi


# Procedura BruteForce: 
#                       przyjmuje:  _J - pozostałe zadania, 
#                                   _j - przekładane zadanie, 
#                                   _pi - zadania (nie numeracje) ułożone w kolejności wykonywania.
#                       zwraca:     Cmax - najlepszy możliwy czas wykonywania Cmax dla danego rozgałęzienia lub liścia.
#                Uwaga:             algorytm drzewiasty o bardzo dużej złożoności obliczeniowej (O(n!)), 
#                                   nie dawać dużego n i M

def ProcedureBruteForce(_J,_j,_pi): 
    N = copy.deepcopy(_J)
    pi = copy.deepcopy(_pi)
    pi.append(_j)
    N.remove(_j)
    BestPenalty = float('inf')
    if N:
       for j in N:
            Penalty, BranchPi = ProcedureBruteForce(N,j,pi)
            if BestPenalty > Penalty:
                BestPenalty = Penalty
                BestPi = copy.deepcopy(BranchPi)
    else:
        Penalty = EvalPenalty(pi)
        return Penalty, pi
    return BestPenalty, BestPi