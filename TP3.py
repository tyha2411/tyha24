def create_adjacency_matrix(edges, n):
    matrix = [[0] * n for _ in range(n)]
    for edge in edges:
        u, v = edge[0]-1, edge[1]-1
        matrix[u][v] = 1
    return matrix

def get_children(adj_matrix, node):
    children = []
    for i in range(len(adj_matrix)):
        if adj_matrix[node-1][i] == 1:
            children.append(i+1)
    return children

def inorder_subtree(adj_matrix, x):
    def inorder_helper(node, visited):
        if node in visited:
            return []
        
        visited.add(node)
        result = []
        children = get_children(adj_matrix, node)
        
        if len(children) > 0:
            result.extend(inorder_helper(children[0], visited))
        result.append(node)
        if len(children) > 1:
            for child in children[1:]:
                result.extend(inorder_helper(child, visited))
        
        return result
    
    return inorder_helper(x, set())


if __name__ == "__main__":
    # graph
    edges = [(1,2), (1,3), (2,5), (2,6), (3,4), (4,8), (5,7)]
    n = 8  
    adj_matrix = create_adjacency_matrix(edges, n)

    x = int(input("Enter node label (1-8): "))
    if 1 <= x <= n:
        result = inorder_subtree(adj_matrix, x)
        print(f"Inorder traversal of subtree rooted at node {x}:", result)
    else:
        print("Invalid node label. The label must be in between 1 and 8")