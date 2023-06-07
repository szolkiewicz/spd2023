from NEH import CalculateCmax

# def cirt_path(_pi, _J):
#     n = len(_pi)
#     m = len(_J[0])
#     completionTimes = [[0] * (m + 1) for _ in range(n)]
#     tasks = [[0] * (m + 1) for _ in range(n)]
#     for i in range(n):
#         for j in range(1, m + 1):
#             job = _J[_pi[i] - 1][j - 1]
#             longer = max(completionTimes[i][j - 1], completionTimes[i - 1][j])
#             if longer == completionTimes[i - 1][j]:
            
#             else:
            
#             completionTimes[i][j] = longer + job
            

#     return completionTimes[n - 1][m]

def neh_mod(_J):
    n = len(_J)  # liczba zadań

    # Obliczanie sum czasów dla każdego zadania
    taskTimes = [(i + 1, sum(_J[i])) for i in range(n)]
    taskTimes.sort(key=lambda x: x[1], reverse=True)  # Sortowanie malejąco
    _pi = [taskTimes[0][0]]  # Inicjalizacja kolejności zadań
    totalTime = CalculateCmax(_pi, _J)
    print(_pi)
    print(totalTime)
    print("Best:    ", _pi)
    
    for i in range(1, n):
        minTotalTime = float('inf')
        best = -1

        for j in range(i + 1):
            _pi.insert(j, taskTimes[i][0])
            totalTime = CalculateCmax(_pi, _J)
            if totalTime < minTotalTime:
                minTotalTime = totalTime
                best = j

            _pi.remove(taskTimes[i][0])
        _pi.insert(best, taskTimes[i][0])

        ind = [a for a in range(i + 1)]
        ind.remove(best)
        print("\n")
        print("search")
        print(_pi)
        minTotalTime = float('inf')
        best2 = -1
        for j in ind:

            task = _pi.pop(j)
            totalTime = CalculateCmax(_pi, _J)
            print(totalTime," ",_pi," ",task)
            if totalTime < minTotalTime:
                minTotalTime = totalTime
                best2 = j
            _pi.insert(j,task)
        print("\n")
        print(task," Fit:")
        task = _pi.pop(best2)
        print("\n")
        minTotalTime = float('inf')
        for j in range(i + 1):
            _pi.insert(j, task)
            totalTime = CalculateCmax(_pi, _J)
            print(totalTime," ",_pi," ",j)
            if totalTime < minTotalTime:
                minTotalTime = totalTime
                best = j

            _pi.remove(task)
        _pi.insert(best,task)
        print(CalculateCmax(_pi, _J)," ",best)

    print("Best:    ", _pi)
    return _pi

def neh_modminCmax(_J):
    n = len(_J)  # liczba zadań

    # Obliczanie sum czasów dla każdego zadania
    taskTimes = [(i + 1, sum(_J[i])) for i in range(n)]
    taskTimes.sort(key=lambda x: x[1], reverse=True)  # Sortowanie malejąco
    _pi = [taskTimes[0][0]]  # Inicjalizacja kolejności zadań
    totalTime = CalculateCmax(_pi, _J)
    print(_pi)
    print(totalTime)
    print("Best:    ", _pi)
    
    for i in range(1, n):
        minTotalTime = float('inf')
        best = -1

        for j in range(i + 1):
            _pi.insert(j, taskTimes[i][0])
            totalTime = CalculateCmax(_pi, _J)
            if totalTime < minTotalTime:
                minTotalTime = totalTime
                best = j

            _pi.remove(taskTimes[i][0])
        _pi.insert(best, taskTimes[i][0])

        ind = [a for a in range(i + 1)]
        ind.remove(best)
        print("\n")
        print("search")
        print(_pi)
        minTotalTime = float('inf')
        best2 = -1
        for j in ind:

            task = _pi.pop(j)
            totalTime = CalculateCmax(_pi, _J)
            print(totalTime," ",_pi," ",task)
            if totalTime < minTotalTime:
                minTotalTime = totalTime
                best2 = j
            _pi.insert(j,task)
        print("\n")
        print(task," Fit:")
        task = _pi.pop(best2)
        print("\n")
        minTotalTime = float('inf')
        for j in range(i + 1):
            _pi.insert(j, task)
            totalTime = CalculateCmax(_pi, _J)
            print(totalTime," ",_pi," ",j)
            if totalTime < minTotalTime:
                minTotalTime = totalTime
                best = j

            _pi.remove(task)
        _pi.insert(best,task)
        print(CalculateCmax(_pi, _J)," ",best)

    print("Best:    ", _pi)
    return _pi