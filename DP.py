MAX = 999999

def dynamicPrograming(mask, pos, graph, dp,n, visited):
	if mask == visited: # O(1)
		return graph[pos][0]
	if dp[mask][pos] != -1: # O(1)
		return dp[mask][pos]
	
	ans = MAX # O(1)
	for city in range(0, n): # O(N)
		if ((mask & (1 << city)) == 0): # O(1)
			new = graph[pos][city] + dynamicPrograming(mask|(1<<city),city, graph, dp, n, visited) # O(N*2^N)
			ans = min(ans, new) # O(1)
	
	dp[mask][pos]=ans # O(1)
	return dp[mask][pos]