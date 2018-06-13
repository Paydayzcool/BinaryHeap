MIN_HEAP = 0
MAX_HEAP = 1

class BinaryHeap:
    def __init__(self, items, heap_type=MIN_HEAP):
        self.heapType = heap_type
        self.heap = items

        if self.heapType == MIN_HEAP:
            self.buildMinHeap()

    def getLeft(self, index):
        return 2 * index + 1

    def getRight(self, index):
        return 2 * (index + 1)

    def getParent(self, index):
        return (index - 1) // 2
    
    def leftExists(self, index):
        return self.getLeft(index) < len(self.heap)

    def rightExists(self, index):
        return self.getRight(index) < len(self.heap)

    def parentExists(self, index):
        return self.getParent(index) >= 0

    def swap(self, p, q):
        k = self.heap[p]
        self.heap[p] = self.heap[q]
        self.heap[q] = k

    # Return the root item of the heap
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    # Return and remove the root node of the heap.
    def poll(self):
        item = self.heap[0]
        self.heap[0] = self.heap.pop(-1)
        self.heapifyDown()
        return item

    def insert(self, item):
        self.heap.append(item)
        self.heapifyUp()

    def heapifyUp(self):
        index = len(self.heap) - 1
        while self.parentExists(index) and self.heap[self.getParent(index)] > self.heap[index]:
            self.swap(self.getParent(index), index)
            index = self.getParent(index)

    def heapifyDown(self):
        index = 0

        while self.leftExists(index):
            smaller = self.getLeft(index)
            if (self.rightExists(index) and self.getRight(index) < self.getLeft(index)):
                 smaller = self.getRight(index)

            if self.heap[index] < self.heap[smaller]:
                break;
            else:
                self.swap(smaller, index)
                index = smaller

    def buildMinHeap(self):
        for i in range((len(self.heap)-2)//2,-1,-1):
            self.minHeapify(i)
            
    def minHeapify(self, index):
        # There cannot be a right branch without a left branch, but there can be a left branch without a right branch.
        if self.rightExists(index):
            # Check branches
            k = min(self.heap[self.getLeft(index)], self.heap[self.getRight(index)])
            if k < self.heap[index]:
                if k == self.heap[self.getRight(index)]:
                    self.swap(self.getRight(index), index)
                    self.minHeapify(self.getRight(index))
                else:
                    self.swap(self.getLeft(index), index)
                    self.minHeapify(self.getLeft(index))
        elif self.leftExists(index):
            if self.heap[self.getLeft(index)] < self.heap[index]:
                self.swap(self.getLeft(index), index)
                self.minHeapify(self.getLeft(index))
    # ------ Extra Functionalities ------

    def heapSort(self):
        pass
