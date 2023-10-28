class UF: #union-find
    def __init__(self, n):
        self.id = list(range(0, n+1))

    def union(self, i, j):
        self.id[j] = i

    def connected(self, i, j):
        while self.id[j] != j:
            j = self.id[j]
            if self.id[j] == self.id[i]:
                return True

        return False

# Q: We can only seem to traverse up the tree, how do we arrange so we can traverse in both directions? Is there a name for this?

class WUF: #weighted union-find
    def __init__(self, n):
        self.id = list(range(0, n+1))
        self.sz = [1] * (n + 1)

    def union(self, i, j):
        root_i = self.root(i)
        root_j = self.root(j)
        if self.sz[root_i] > self.sz[root_j]:
            self.id[root_j] = self.id[root_i]
            self.sz[root_i] += self.sz[root_j]
        else:
            self.id[root_i] = self.id[root_j]
            self.sz[root_j] += self.sz[root_i]

    def root(self, x):
        while self.id[x] != x:
            x = self.id[x]
        return x

    def connected(self, i, j):
        if self.id[j] == j and self.id[i] != i:
            return self.connected(j, i) # enable reverse traversal

        while self.id[j] != j:
            j = self.id[j]
            if self.id[j] == self.id[i]:
                return True

        return False

#graph = UF(5)
#print(graph.connected(5, 2))

################## extras ####################
class WUF: #weighted union-find - get largest connected element in find method
    def __init__(self, n):
        self.id = list(range(0, n + 1))
        self.sz = [1] * (n + 1)

    def union(self, i, j):
        root_i = self.root(i)
        root_j = self.root(j)
        if self.sz[root_i] > self.sz[root_j]:
            self.id[root_j] = self.id[root_i]
            self.sz[root_i] += self.sz[root_j]
        else:
            self.id[root_i] = self.id[root_j]
            self.sz[root_j] += self.sz[root_i]

    def root(self, x):
        while self.id[x] != x:
            x = self.id[x]
        return x

    def connected(self, i, j):
        if self.id[j] == j and self.id[i] != i:
            return self.connected(j, i) # enable reverse traversal

        while self.id[j] != j:
            j = self.id[j]
            if self.id[j] == self.id[i]:
                return True

        return False

    #find highest value in connected elements
    def find(self, i):
        highest = i
        while self.id[i] != i:
            i = self.id[i]
            if i > highest:
                highest = i
        return highest

graph = WUF(5)
graph.union(0, 3)
graph.union(0, 2)
graph.union(0, 4)
print(graph.find(2))