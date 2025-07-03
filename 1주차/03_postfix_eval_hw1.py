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
    
def postfifx_eval(expr):
    s = Stack(100)
    for token in expr:
        if token in '*/+-%':
            val2 = s.pop()
            val1 = s.pop()
            if token == '*': s.push(val1* val2)
            elif token == '/': s.push(val1/val2)
            elif token == '%': s.push(val1%val2)
            elif token == '+': s.push(val1+val2)
            elif token == '-': s.push(val1-val2)
        else:
            s.push(float(token))
    
    return s.pop()

                
    
if __name__ == '__main__':
    stack = Stack(max_size = 300)
    filename = './1주차/03_postfix_eval_hw1_input.txt'
    
    with open(filename, 'r') as f:
        for line in f:
            expr = ''
            for char in line.strip():
                if char == '#':
                    result = postfifx_eval(expr)
                    print(f'converted postfix form: {expr}')
                    print(f'evaluation result: {result}\n')
                    expr = ''
                else:
                    expr += char
                
            
         