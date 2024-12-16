### Part 1

* * * * *
1.  Write all required algorithms needed to sort a sequence of numbers using Heapsort Algorithms. Heap-sort requires two main operations: build a max heap and repeatedly extracting the largest element from the heap (the root). Build a max heap from the input array.

    -   For each element in the array (starting from the end):
        -   Swap the root of the heap (largest element) with the last element of the heap.
        -   Reduce the size of the heap by one.
        -   Restore the max heap property.

    ### **Required Helper Functions**

    1.  **Max-Heapify**:
        -   Ensures the max-heap property for a subtree rooted at a given node.
        -   If a node violates the heap property, swap it with its largest child and recursively apply the operation.
    2.  **Build-Max-Heap**:
        -   Converts an unsorted array into a max heap by applying the `Max-Heapify` operation to each non-leaf node.

    ```
    HEAP-SORT(A):
        BUILD-MAX-HEAP(A)
        for i = A.length downto 2:
            swap A[1] and A[i]
            A.heap_size = A.heap_size - 1
            MAX-HEAPIFY(A, 1)

    BUILD-MAX-HEAP(A):
        A.heap_size = A.length
        for i = floor(A.length / 2) downto 1:
            MAX-HEAPIFY(A, i)

    MAX-HEAPIFY(A, i):
        left = 2 * i
        right = 2 * i + 1
        largest = i

        if left <= A.heap_size and A[left] > A[largest]:
            largest = left

        if right <= A.heap_size and A[right] > A[largest]:
            largest = right

        if largest != i:
            swap A[i] and A[largest]
            MAX-HEAPIFY(A, largest)

    ```

2.  Analyze in detail the written algorithm in part a.

    | **Function** | **Operation** | **Complexity** |
    | --- | --- | --- |
    | HEAP-SORT(A) | Sort array using heap | O( (n log⁡ n)+((n-1)(log n)) |
    | BUILD-MAX-HEAP(A) | Build a max heap | O(n log n) |
    | MAX-HEAPIFY(A, i) | Maintain max-heap property for a subtree | O(log⁡ n) |

    ```
    MAX-HEAPIFY(A, i):
        left = 2 * i          ->1
        right = 2 * i + 1     ->1
        largest = i           ->1

        if left <= A.heap_size and A[left] > A[largest]:   ->1
            largest = left    ->1

        if right <= A.heap_size and A[right] > A[largest]: ->1
            largest = right   ->1

        if largest != i:                     ->1
            swap A[i] and A[largest]         ->1
            MAX-HEAPIFY(A, largest)          ->log(n)

    ```

    ```
    BUILD-MAX-HEAP(A):
        A.heap_size = A.length    ->1
        for i = floor(A.length / 2) downto 1:  ->(n/2)
            MAX-HEAPIFY(A, i)   ->(n/2)*(log n)

    ```

    ```
    HEAP-SORT(A):
        BUILD-MAX-HEAP(A)
        for i = A.length downto 2: ->n
            swap A[1] and A[i]     ->n-1
            A.heap_size = A.heap_size - 1  ->n-1
            MAX-HEAPIFY(A, 1)       ->(n-1)log(n)

    ```



### Part 2

* * * * *

### Write all required algorithms needed to find MST using Kruskal's Algorithm.

### **Steps in Kruskal's Algorithm**

1.  Sort all edges of the graph by their weights in ascending order.
2.  Initialize an empty set for the MST.
3.  Use a Union-Find (Disjoint Set) data structure to check if adding an edge forms a cycle:
    -   If adding the edge does not form a cycle, add it to the MST.
    -   Otherwise, skip the edge.

### **Pseudocode**

1.  **Kruskal's Algorithm**

```

KRUSKAL(G):
    Input: G = (V, E), a graph with vertices V and edges E
    Output: MST, the Minimum Spanning Tree of G

    SORT E by weight in ascending order
    Initialize MST = {}
    Initialize a Union-Find data structure UF for all vertices in V

    for each edge (u, v) in E (in sorted order):
        if UF.FIND(u) ≠ UF.FIND(v):   // Check if u and v are in different sets
            MST.add((u, v))           // Add edge to MST
            UF.UNION(u, v)            // Merge sets of u and v

    return MST

```

1.  **Union-Find Data Structure**
    -   **Find**: Determines which subset a particular element is in.
    -   **Union**: Joins two subsets into a single subset.

```
UNION-FIND:
    MAKE-SET(x):
        Create a new set containing x
        Parent[x] = x
        Rank[x] = 0

    FIND(x):
        if Parent[x] ≠ x:
            Parent[x] = FIND(Parent[x])  // Path compression
        return Parent[x]

    UNION(x, y):
        rootX = FIND(x)
        rootY = FIND(y)
        if rootX ≠ rootY:
            if Rank[rootX] > Rank[rootY]:
                Parent[rootY] = rootX
            else if Rank[rootX] < Rank[rootY]:
                Parent[rootX] = rootY
            else:
                Parent[rootY] = rootX
                Rank[rootX] = Rank[rootX] + 1

```

* * * * *

### **Part (b): Analyze the Algorithms**

### **1\. Sorting the Edges**

-   Sorting all edges by weight takes $O(E\log{E})$, where E is the number of edges in the graph.

### **2\. Union-Find Operations**

-   Each `FIND` operation takes $O(α(V))$, where $α(V)$ is the inverse Ackermann function (a very slow-growing function, essentially constant for practical purposes).
-   Each `UNION` operation also takes $O(α(V)).$

### **3\. Kruskal's Algorithm**

-   For each edge, we perform `FIND` twice and possibly one `UNION`, leading to $O(E⋅α(V))$ for all edges.

### **Total Time Complexity**

-   Sorting edges: $O(E\log{E})$
-   Union-Find operations: $O(E⋅α(V))$
-   Total complexity: $O(E\log{E})$, since $α(V)$ is effectively constant.

* * * * *

