class Node(self,value):
    self.value = value
    self.next = None

class LinkedList(self):
    self.head = None
    self.tail = None
    self.length = 0

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_front(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

        #thank you stuffi
    #i hate living right about now, kill me

    