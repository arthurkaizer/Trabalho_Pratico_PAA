from itertools import permutations
from mailbox import linesep
from math import sqrt
from sys import maxsize
from numpy import size

def distanceCalculate(cityA, cityB):
    A = cityA.split()
    B = cityB.split()
    return sqrt(pow((int(A[0])-int(B[0])),2)+pow((int(A[1])-int(B[1])),2))

def generateGraph(lines):
    graph = []
    for line in lines:
        distance = []
        for i in range(0,size(lines)):
            if(lines[i] != line):
                distance.append(distanceCalculate(line, lines[i]))
            else:
                distance.append(0)
        graph.append(distance)
    return graph

def readFile():
    file = open("input1.txt")
    lines = file.readlines()
    return lines

def bruteForce(graph, s, V):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
		
    return min_path

MAX = 999999

def dynamicPrograming(mask, pos, graph, dp,n, visited):
	if mask == visited:
		return graph[pos][0]
	if dp[mask][pos] != -1:
		return dp[mask][pos]
	
	ans = MAX 
	for city in range(0, n):
		if ((mask & (1 << city)) == 0):
			new = graph[pos][city] + dynamicPrograming(mask|(1<<city),city, graph, dp, n, visited)
			ans = min(ans, new)
	
	dp[mask][pos]=ans
	return dp[mask][pos]

def greedy(tsp):
    sum = 0
    counter = 0
    i = 0
    j = 0
    mn = 999999999
    visitedRouteList = {}
    visitedRouteList[0] = 1
    route = [0] *len(tsp)
    while i < len(tsp) and j < len(tsp[i]):
        if counter >= len(tsp[i]) - 1:
            break
        if j!=i and j not in visitedRouteList:
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
    for  j in range(0, len(tsp)):
        if i != j and tsp[i][j] < mn:
            mn = tsp[i][j]
            route[counter] = j + 1 
        
    sum += mn 
    return sum
    

resultados = list()
lines = readFile()
cityQuantity = int(lines.pop(0))
graph = generateGraph(lines)
sourceCity = 0
resultados.append(f'Travelled Distance (Brute Force) = {bruteForce(graph, sourceCity, cityQuantity)}\n')


visited = (1 << cityQuantity) - 1
r,c=16,4
dp = [[0]*c]*r
for i in range(0, (1<<cityQuantity)):
	for j in range(0, cityQuantity):
		dp[i][j] = -1
resultados.append(f'Travelled Distance (Dynamic Programming)= {dynamicPrograming(1, 0,graph, dp, cityQuantity, visited)}\n')
resultados.append(f'Travelled Distance (Greedy)= {greedy(graph)}\n')

arquivo = open("output1.txt", "a")
arquivo.writelines(resultados)


