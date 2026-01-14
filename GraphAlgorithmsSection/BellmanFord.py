
V = 5
edges = [[0,1,5], [1,2,1],[1,3,2], [2,4,1],[4,3,-1]]
src = 0

V = len(edges)
dist  = [float('inf')]*(V)
print(dist)
def bellmanFord(V, edges, src):
    dist[src] = 0
    for i in range(V):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            if dist[u] != float('inf') and dist[u]  + w < dist[v]:
                if i == V -1:
                    return -1
                dist[v] = dist[u] + w

    return dist


print("Bellman Ford")
print(bellmanFord(V, edges,0))
