from collections import deque, defaultdict


def topologicalsort(A): # A : 出を1, 入を-1で表現した隣接行列
    V = len(A)
    deg = defaultdict(lambda: 0) # deg[v] : 頂点 v に到達できる頂点数
    G = defaultdict(list)        # G[v]   : 頂点v から到達できる頂点集合

    for i in range(V):
        for j in range(V):
            if i != j and A[i][j] == -1:
                deg[i] += 1
            if i != j and A[i][j] == 1:
                G[i].append(j)


    ans = list(v for v in range(V) if deg[v]==0)
    deq = deque(ans)
    used = [0]*V

    while deq:
        v = deq.popleft()
        for t in G[v]:
            deg[t] -= 1
            if deg[t]==0:
                deq.append(t)
                ans.append(t)

    return ans

A = [[1, -1, 0, 1], [1, 1, 1, 0], [0, -1, 1, 1], [-1, 0, -1, 1]]

print(topologicalsort(A))










