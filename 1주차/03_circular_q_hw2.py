class circular_q:
    def __init__(self, capacity):
        self.capacity = capacity+1
        self.array = [None]*self.capacity
        self.rear = 0
        self.front = 0
        self.qsize = 0
        
        
    def isEmpty(self):
        return self.rear == self.front
    
    def isFull(self):
        return self.front == (self.rear+1)%self.capacity
    
    def enqueue(self, e):
        if self.isFull():
            print('Circular Queue is Full')
        else:
            self.rear = (self.rear+1)%self.capacity
            self.array[self.rear] = e
            self.qsize += 1
            print(f'enqueue element: {e}')
            
    def dequeue(self):
        if self.isEmpty():
            print('Circular Queue is Empty')
        else:
            self.front = (self.front + 1) % self.capacity
            e = self.array[self.front]
            self.qsize -= 1
            print(f'dequeue element: {e}')
            return e
            
    def printFirst(self):
        if self.isEmpty():
            print('Circular Queue is Empty')
        else:
            e = self.array[self.front + 1]
            print(f'first element is {e}')
    
    def printRear(self):
        if self.isEmpty():
            print('Circular Queue is Empty')
        else:
            e = self.array[self.rear]
            print(f'rear element is {e}')
            
    def makeEmpty(self):
        if self.isEmpty():
            print('Circular Queue is already Empty')
        else:
            self.array = [None]*self.capacity
            self.qsize = 0
            self.rear = 0
            self.front = 0
            
    
    def deleteQueue(self):
        self.capacity = 0
        self.array = None
        self.rear = None
        self.front = None
           
if __name__ == '__main__':
    
    filename = './1주차/03_circular_q_hw2_input.txt'
    with open(filename, 'r') as f:
        for line in f:
            token = line.strip().split()
            # print(token)
            
            if not token:
                continue
            
            cmd = token[0]
            
            if cmd == 'n':
                size = int(token[1])
                cq = circular_q(size)
                print(f'create size is {size} queue')
            
            if cmd == 'e':
                e = int(token[1])
                cq.enqueue(e)
                
            
            if cmd == 'd':
                e = cq.dequeue()
                    
            
            if cmd == 'f':
                cq.printFirst()
            
            if cmd == 'r':
                cq.printRear()
                
                
                