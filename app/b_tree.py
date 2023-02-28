class BTreeNode:
    def __init__(self, t, leaf=True):
        self.t = t
        self.keys = []
        self.values = []
        self.children = []
        self.leaf = leaf

    def split_child(self, i, y):
        z = BTreeNode(t=self.t, leaf=y.leaf)
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys[self.t - 1])
        self.values.insert(i, y.values[self.t - 1])
        z.keys = y.keys[self.t:]
        z.values = y.values[self.t:]
        y.keys = y.keys[:self.t - 1]
        y.values = y.values[:self.t - 1]
        if not y.leaf:
            z.children = y.children[self.t:]
            y.children = y.children[:self.t]

    def insert_non_full(self, k, v):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            self.values.append(None)
            while i >= 0 and self.keys[i] > k:
                self.keys[i + 1] = self.keys[i]
                self.values[i + 1] = self.values[i]
                i -= 1
            self.keys[i + 1] = k
            self.values[i + 1] = v
        else:
            while i >= 0 and self.keys[i] > k:
                i -= 1
            if len(self.children[i + 1].keys) == 2 * self.t - 1:
                self.split_child(i + 1, self.children[i + 1])
                if self.keys[i + 1] < k:
                    i += 1
            self.children[i + 1].insert_non_full(k, v)

    def search(self, k):
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1
        if i < len(self.keys) and k == self.keys[i]:
            return self.values[i]
        elif self.leaf:
            return None
        else:
            return self.children[i].search(k)

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                yield from self.children[i].traverse()
            yield self.keys[i]

        if not self.leaf:
            yield from self.children[-1].traverse()

    def get_range(self, start, end):
        i = 0
        result = []
        while i < len(self.keys) and self.keys[i] < start:
            i += 1
        if i < len(self.keys):
            if not self.leaf:
                result.extend(self.children[i].get_range(start, end))
            while i < len(self.keys) and self.keys[i] <= end:
                result.append(self.values[i])
                i += 1
            if not self.leaf and i == len(self.keys):
                result.extend(self.children[-1].get_range(start, end))
        return result


class BTree:
    def __init__(self, t=2):
        self.t = t
        self.root = None

    def search(self, k):
        result = self.root.search(k) if self.root else None
        if isinstance(result, int):
            result = [result]
        return result

    def insert(self, k, v):
        print("insert Btree")
        if not self.root:
            self.root = BTreeNode(t=self.t, leaf=True)
            self.root.keys.append(k)
            self.root.values.append(v)
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                s = BTreeNode(t=self.t, leaf=False)
                s.children.append(self.root)
                s.split_child(0, self.root)
                i = 0 if s.keys[0] < k else 1
                s.children[i].insert_non_full(k, v)
                self.root = s
            else:
                self.root.insert_non_full(k, v)

    def traverse(self):
        if self.root:
            return self.root.traverse()
        else:
            return iter([])