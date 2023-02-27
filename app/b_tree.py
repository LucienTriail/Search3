class BTree:
    class Node:
        def __init__(self, t):
            self.keys = []
            self.values = []
            self.leaf = True
            # t is the order of the parent B-Tree. Nodes need this value to define max size and splitting
            self._max_keys = 2 * t - 1

        def split(self, parent, payload):
            new_node = self.__class__(parent._max_keys // 2)
            mid_key, mid_val = self.keys[self._max_keys // 2], self.values[self._max_keys // 2]

            # update parent
            self.keys.pop(self._max_keys // 2)
            self.values.pop(self._max_keys // 2)
            parent.keys.insert(payload, mid_key)
            parent.values.insert(payload, mid_val)
            parent.children.insert(payload + 1, new_node)

            # update children
            new_node.values = self.values[self._max_keys // 2 + 1 :]
            new_node.keys = self.keys[self._max_keys // 2 + 1 :]
            self.values = self.values[: self._max_keys // 2]
            self.keys = self.keys[: self._max_keys // 2]
            if not self.leaf:
                new_node.children = self.children[self._max_keys // 2 + 1 :]
                self.children = self.children[: self._max_keys // 2 + 1]

            return parent

    def __init__(self, t=2):
        self._t = t
        if self._t <= 1:
            raise ValueError("B-Tree must have a degree of 2 or more.")
        self._root = self