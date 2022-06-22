from itertools import permutations
from math import sqrt
from sys import maxsize
from numpy import size

global pathsTaken
pathsTaken = ""


def calcFactorial(fat):
    output = 1
    for i in range(1,fat+1):
        output *= i
    return output
def calcRam(qtd):
    return (2**qtd) /8/1024/1024


def distanceCalculate(cityA, cityB):
    A = cityA.split()
    B = cityB.split()
    return sqrt(pow((int(A[0]) - int(B[0])), 2) + pow((int(A[1]) - int(B[1])), 2))


def generateInput(qtd):
    output = []
    output.append(str(qtd)+"\n")
    i=1
    while(i<qtd*2):
        output.append(str(i)+" "+str(i+1)+"\n")
        i+=2
    i-=2
    output.pop(len(output)-1)
    output.append(str(i)+" "+str(i+1))
    return output

def generateGraph(lines):
    graph = []
    for line in lines:
        distance = []
        for i in range(0, size(lines)):
            if (lines[i] != line):
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
    global pathsTaken
    bolinha = 0
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        bolinha += 1
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            print("BF: "+str(k)+" "+str(j))
            pathsTaken += "BF: "+str(k)+" "+str(j)+"\n"
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    pathsTaken += "=======\n"
    return min_path


MAX = 999999


def dynamicPrograming(mask, pos, graph, dp, n, visited):
    global pathsTaken
    if mask == visited:
        return graph[pos][0]
    if dp[mask][pos] != -1:
        return dp[mask][pos]

    ans = MAX
    for city in range(0, n):
        if ((mask & (2**city)) == 0):
            print("DP: "+str(pos)+" "+str(city))
            pathsTaken += "DP: "+str(pos)+" "+str(city)+"\n"
            new = graph[pos][city] + dynamicPrograming(mask | (1 << city), city, graph, dp, n, visited)
            ans = min(ans, new)
    dp[mask][pos] = ans
    return dp[mask][pos]


def greedy(tsp):
    global pathsTaken
    pathsTaken += "=======\n"
    sum = 0
    counter = 0
    i = 0
    j = 0
    mn = 999999999
    visitedRouteList = {}
    visitedRouteList[0] = 1
    route = [0] * len(tsp)
    while i < len(tsp) and j < len(tsp[i]):
        print("GR: " + str(i) + " " + str(j))
        pathsTaken += "GR: " + str(i) + " " + str(j)+"\n"
        if counter >= len(tsp[i]) - 1:
            break
        if j != i and j not in visitedRouteList:
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
    for j in range(0, len(tsp)):
        if i != j and tsp[i][j] < mn:
            mn = tsp[i][j]
            route[counter] = j + 1

    sum += mn
    return sum


resultados = list()
lines = generateInput(256)    # Definir quantidade de cidades
cityQuantity = int(lines.pop(0))
graph = generateGraph(lines)
sourceCity = 0
if cityQuantity < 9:
    resultados.append(f'Travelled Distance (Brute Force) = {bruteForce(graph, sourceCity, cityQuantity)}\n')
else:
    resultados.append("Brute Force too slow to compute! It would take "+str(calcFactorial(cityQuantity))+" steps to complete.\n")

# 29 cidades = 4gb de ram
# 30 cidades = 8gb de ram
# 31 cidades = 16gb de ram
# ...

if cityQuantity < 31:
    visited = (2 ** cityQuantity) - 1
    r = 2 ** cityQuantity
    c = cityQuantity
    dp = [[-1] * c] * r
    resultados.append(
        f'Travelled Distance (Dynamic Programming)= {dynamicPrograming(1, 0, graph, dp, cityQuantity, visited)}\n')
else:
    resultados.append("Dynamic Programming too expensive to compute! It would need "+str(calcRam(cityQuantity))+" GB of ram to compute.\n")
resultados.append(f'Travelled Distance (Greedy)= {greedy(graph)}\n')

arquivo = open("output2.txt", "a")
arquivo.truncate(0)
arquivo.write(pathsTaken)
arquivo.writelines(resultados)