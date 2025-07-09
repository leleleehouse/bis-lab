class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def findNode(self, n, key):
        if n == None:
            return None
        elif key == n.key:
            return n
        elif key < n.key:
            return self.findNode(n.left, key)
        else:
            return self.findNode(n.right, key)
            
    def insertNode(self, root, n):
        if self.findNode(self.root, n.key):
            print(f'Element {n.key} already exist')
            return self.root
        if root == None:
            return n
        
        if n.key == root.key:
            return root
        
        if n.key < root.key:
            root.left = self.insertNode(root.left, n)
        
        else:
            root.right = self.insertNode(root.right, n)
            
        return root
    
    def searchMin(self, root):
        while root != None and root.left != None:
            root = root.left
            
        return root
    
    def searchMax(self, root):
        while root != None and root.right != None:
            root = root.right
            
        return root
    
    def deleteNode(self,root, key):
        if root == None:
            return root
        
        if key < root.key:
            root.left = self.deleteNode(root.left, key)
        elif key > root.key:
            root.right = self.deleteNode(root.right, key)
            
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                tmp = self.searchMax(root.left)
                root.key = tmp.key
                root.value = tmp.value
                root.left = self.deleteNode(root.left, tmp.key)
                
        return root
    
    def printPreOrder(self, n):
        if n != None:
            print(n.key, end = ' ')
            self.printPreOrder(n.left)
            self.printPreOrder(n.right)
            
    def printInOrder(self, n):
        if n != None:
            self.printInOrder(n.left)
            print(n.key, end = ' ')
            self.printInOrder(n.right)

    def printPostOrder(self, n):
        if n != None:
            self.printPostOrder(n.left)
            self.printPostOrder(n.right)
            print(n.key, end = ' ')
            
            
if __name__ == '__main__':
    filename = './2주차/01_bst_hw_input.txt'
    bst = BST()
    with open(filename, 'r') as f:
        for line in f:
            token = line.strip().split()

            if not token:
                continue
            
            cmd = token[0]
            
            if cmd == 'i':
                key = int(token[1])
                node = Node(value=key, key=key)
                bst.root = bst.insertNode(bst.root, node)
            
            elif cmd == 'd':
                key = int(token[1])
                if bst.findNode(bst.root, key):
                    bst.root = bst.deleteNode(bst.root, key)
                
                else:
                    print(f'Element {key} not found')
                    
            elif cmd == 'pi':
                bst.printInOrder(bst.root)
                print()
            elif cmd == 'pr':
                bst.printPreOrder(bst.root)
                print()
            elif cmd == 'po':
                bst.printPostOrder(bst.root)
                print()
                
            
            elif cmd == 'f':
                key = int(token[1])
                if bst.findNode(bst.root, key):
                    print(f'{key} is in the tree')
                else:
                    print(f'{key} is not in the tree')
                    
            

    