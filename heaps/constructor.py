class Heap:
    def __init__(self):
        self.heap = []
    
    def left_child(self,value):
        return 2*value+1
    def right_child(self,value):
        return 2*value+2
    def parent(self,value):
        return (value-1)//2
    def swap(self,v1,v2):
        self.heap[v1],self.heap[v2] = self.heap[v2],self.heap[v1]

    def insert(self,value):
        self.heap.append(value)
        current= len(self.heap)-1
        # just reverse the lesser sign to greater than sign for max heap
        while current>0 and self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current,self.parent(current))
            current = self.parent(current)
        return True
    def remove(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        #or max_val for max_heap
        min_val= self.heap[0]
        self.heap[0]=self.heap.pop()
        self.sink_down(0)

    def sink_down(self,index):
        min_index=index
        left=self.left_child(index)
        right=self.right_child(index)
        if left < len(self.heap) and self.heap[left]<self.heap[min_index]:
            min_index=left
        if right< len(self.heap) and self.heap[right]<self.heap[min_index]:
            min_index=right
        if min_index!=index:
            self.swap(index,min_index)
            self.sink_down(min_index)

bruh=Heap()
bruh.insert(1)
bruh.insert(30)
bruh.insert(23)
bruh.insert(15)
bruh.insert(17)
bruh.insert(25)
bruh.remove()
print(bruh.heap)
