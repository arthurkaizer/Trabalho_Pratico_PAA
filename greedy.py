def greedy(tsp):
    sum = 0 # O(1)
    counter = 0 # O(1)
    i = 0 # O(1)
    j = 0 # O(1)
    mn = 999999999 # O(1)
    visitedRouteList = {} # O(1)
    visitedRouteList[0] = 1 # O(1)
    route = [0] *len(tsp) # O(1)
    while i < len(tsp) and j < len(tsp[i]): # O(N)
        if counter >= len(tsp[i]) - 1:# O(1)
            break
        if j!=i and j not in visitedRouteList: # O(N)
            if tsp[i][j] < mn:
                mn = tsp[i][j]
                route[counter] = j + 1
        j += 1
        if j == len(tsp[i]):
            sum += mn 
            mn = 999999999 
            visitedRouteList[route[counter] - 1] = 1 
            j = 0 
            i = route[counter] - 1 
            counter += 1
    
    i = route[counter - 1] - 1 
    for  j in range(0, len(tsp)): # O(N)
        if i != j and tsp[i][j] < mn: # O(1)
            mn = tsp[i][j] # O(1)
            route[counter] = j + 1 # O(1)
        
    sum += mn # O(1)
    return sum