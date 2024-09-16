# The code is to find the spanning tree edges of unweighted graph from starting node-0

def add_edge(u,v,graph):
    graph[u].append(v)
    graph[v].append(u)
a=[[0,1],[0,3],[1,2],[2,3],[2,4],[4,5]]
dest=0
for i in a:
    if i[0]>dest:
        dest=i[0]
    if i[1]>dest:
        dest=i[1]
graph=[]
for i in range(dest+1):
    list1=[]
    graph.append(list1)
for l in a:
    add_edge(l[0],l[1],graph)
# printing the neighbouring nodes of each nodes
print(f'Neighbouring nodes of each nodes\n')
for i in range(len(graph)):
    print(f'{i}:{graph[i]}\n')
tree_edges=[] #to store spanning edges between the nodes
visited=[0]*(dest+1) # to check whether the node is visited or not (initialized to 0)


# defining the spanning tree function to find out by breadth-first search algorithm
def find_spanning_tree(v,visited,graph,tree_edges):
    visited[v]=1
    for n in graph[v]:

        if visited[n]==0:
            tree_edges.append((v,n))
            find_spanning_tree(n,visited,graph,tree_edges)

start_vertex=0
find_spanning_tree(start_vertex,visited,graph,tree_edges)
            
# printing spanning tree edges between nodes
print(f'Spanning tree edges between nodes\n')
for e in tree_edges:
    print(f'{e}')
