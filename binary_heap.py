class BinaryHeap:

    def __init__(self):
        self._nodes = list()

    def _parent(self, i):
        """
        Return the index of the parent of the node at index i.
        """
        return (i-1)//2

    def _lchild(self,i):
        """
        Return the index of the left child of the node at index i.
        """
        return (2*i)+1

    def _rchild(self,i):
        """
        Return the index of the right child of the node at the index i.
        """
        return (2*i)+2

    def _fix_heap_up(self, i):
        """
        Recursively fix the heap property along the i-root path.
        
        Efficiency: O(log(n)) where n = number of nodes in heap.
        Since the number of items at max is 2^height. We're only accessing 1 node per height per
        iteration.
        h = max height
        h-1 = heights we actually reach
        # nodes at level i
            for 0 <= i <h is 2^i
        therefore n => sum (h-1, i = 0) w^i = 2^h - 1
        so 2^n <= n+1 or h<= log2(n+1)
        
        """
        while i > 0:
            par = self._parent(i)
            if self._nodes[par][1] <= self._nodes[i][1]:
                return
            self._nodes[par], self._nodes[i] = self._nodes[i], self._nodes[par]
            i = par

    def add(self,item,key):
        """
        Add the item with the given key to the binary heap.
        
        
        >>> h = BinaryHeap()
        >>> h.add("A", 3)
        >>> h.add("B", 1)
        >>> h.add("C", 4)
        >>> h._nodes[0] == ["B", 1]
        True
        >>> h.add("D", 0)
        >>> h._nodes[0] == ["D", 0]
        True
        
        """

        self._nodes.append([item, key])
        self._fix_heap_up(len(self._nodes)-1)

    def _fix_heap_down(self,i):
        """
        Recursively fix the heap property between i and its children.
        """
        while True:
            lchil = self._lchild(i)
            if lchil >= len(self._nodes):
                return
            rchil = self._rchild(i)
            if rchil >= len(self._nodes) or self._nodes[lchil][1] <= self._nodes[rchil][1]:
                min_child = lchil
            else:
                min_child = rchil
            if self._nodes[min_child][1] >= self._nodes[i][1]:
                return
            self._nodes[min_child], self._nodes[i] = self._nodes[i], self._nodes[min_child]
            i = min_child


    def pop_min(self):
        """
        Remove and return a minimum-key item in the heap.
        
        Efficiency: O(log n) where n is the number of items in the heap.
        
        >>> h = BinaryHeap()
        >>> h.add("A", 3)
        >>> h.add("B", 1)
        >>> h.add("C", 4)
        >>> h.pop_min() == ['B', 1]
        True
        >>> h.pop_min() == ["A", 3]
        True
        >>> h.add("D",0)
        >>> h.pop_min() == ["D", 0]
        True
        >>> h.pop_min() == ["C", 4]
        True
        >>> h._nodes == []
        True
        """
        
        if len(self._nodes) == 0:
            raise IndexError("pop from an empty binary heap")
        
        min_item = self._nodes[0]
        self._nodes[0] = self._nodes[-1]
        self._nodes.pop()
        self._fix_heap_down(0)

        return min_item

    def __len__(self):
        return len(self._nodes)
