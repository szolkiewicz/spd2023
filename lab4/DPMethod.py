import copy 

def DP(_J):

    J = _J.copy()
    n = len(J)
    mask = (1 << n)

    memory = [-1 for _ in range(mask)]
    memory[0] = 0
    for D in range(1,mask):
        TimeSum = 0
        for i in range(0,n):
            if D & (1<<i):
                TimeSum += J[i][0]
        MinPenalty = float('inf')
        for i in range(0,n):
            if D & (1<<i):
                Penalty = max(TimeSum - J[i][2] ,0)* J[i][1] + memory[D ^ (1<<i)]
                MinPenalty = min(MinPenalty, Penalty)
        memory[D] = MinPenalty
    return memory[mask-1]

def DPmod(_J): #to wyzej jest mega git, tu cos grzebie do zrobienia backtrackingu

    J = _J.copy()
    n = len(J)
    depth = 0
    mask = (1 << n)

    memory = [-1 for _ in range(mask)]
    memory[0] = 0

    BestMoves = [0 for _ in range(mask)]
    for D in range(1,mask):
        TimeSum = 0
        depth = 0
        for i in range(0,n):
            if D & (1<<i):
                TimeSum += J[i][0]
                depth += 1

        MinPenalty = float('inf')
        for i in range(0,n):
            if D & (1<<i):
                SubCollectionAddr = D ^ (1<<i)
                Penalty = max(TimeSum - J[i][2] ,0)* J[i][1] + memory[SubCollectionAddr]
                if MinPenalty > Penalty:
                    MinPenalty = Penalty
                    PrevBestMove = [i + 1, SubCollectionAddr]
                    
                    

        memory[D] = MinPenalty
        BestMoves[D] = PrevBestMove
    return memory[mask-1], BestMoves

def Backtrack(BestMoves):
    i = len(BestMoves)-1
    tasks = []
    while i != 0:
        tasks.append(BestMoves[i][0])
        i = BestMoves[i][1]
    tasks.reverse()
    return tasks

