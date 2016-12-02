#include <iostream>

class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
  
def in_order_iterative(tree):
    node = tree
    stack = []
    condition = True

    while condition == True:
        if node != None:          #Traverses to the left most value on the tree while putting
            stack.append(node)    #every value it passes in the stack. Pops the left most value
            node = node.left      #and prints it. Checks if there is a value on the left. If not 
        else:                     #it pops the next value in the list and prints it. Check if there 
            if(len(stack) > 0):   #is a value to right again and continues to do this until the stack is
                node = stack.pop()#empty.
                print(node.value)
                node = node.right
            else:
                condition = False

def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right!=None):
        in_order(tree.right)

if __name__ == '__main__':
    
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
  print(" ")
  in_order_iterative(t)
