# 2D- Array: Water

N = int(input())
M = int(input())
A = [None] * N
for i in range(N):
    A[i] = [None] * M
    A[i] = list(map(int, input().split()))



# write your logic here
def DFS(self, start, visited):
         
        # Print current node
        print(start, end = ' ')
 
        # Set current node as visited
        visited[start] = True
 
        # For every node of the graph
        for i in range(self.v):
             
            # If some node is adjacent to the
            # current node and it has not
            # already been visited
            if (A.adj[start][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited)

