import heapq

graph = {
    0: [(1, 10)],
    1: [(2, 1)],
    2: [(3, 1)],
    3: [(4, 2)],
    4: [(2, 1)],  
}


print(graph)


# Dijkstra algorithm is a greedy algorithm. It relies on a min heap to choose
# the next vertex, it does this by selecting the edge with the smallest distance u->v. 
# Where u->v was a previously added edge. Once it selects the edge and the new 
# vertex is added. We add the edges connecting to the neigthbors of that vertex to 
# the min heap. This steps repeat until there are no more edges to add and no more edges to select.

# Note that there will be cases were u-v was an edge mapping to a vertex(v) 
# that was already added. In those cases we will update the distance of dist[v] to new_dist =  dist[u] + u->v if new_dist < dist[v].


start = 0
h = []
for v, w in graph.get(start):
    h.append((w, (start,v)))
    
heapq.heapify(h)
dist = [float('inf')]*(len(graph))
visited = set()
dist[start] = 0
while h:
    # select the smallest one 
    wt, (u, v) = heapq.heappop(h)
    visited.add(v)
    # update distance if smaller path can be found 
    if dist[v] > dist[u] + wt:
        dist[v] = dist[u] + wt
        
    # add neigthbors 
    if graph.get(v):
        for z,w in graph.get(v):
            print('adding')
            if z not in visited: 
                heapq.heappush(h,(w, (v, z)))
    
    
        
print(dist)
        
    
    
    
    
    
    
    





