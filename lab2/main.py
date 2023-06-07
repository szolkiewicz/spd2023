from RandomNumberGenerator import RandomNumberGenerator

rng = RandomNumberGenerator(1)

n = 12
p = [rng.nextInt(1, 29) for _ in range(n)]
A = sum(p)
r = [rng.nextInt(1, A) for _ in range(n)]
X = A
#X = 29
q = [rng.nextInt(1, X) for _ in range(n)]

J = list(zip(r, p, q))
print(J)

J.sort(key=lambda x: x[0])

def eval(pi):
    S = [pi[0][0]]
    C = [S[0] + pi[0][1]]
    Cmax = C[0] + pi[0][2]
    for i in range(1, len(J)):
        S.append(max(pi[i][0], C[i - 1]))
        C.append(S[i] + pi[i][1])
        Cmax = max(Cmax,C[-1]+pi[i][2])
    return Cmax

def schrage(J):
    G = []
    pi = []
    N = sorted(J, key=lambda x: x[0])
    t = 0
    Cmax = 0
    while G or N:
        while N and N[0][0] <= t:
            j = N.pop(0)
            G.append(j)
        if G:
            j = max(G, key=lambda x: x[2])
            G.remove(j)
            pi.append(j)
            t += j[1] 
            Cmax = max(Cmax, t+j[2])
        else:
            t = N[0][0]
    return Cmax

def schragepmtn(J):
    G = []
    pi = []
    N = sorted(J, key=lambda x: x[0])
    t = N[0][0]
    l = (0,0,0)
    print(l)
    Cmax = 0
    while G or N:
        while N and N[0][0] <= t:
            j = N.pop(0)
            G.append(j)
            if j[2]>l[2]:
                l = list(l)
                l[1] = t-j[0]
                l = tuple(l)
                t = j[0]
                if l[1]>0:
                    G.append(l)
        if G:
            j = max(G, key=lambda x: x[2])
            G.remove(j)
            l = j
            t += j[1] 
            Cmax = max(Cmax, t+j[2])
        else:
            t = N[0][0]
    return Cmax

schrageCmax = schrage(J)
sPMTNCmax = schragepmtn(J)
print(schrageCmax,sPMTNCmax)