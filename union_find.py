from collections import defaultdict

class UnionFind():
    def __init__(self, n) -> None:
        ## if 正 : そのノードの根
        ## if 負 : 根であり、絶対値は要素数を表す
        self.n = n
        self.root = [-1] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.root[x] > self.root[y]:
            x, y = y, x

        self.root[x] += self.root[y]
        self.root[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())

    def group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

if __name__ == '__main__':
    ufb = UnionFind(5)
    ufb.union(3, 4)
    ufb.union(2, 3)
    ufb.union(0, 1)




