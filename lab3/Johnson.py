from TestingEssentials import EvaluateCmax, GetListOfTasks
# Johnson:  FLM - first and last machine
#           przyjmuje:  _J - pozostałe zadania, 
#           zwraca:     pi - numeracja zadań z _J(nie lista zadań)
#   Uwaga:  Algorytm znajduje optymalne rozwiązanie tylko dla problemu z 2 maszynami,
#           Algorytm jest rozszerzony na wiecej maszyn 
#           (bierze pod uwagę pierwszą i ostatniną maszynę)

def JohnsonFLM(_J):     # Johnson, optymalny dla 2 maszyn, mozna zastosować dla wiekszej ilosci maszyn
    n = len(_J)  # Liczba zadań
    m = len(_J[0])  # Liczba maszyn
    l = 0  # Indeks dla zadania wpiętego na początek listy pi
    k = n - 1  # Indeks dla zadania wpiętego na koniec listy pi
    N = list(range(n))  # Zbiór zadań do przetworzenia
    pi = [0] * n  # Lista reprezentująca kolejność wykonywania zadań

    while N:
        min_pij = float('inf')  # ustatwiamy na inf aby móc znaleźć najmniejszą
        j_star, i_star = None, None  # Indeksy zadania i maszyny z najmniejszym czasem operacji
        # Szukamy indeksów zadania o najmniejszym czasie operacji na maszynie #OFTOP egzamin z optymalizacji jest przeniesiony na godzine 13 brbrber
        for j in N:
            for i in range(m):
                if _J[j][i] < min_pij:
                    min_pij = _J[j][i]
                    j_star = j
                    i_star = i
        # Dodawanie zadania do listy pi w odpowiedniej kolejności
        if _J[j_star][0] < _J[j_star][m - 1]:#bierzemy pod uwagę 1 i ostatnią maszynę
            pi[l] = j_star
            l += 1
        else:
            pi[k] = j_star
            k -= 1
        N.remove(j_star)  # Usunięcie zadania z zbioru N
    return pi

# Johnson:  VM - virtual machines
#           przyjmuje:  _J - pozostałe zadania, 
#           zwraca:     pi - numeracja zadań z _J(nie lista zadań)
#   Uwaga:  Algorytm znajduje optymalne rozwiązanie tylko dla problemu z 2 maszynami,
#           Algorytm jest rozszerzony na wiecej maszyn 
#           (tworzy 2 virtualne maszyny których wartość to suma z połowy maszyn)

def JohnsonVM(_J):     # Johnson, optymalny dla 2 maszyn, mozna zastosować dla wiekszej ilosci maszyn
    n = len(_J)  # Liczba zadań
    m = len(_J[0])  # Liczba maszyn
    l = 0  # Indeks dla zadania wpiętego na początek listy pi
    k = n - 1  # Indeks dla zadania wpiętego na koniec listy pi
    N = list(range(n))  # Zbiór zadań do przetworzenia
    pi = [0] * n  # Lista reprezentująca kolejność wykonywania zadań
    
    VM1Ind = (m+m%2)//2
    VM2Ind = (m)//2

    while N:
        min_pij = float('inf')  # ustatwiamy na inf aby móc znaleźć najmniejszą
        j_star = None  # Indeksy zadania i maszyny z najmniejszym czasem operacji
        # Szukamy indeksów zadania o najmniejszym czasie operacji na maszynie #OFTOP egzamin z optymalizacji jest przeniesiony na godzine 13 brbrber
        for j in N:
            for i in range(m):
                if _J[j][i] < min_pij:
                    min_pij = _J[j][i]
                    j_star = j
        
        # print(_J[j_star][:VM1Ind], _J[j_star][VM2Ind:])
        VM1 = sum(_J[j_star][:VM1Ind])
        VM2 = sum(_J[j_star][VM2Ind:])

        # Dodawanie zadania do listy pi w odpowiedniej kolejności
        if VM1 < VM2:   #bierzemy pod uwagę virtualne maszyny
            pi[l] = j_star
            l += 1
        else:
            pi[k] = j_star
            k -= 1
        N.remove(j_star)  # Usunięcie zadania z zbioru N
    return pi

def JohnsonCmax(_J):
    JFLMTasksNumeration = JohnsonFLM(_J)
    JFLMTasks = GetListOfTasks(_J, JFLMTasksNumeration)
    return EvaluateCmax(JFLMTasks)
