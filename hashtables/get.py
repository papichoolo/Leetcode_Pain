class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size
    
    def _hash(self,key):
        my_hash=0
        for letter in key:
            my_hash = (my_hash+ ord(letter)*23)% len(self.data_map)
            return my_hash
    def printer(self):
        for i,x in enumerate(self.data_map):
            print(i,': ',x)

    def set_item(self,key,value):
        index= self._hash(key)
        if self.data_map[index]== None:
            self.data_map[index]= []
        self.data_map[index].append([key,value])
    def get_item(self,key):
        index=self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None

myhash= HashTable()
myhash.set_item('bruh',5000)
myhash.set_item('xd',400)
myhash.set_item('lol',789)

print(myhash.get_item('lol'))
#myhash.printer()