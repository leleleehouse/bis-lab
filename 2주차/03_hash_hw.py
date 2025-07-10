from math import floor

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    
class Hash:
    def __init__(self, size, A):
        self.table = [None] * size
        self.tsize = size
        self.A = A
        
    
    def hashfn(self, k):
        return floor(self.tsize * ((k * self.A) % 1))
    
    def insert(self, key):
        k = self.hashfn(key)
        n = self.table[k]
        while n:
            if n.data == key:
                return
            n = n.next
        
        new_node = Node(key)
        new_node.next = self.table[k]
        self.table[k] = n=new_node
        print(f"inserted : {key} in node{k}")
        
    def delete(self, key):
        k = self.hashfn(key)
        n = self.table[k]
        prev = None
        
        while n:
            if n.data == key:
                if prev:
                    prev.next = n.next
                else:
                    self.table[k] = n.next
                print(f"deleted : {key} in node{k}")
                return
            prev = n
            n = n.next
            
    def find(self, key):
        k = self.hashfn(key)
        n = self.table[k]
        while n:
            if n.data == key:
                print(f"found {key} : {k}")
                return
            n = n.next
        print("null")
        
    def print_table(self):
        for i in range(self.tsize):
            print(f"[{i}]:", end = ' ')
            n = self.table[i]
            if n == None:
                print("null")
            else:
                while n:
                    print(n.data, end = ' ')
                    n = n.next
                
                print()
                
if __name__ == '__main__':
    filename = './2주차/03_hash_hw_input.txt'
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    size = int(lines[0].strip())
    A = float(lines[1].strip())
    print(f"Hash Table Size: {size}")
    print(f"A : {A}")
    hstable = Hash(size, A)
    
    for line in lines[2:]:
        token = line.strip().split()

        if not token:
            continue
            
        cmd = token[0]
        
        if cmd == 'i':
            key = int(token[1])
            hstable.insert(key)
            
        elif cmd == 'd':
            key = int(token[1])
            hstable.delete(key)

        elif cmd == 'f':
            key = int(token[1])
            hstable.find(key)
        
        elif cmd == 'p':
            hstable.print_table()
            
        elif cmd == 'q':
            break
        
    