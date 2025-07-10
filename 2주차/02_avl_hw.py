class AVLNode:
    def __init__(self, key, value= None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
        
class AVLTree:
    def __init__(self):
        pass
    
    def getHeight(self, node):
        if node is None:
            return -1
        return node.height
    
    def updateHeight(self, node):
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) +1
    
    def heightDiff(self, n):
        if n == None:
            return 0
        return self.getHeight(n.left) - self.getHeight(n.right)
        
    def singleRotateWithLeft(self, A): #LL
        B = A.left
        if B == None:
            return A
        A.left = B.right
        B.right = A
        self.updateHeight(A)
        self.updateHeight(B)
        return B
    
    def singleRotateWithRight(self, A): #RR
        B = A.right
        if B == None:
            return A
        A.right = B.left
        B.left = A
        self.updateHeight(A)
        self.updateHeight(B)
        return B
    
    def doubleRotateWithLeft(self, A): #RL
        B = A.right
        if B == None:
            return A
        A.right = self.singleRotateWithLeft(B)
        return self.singleRotateWithRight(A)
    
    def doubleRotateWithRight(self, A): #LR
        B = A.left
        if B == None:
            return A
        A.left = self.singleRotateWithRight(B)
        return self.singleRotateWithLeft(A)
    


    def avlInsert(self, root, node):
        if root == None:
            return node
        
        if node.key == root.key:
            return root
        
        if node.key < root.key:
            root.left = self.avlInsert(root.left, node)
        elif node.key > root.key:
            root.right = self.avlInsert(root.right, node)
        else:
            return root
    
        self.updateHeight(root)
        diff = self.heightDiff(root)
        
        if diff > 1 and node.key < root.left.key:
            return self.singleRotateWithLeft(root)
            
        if diff > 1 and node.key > root.left.key:
                return self.doubleRotateWithRight(root)
            
        if diff < -1 and node.key > root.right.key:
            return self.singleRotateWithRight(root)
    
        if diff < -1 and node.key < root.right.key:
            return self.doubleRotateWithLeft(root)

        return root
    
    def printInOrder(self, n):
        if n != None:
            self.printInOrder(n.left)
            print(n.key, end = ' ')
            self.printInOrder(n.right)
    
if __name__ == '__main__':
    filename = './2주차/02_avl_hw_input.txt'
    tree = AVLTree()
    root = None
    
    with open(filename, 'r') as f:
        for line in f:
            tokens = line.strip().split()

            if not tokens:
                continue
            
            for token in tokens:
                key = int(token)
                node = AVLNode(key)
                root = tree.avlInsert(root, node)
                
                print(f"\nheight: {root.height}")
                tree.printInOrder(root)
            
            