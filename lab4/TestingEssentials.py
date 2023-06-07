from RandomNumberGenerator import RandomNumberGenerator
import copy 

    
def GenerateJ(_n,_seed):     # Generuje nam J wypełnione _n zadaniami na _M maszyn z ziarnem _seed
    rng = RandomNumberGenerator(_seed)
    n = _n
    Lines = []
    J = []
    Lines.append([rng.nextInt(1, 29) for _ in range(n)])
    A = sum(Lines[0])
    X = 29 #A
    Lines.append([rng.nextInt(1, 9) for _ in range(n)])
    Lines.append([rng.nextInt(1, X) for _ in range(n)])
    Lines.append([i for i in range(1,1+n)])
    for i in range(len(Lines[0])):
        J.append([Lines[j][i] for j in range(4)])
    return J

def EvaluateC(_J):           # Oblicza nam C dla kolejności zadań w podanym _J
    n = len(_J)
    C = []

    C.append(_J[0][0])
    for i in range(1,n):
        C.append(_J[i][0]+C[i-1]) # Obliczamy czasy zakończenia
    return C

def EvaluateCmax(_J):           # Oblicza nam Cmax dla kolejności zadań w podanym _J,
    C = EvaluateC(_J)
    return C[-1]   # Cmax to będzie czas zakończenia ostatniego zadania

# def EvaluateCmax(C):           # Oblicza nam Cmax dla kolejności zadań w podanym _J,
#     return C[-1]   # Cmax to będzie czas zakończenia ostatniego zadania

def EvalPenalty(_J):     # Oblicza nam liste kar dla danej kolejnosci zadań
    C = EvaluateC(_J)
    WD = []
    for i in range(len(C)): 
        WD.append(max(C[i]-_J[i][2],0)*_J[i][1])
    return sum(WD)
