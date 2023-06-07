from TestingEssentials import EvaluateCmax, EvaluateC
N = [[1,2,3],[2,3,4],[4,5,6]]

def Bound2(_N):
    l = len(_N)
    m = len(_N[0])
    sums = []
    C = EvaluateC(_N)[-1]
    for i in range(m):
        times = [_N[n][i] for n in range(0,l)]
        sums.append(sum(times))
    print(C)

Bound2(N)