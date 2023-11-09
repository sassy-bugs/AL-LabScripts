V = 5
answer = []

def travellingSalesmanProblem(graph, v, currPos, n, count, cost):

	if (count == n and graph[currPos][0]):
		answer.append(cost + graph[currPos][0])
		return

	for i in range(n):
		if (v[i] == False and graph[currPos][i]):
			
			v[i] = True
			travellingSalesmanProblem(graph, v, i, n, count + 1, 
				cost + graph[currPos][i])
			
			v[i] = False

if __name__ == '__main__':
	n = 5
	graph= [[0, 80, 100000, 25, 55], 
		     [80, 0, 30, 100000, 20],
			 [100000, 30, 0, 65, 15], 
			 [25, 100000, 65, 0, 100000], 
			 [55, 20, 15, 100000, 0]]

	visited = [False for i in range(n)]
	
	visited[0] = True

	travellingSalesmanProblem(graph, visited, 0, n, 1, 0)

	print(min(answer))