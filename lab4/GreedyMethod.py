from TestingEssentials import EvaluateCmax
import copy 

# BruteForce:   
#               przyjmuje:  _J zbiór wszystkich zadań
#               zwraca:     BestPenalty - najlepszy możliwy czas Cmax wykonywania dla danego zbioru _J
#      Uwaga:   algorytm drzewiasty o bardzo dużej złożoności obliczeniowej (O(n!)), 
#               nie dawać dużego n i M

def GreedyMethod(_J):     
    N = copy.deepcopy(_J)
    N.sort(key=lambda x: x[2])
    return N


