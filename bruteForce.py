def bruteForce(graph, s, V):
    vertex = []
    for i in range(V): # O(N)
        if i != s: # O(1)
            vertex.append(i) # O(1)
    min_path = maxsize # O(1)
    next_permutation=permutations(vertex) # O(N!)
    for i in next_permutation: # O(N)
        current_pathweight = 0 # O(1)
        k = s # O(1)
        for j in i:
            current_pathweight += graph[k][j] # O(1)
            k = j # O(1)
        current_pathweight += graph[k][s] # O(1)
        min_path = min(min_path, current_pathweight) # O(1)
		
    return min_path