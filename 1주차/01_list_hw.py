class Node:
    def __init__(self, id, name):
        self.pre = None
        self.next = None
        self.id = id
        self.name = name
        
class Linked_list:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.head = None
        self.position = 0
        
    def isEmpty(self):
        if (self.size == 0):
            print('리스트가 비어있습니다.')
        return self.size == 0
    
    def isFull(self):
        if(self.size == self.max_size):
            print(f'최대 학생수({self.max_size})가 다 찼습니다.')
        return self.size == self.max_size
    
    def isHere(self, id):
        n = self.head
        while n != None:
            if(n.id == id):
                return True
            n = n.next
        
        else:
            return False
        
    def findPosition(self, id):
        #position 0부터 시작
        n = self.head
        e_position = 0
        while(n != None  and n.id != id  ):
            n = n.next
            e_position += 1
        
        if(n.id == id):
            return e_position
        else:
            return -1
        
    def findElement(self, id):
        n = self.head
        while n != None :
            if(n.id == id):
                return n.name
            n = n.next
       
        print(f'Find failed : {id} is not in the list')
        
        
             
    def isLast(self, e_position):
        return self.size == e_position+1
        
        
    def delete(self, id):
        if not self.isHere(id):
            print(f'Deletion failed : element {id} is not in the list')
            return
        
        n = self.head
            
        while(n != None and n.id != id ):
            n = n.next
        
        if n is None:
            return
        
        # 삭제할 노드가 head 인 경우
        if n.pre is None:
            self.head = n.next
            if self.head != None:
                self.head.pre = None

        # 삭제할 노드가 head가 아닌 경우
        else:
            n.pre.next = n.next
            if n.next != None:
                n.next.pre = n.pre
            
        self.size -= 1
        print(f'Deletion Success : {id}')
                    
    def insert(self, id, name):
        if self.isFull():
            print(f'Insertion failed : list is full')
            return
            
        if self.isHere(id):
            print(f'There already is an element with key {id}. Insertion failed')
            return
        
        new = Node(id, name)
        
        if self.head is None:
            self.head = new
            self.size += 1
            print(f'Insertion Success : {id}')
            return
        
        if id < self.head.id:
            
            new.next = self.head
            self.head.pre = new
            self.head = new
            self.size +=1
            print(f'Insertion Success : {id}')
            return
            
        else:
            n = self.head
            while n.next != None and n.next.id < id:
                n = n.next
            
            new.next = n.next
            if n.next != None:
                n.next.pre = new
            n.next = new
            new.pre = n
            self.size += 1
            print(f'Insertion Success : {id}')
            return
        
    def printList(self):
        result = []
        n = self.head
        while n != None:
            result.append(f'{n.id} {n.name}')
            n = n.next
        print("Current List : " + '  '.join(result))
                    
if __name__ == '__main__':
    linked_list = Linked_list(max_size = 300)
    filename = './1주차/01_list_hw_input.txt'
    
    with open(filename, 'r') as f:
        for line in f:

            token = line.strip().split()
            # print(token)
            
            if token == None:
                continue
            
            cmd = token[0]
            
            if cmd == 'i':
                student_id = int(token[1])
                student_name = ' '.join(token[2:])
                linked_list.insert(student_id, student_name)
                linked_list.printList()
                
            if cmd == 'd':
                student_id = int(token[1])
                linked_list.delete(student_id)
                linked_list.printList()
                
            if cmd == 'f':
                student_id = int(token[1])
                student_name = linked_list.findElement(student_id)
                print(f'student_id({student_id}): {student_name}')
                
            if cmd == 'p':
                linked_list.printList()
                
