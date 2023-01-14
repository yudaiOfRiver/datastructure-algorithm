from collections import defaultdict

class UnionFind():

    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

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
    n = 9
    uf = UnionFind(n)
    uf.unite(1, 2)
    uf.unite(2, 5)
    uf.unite(5, 9)
    uf.unite(3, 6)
    uf.unite(4, 7)
    uf.unite(7, 8)

    print(uf.find(1))
    print(uf.find(4))

    print(uf.same(1, 2))
    print(uf.same(1, 3))
    print(uf.root)
    print(uf.rank)
