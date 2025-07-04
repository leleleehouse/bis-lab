
class MaxHeap:
    def __init__(self, capacity):
       self.capacity = capacity +1
       self.size = 0
       self.array = [None] * self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity-1
    
    def insert(self, e):
        if not self.isFull():
            self.size += 1 # 0인덱스는 사용안함
            self.array[self.size] = e
            current = self.size
            
            while current > 1:
                parent = current//2
                if(self.array[current] > self.array[parent]):
                    self.array[current], self.array[parent] = self.array[parent], self.array[current]
                    current = parent
                else:
                    break
                
            self.array[current] = e
            
        else:
            print('Insert: Max Heap is full')
                
    def deleteMax(self):
        if not self.isEmpty():
            parent = 1    
            child = 2   
            root = self.array[parent] 
            last = self.array[self.size]
            self.size -=1

            while child <= self.size:
                if child < self.size and self.array[child] < self.array[child+1]:
                    child += 1
                if last >= self.array[child]:
                    break
                self.array[parent] = self.array[child]
                parent = child
                child *=2
            
            self.array[parent] = last
            self.array[self.size+1] = None
            
            return root  
        else:
            print('Delete: Max Heap is empty')
        
    def levelprintHeap(self): 
        if not self.isEmpty():
            #레벨순회
            level = 0
            i =1
            while i <= self.size :
                count = 2**level
                line = self.array[i:i+count]
                print(' '.join(str(x) for x in line if x is not None)) 
                i += count
                level +=1
        else:
            print('Print: Max Heap is empty')
            
    def printHeap(self): 
        if not self.isEmpty():
            print(' '.join(str(self.array[i]) for i in range(1, self.size + 1)))
        else:
            print('Print: Max Heap is empty')
            
if __name__ == '__main__':
    filename = './1주차/04_binary_heap_hw_input.txt'
    
    with open(filename, 'r') as f:
        for line in f:
            token = line.strip().split()

            if not token:
                continue
            
            cmd = token[0]
            
            if cmd == 'n':
                size = int(token[1])
                heap = MaxHeap(size)
                print(f'create size is {size} heap')
            
            if cmd == 'i':
                e = int(token[1])
                heap.insert(e)
                
            
            if cmd == 'd':
                e = heap.deleteMax()
                    
            
            if cmd == 'p':
                heap.printHeap()
