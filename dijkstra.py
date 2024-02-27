graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

infinite = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinite

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed_nodes = []

def find_lower_cost_node(graph):
	lower_cost = infinite
	lower_cost_node = None
	for node in graph:
		if graph[node] < lower_cost and node not in processed_nodes:
			lower_cost = graph[node]
			lower_cost_node = node
	return lower_cost_node

def dijkstra(graph): 
	node = find_lower_cost_node(costs)
	while node is not None:
		cost = costs[node]
		neighbors = graph[node]
		for n in neighbors.keys():
			new_cost = cost + neighbors[n]
			if costs[n] > new_cost:
				costs[n] = new_cost
				parents[n] = node
		processed_nodes.append(node)
		node = find_lower_cost_node(costs)

dijkstra(graph)

print(costs)
print(parents)

























