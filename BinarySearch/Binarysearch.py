class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class.
    class __Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right

        def getVal(self):
            return self.val

        def setVal(self,newval):
            self.val = newval

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self,newleft):
            self.left = newleft

        def setRight(self,newright):
            self.right = newright

        # This method deserves a little explanation. It does an inorder traversal
        # of the nodes of the tree yielding all the values. In this way, we get
        # the values in ascending order.
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self.val

            if self.right != None:
                for elem in self.right:
                    yield elem

    # Below are the methods of the BinarySearchTree class.
    def __init__(self):
        self.root = None

    def insert(self,val):
        self.root = BinarySearchTree.__insert(self.root,val)

    # This function is recursive and is not a passed a self parameter. It is a static
    # function (not a method of the class) but is hidden inside the class so users of
    # the class will not know it exists.

    def __insert(root,val):
        if root == None:
            return BinarySearchTree.__Node(val)

        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(),val))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(),val))

        return root
    
    def __getRightMost(root):
        while root.getRight()!=None:
            root= root.getRight()
        return root.getVal()    
            

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()
        
    def lookUp(self,val):
        return BinarySearchTree.__lookUp(self.root,val)
   
    def __lookUp(root,val):
        if root == None:
            return False
        if val==root.getVal():
            return True
        if val<root.getVal():
            return BinarySearchTree.__lookUp(root.getLeft(),val)
        else:
            return BinarySearchTree.__lookUp(root.getRight(),val)
        
        
    def delete(self,val):
        self.root= BinarySearchTree.__delete(self.root,val)
    
    # Recursive
    # It deletes val from the tree rooted at root
    # It returns the tree after deleting the val
    def __delete(root,val):
        if root == None:
            return None
            
        if val<root.getVal():
            root.setLeft(BinarySearchTree.__delete(root.getLeft(),val))
            
            
        elif val>root.getVal():
            root.setRight(BinarySearchTree.__delete(root.getRight(),val))
        else: # root.getVal() == val
            # Case 1
            if root.getRight()==None and root.getLeft()==None:
                return None
            
            # Case 2
            if root.getRight()==None:
                return root.getLeft()
            if root.getLeft()==None:
                return root.getRight()
            
            # Case 3
            newVal = BinarySearchTree.__getRightMost(root.getLeft())
            root.setVal(newVal)
            root.setLeft(BinarySearchTree.__delete(root.getLeft(),newVal))
        return root

                
            
        


def main():
    tree = BinarySearchTree()

    print("Binary search Tree Program ")
    print("............................")
    
    gettingInput=True
    while gettingInput:
        print("Make a choice")
        print("1. Insert into tree")
        print("2. delete from tree")
        print("3. Lookup value ")
        print("4. Exit")
        
        Choice= input("Choice?")
        if Choice=="1":
            #read a line of input
            val=input("insert?")
            
            #while there is more input
            while val!="":
                # Process the input
                tree.insert(val)
                
                
                # Read the next line of input
                val=input("insert?")
                
        elif Choice=="2":
            val=input("Value?")
            if val in tree:
                tree.delete(val)
                
                print(val,"has been deleted from the tree.")
            elif val not in tree:
                print(val,"was not in the tree.")
            
            
        elif Choice=="3":
            val=input("Value?")
            if tree.lookUp(val):

                print("Yes",val,"is in the tree")
            else:
                print("No",val,"is not in the tree")
        elif Choice=="4":
            return
        else:
            print("invalid Choice")
if __name__ == "__main__":
    main()