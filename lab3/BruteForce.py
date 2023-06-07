from TestingEssentials import EvaluateCmax
import copy 

# BruteForce:   
#               przyjmuje:  _J zbiór wszystkich zadań
#               zwraca:     BestCmax - najlepszy możliwy czas Cmax wykonywania dla danego zbioru _J
#      Uwaga:   algorytm drzewiasty o bardzo dużej złożoności obliczeniowej (O(n!)), 
#               nie dawać dużego n i M

def BruteForce(_J):     
    BestCmax = float('inf')
    for j in _J:
        BranchCmax, BranchPi = ProcedureBruteForce(_J,j,[])
        if BestCmax > BranchCmax:
            BestCmax = BranchCmax
            BestPi = copy.deepcopy(BranchPi)
    return BestCmax, BestPi


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
    BestCmax = float('inf')
    if N:
       for j in N:
            BranchCmax, BranchPi = ProcedureBruteForce(N,j,pi)
            if BestCmax > BranchCmax:
                BestCmax = BranchCmax
                BestPi = copy.deepcopy(BranchPi)
    else:
        Cmax = EvaluateCmax(pi)
        return Cmax, pi
    return BestCmax, BestPi