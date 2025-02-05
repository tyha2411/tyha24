from collections import defaultdict

class GraphComponents:
    def __init__(self, matrix):
        self.matrix = matrix
        self.V = len(matrix)
        
    def get_adjacency_lists(self, ignore_direction=False):
        """Convert matrix to adjacency lists, optionally ignoring edge directions"""
        adj = defaultdict(list)
        for i in range(self.V):
            for j in range(self.V):
                if self.matrix[i][j]:
                    adj[i].append(j)
                    if ignore_direction:
                        adj[j].append(i)
        return adj

    def dfs(self, v, visited, adj):
        """Depth-first search helper function"""
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, adj)

    def get_transpose(self):
        """Get transpose of the graph for Kosaraju's algorithm"""
        adj = defaultdict(list)
        for i in range(self.V):
            for j in range(self.V):
                if self.matrix[i][j]:
                    adj[j].append(i)
        return adj

    def fill_order(self, v, visited, stack, adj):
        """Fill vertices in stack according to their finishing times"""
        visited[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                self.fill_order(neighbor, visited, stack, adj)
        stack.append(v)

    def weakly_connected_components(self):
        """Find number of weakly connected components"""
        visited = [False] * self.V
        count = 0
        adj = self.get_adjacency_lists(ignore_direction=True)
        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited, adj)
                count += 1        
        return count

    def strongly_connected_components(self):
        """Find number of strongly connected components using Kosaraju's algorithm"""
        stack = []
        visited = [False] * self.V
        adj = self.get_adjacency_lists()
        
        for i in range(self.V):
            if not visited[i]:
                self.fill_order(i, visited, stack, adj)
        transpose_adj = self.get_transpose()
        visited = [False] * self.V
        count = 0
        while stack:
            v = stack.pop()
            if not visited[v]:
                self.dfs(v, visited, transpose_adj)
                count += 1
        return count

if __name__ == "__main__":
    G = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    graph = GraphComponents(G)
    weakly = graph.weakly_connected_components()
    strongly = graph.strongly_connected_components()
    print(f"Number of weakly connected components: {weakly}")
    print(f"Number of strongly connected components: {strongly}")