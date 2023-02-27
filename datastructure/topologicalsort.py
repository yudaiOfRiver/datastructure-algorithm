import io
import sys
_INPUT = """\
6 6
0 1
1 2
3 1
3 4
4 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------#

from collections import deque, defaultdict

def topological_sort(A, in_deg):
    # A[i] : 頂点i からの到達可能集合
    # in_deg[i] : 頂点i の入次数
    V = len(A)

    topo_sort = [v for v in range(V) if in_deg[v] == 0]
    q = deque(topo_sort)

    while q:
        v = q.popleft()
        for next in A[v]:
            in_deg[next] -= 1
            if in_deg[next] == 0:
                q.append(next)
                topo_sort.append(next)

    return topo_sort


if __name__ == '__main__':
    V, E = map(int, input().split())
    A = defaultdict(list)
    in_deg = defaultdict(lambda : 0)
    for i in range(E):
        si, ti = map(int, input().split())
        A[si].append(ti)
        in_deg[ti] += 1
    print(topological_sort(A, in_deg))







