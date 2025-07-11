
def topological_sort(vertex, edge):
    n = len(vertex)
    inDeg = [0]*(1000)
    
    for i in vertex:
        for j in vertex:
            if edge[i][j] > 0:
                inDeg[j] +=1
                
    vlist = []
    for i in vertex:
        if inDeg[i]==0:
            vlist.append(i)
     
    
    vlist.sort()
    
    while len(vlist) > 0:
        v = vlist.pop(0)
        print(v, end = ' ')

        for u in vertex:
            if v!=u and edge[v][u]>0:
                inDeg[u] -=1
                if inDeg[u] == 0:
                    vlist.append(u)
    
    
if __name__ == '__main__':
    filename = './2주차/04_topological_hw_input.txt'
    edge = [[0 for i in range(1000)] for _ in range(1000)]
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        v = list(map(int, lines[0].strip().split()))
        edges = lines[1].strip().split()
        for e in edges:
            a,b = map(int, e.split('-'))
            edge[a][b] = 1 
            
    topological_sort(v,edge)
        
        
        