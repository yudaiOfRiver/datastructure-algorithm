class heap:
    
    def __init__(self, heap=None) -> None:
        self.heap = []
        for c in heap:
            self.insert(c)
                
    def insert(self,value):
        self.heap.append(value)
        ind = len(self.heap)-1
        if len(self.heap) >= 2:
            while self.heap[ind] < self.heap[(ind-1)//2]:
                self.heap[ind], self.heap[(ind-1)//2] = self.heap[(ind-1)//2], self.heap[ind]
                ind = (ind-1)//2
                #print(self.heap[(ind-1)//2])        
        return heap

    def get_min(self):
        min = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        i = 0


my_list = [1, 5, 9, 7, 6, 10, 11, 8, 9]
my_heap = heap(my_list)
my_heap.insert(4)
print(my_heap.heap)
