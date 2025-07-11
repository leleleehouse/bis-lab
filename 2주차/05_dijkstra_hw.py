import heapq

class Node:
    def __init__(self, vertex_no, d, heap_index):
        self.vertex_no = vertex_no
        self.d = d
        self.heap_index = heap_index
        
def dijstra(start, end, edge, vertex_count):
    start = int(start)
    end = int(end)
    dist = [float('inf')] * (vertex_count+1)
    visited = [False] * (vertex_count+1)
    prev = [None] * (vertex_count+1)
    
    dist[int(start)] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        current_dist , u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        visited[u] = True
        
        for v in range(1, vertex_count+1):
            if edge[u][v] != 0 and visited[v] != True:
                new_dist = current_dist + edge[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
                    heapq.heappush(pq, (new_dist, v))
                    
    if dist[end] == float('inf'):
        print(f"nowhere to go {end}")
        return
                    
    path = []
    current = end
    while current != None:
        path.append(current)
        current = prev[current]
        
    path.reverse()
    print(" ".join(map(str,path)))
                

if __name__ == '__main__':
    filename = './2주차/05_dijkstra_hw_input.txt'
    edge = [[0 for i in range(1000)] for _ in range(1000)]
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        v = list(map(int, lines[0].strip().split()))
        v_c = len(v)
        edges = lines[1].strip().split()
        for e in edges:
            a, b, w= map(int, e.split('-'))
            edge[a][b] = w
        
    while True:
        start = int(input('Start :'))
        end = int(input('End :'))

        dijstra(start, end, edge, v_c)
        re = input('Restart(Y/N):')
        
        if re.upper() == 'N':
            break
        
    