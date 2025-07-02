class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data


class Stack:
    def __init__(self, max_size):
        self.top = None
        self.size = 0
        self.max_size = max_size
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.max_size
    
    def push(self, e):
        if self.isFull():
            print('스택 가득 참')
            return
        new = Node(e) 
        if self.isEmpty():
            self.top = new
            self.size+=1
            
        else:
            new.next = self.top
            self.top = new
            self.size+=1
        
    def pop(self):
        if self.isEmpty():
            print('스택에 아무것도 없음')
            return
        
        e = self.top
        self.top = self.top.next
        self.size -= 1
        return e.data
    
    def gettop(self):
        return self.top.data
   
def pre(e):
    if e in '*/%':
        return 2
    elif e in '+-':
        return 1
    else:
        return -1
    
def infixTopostfix(line):
    result = []
    
    s = Stack(100)
    
    for i in line:
        if i not in '-+/*()%': 
            result.append(i)
        
        elif i == '(':
            s.push(i)
        
        elif i == ')':
            while not s.isEmpty():
                e = s.pop()
                if e == '(':
                    break
                result.append(e)
        
        elif i in '-+/*%':
            while not s.isEmpty() and pre(i) <= pre(s.gettop()):
                result.append(s.pop())
                    
            s.push(i)
       

        
    while not s.isEmpty():
        result.append(s.pop())
        
    return result
                
    
if __name__ == '__main__':
    stack = Stack(max_size = 300)
    filename = './1주차/02_stack_q_hw_input.txt'
    
    with open(filename, 'r') as f:
        for line in f:
            expr = ''
            for char in line.strip():
                if char == '#':
                    postfix = infixTopostfix(expr)
                    postfix = ''.join(postfix)
                    print(f'orifinal infix form: {expr}')
                    print(f'converted posrfix form: {postfix}\n')
                    expr = ''
                else:
                    expr += char
                
            
         