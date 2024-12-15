class Edge:
    def __init__(self, u, v, weight):
        self.u = u  
        self.v = v  
        self.weight = weight


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].weight <= right[j].weight:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(edges):
    if len(edges) <= 1:
        return edges

    mid = len(edges) // 2
    left = merge_sort(edges[:mid])
    right = merge_sort(edges[mid:])

    return merge(left, right)


def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])  
    return parent[vertex]


def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


def kruskal(vertices, edges):
   
    sorted_edges = merge_sort(edges)

    
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    mst = []  
    mst_weight = 0


    for edge in sorted_edges:
        u, v, weight = edge.u, edge.v, edge.weight

       
        if find(parent, u) != find(parent, v):
            mst.append(edge)
            mst_weight += weight
            union(parent, rank, u, v)

    return mst, mst_weight

if __name__ == "__main__":
   
    n_v = int(input("Enter the number of vertices: "))
    vertices = []
    print("Enter the vertices (e.g., 0, 1, 2):")
    for _ in range(n_v):
        vertex = int(input())
        vertices.append(vertex)

   
    n_e = int(input("Enter the number of edges: "))
    edges = []
    print("Enter the edges in the format: source destination weight")
    for _ in range(n_e):
        u, v, weight = map(int, input().split())
        edges.append(Edge(u, v, weight))

   
    mst, mst_weight = kruskal(vertices, edges)

    print("Edges in the Minimum Spanning Tree:")
    for edge in mst:
        print(f"({edge.u}, {edge.v}) - Weight: {edge.weight}")

    print(f"Total weight of MST: {mst_weight}")
