


from priority_queue import PriorityQueue

class Node:

    def __init__(self, film = None, genre = None, LeadStudio = None, imbd = None, year = None) -> None:
        '''Constructor for the node class. 

        Value is initialized with 0, however, it will be set to the value that 
        will be sorted.

        Args:
        - self: mandatory reference to this object.
        - elements: the node is populated with these elements.

        Returns:
        None
        '''
        self.value = 0
        self.left = None
        self.right = None
        self.parent = None
        self.filmName = film
        self.genre = genre
        self.LeadStudio = LeadStudio
        self.Imbd = imbd


class CartesianTree:

    def __init__(self, node = Node()) -> None:
        '''Constructor for the Cartesian Tree class. 

        Args:
        - self: mandatory reference to this object.
        - elements: a empty node is set to root node. 

        Returns:
        None
        '''
        self.root = node
        self.last = node

    def findMaxNode(self, node:Node, value):
        '''Finds maximum node in the tree. 

        Args:
        - self: mandatory reference to this object.
        - elements: last node in the tree, value to compare.

        Returns:
        Node
        '''
        if float(node.value) > float(value):
            return node
        
        elif (node.parent != None):
            return self.findLowestNode(node.parent, value)
        
        return None 

    def getRoot(self) -> Node:
        '''Output the root node. 

        Args:
        - self: mandatory reference to this object.
        - elements: -

        Returns:
        Root Node.
        '''
        return self.root 

    def addNode(self,row, index):
        '''Adds new node to the cartesian tree. 

        Args:
        - self: mandatory reference to this object.
        - elements: row :(movies attribute), index: (refers to column number)
        
        Returns:
        None
        '''
        newNode = Node(row[0],row[1],row[2],row[3],row[4])
        newNode.value = row[index]
        
        if self.root.value == 0:
            self.root = newNode
            self.last = newNode
            return 
     
        max_Node = self.findMaxNode(self.last,row[index])

        if (max_Node == None):
            newNode.left = self.root
            self.root.parent = newNode
            self.root = newNode
        
        else:
            newNode.left = max_Node.right
            max_Node.right = newNode
            newNode.parent = max_Node

        self.last = newNode

    def inorderTraversal(self,currentNode:Node):
        '''Perform Inorder Traversal on the tree. 

        Args:
        - self: mandatory reference to this object.
        - elements: currentNode from which traversal begins.

        Returns:
        None
        '''
        if (currentNode == None):
            return 
        self.inorderTraversal(currentNode.left)
        print(currentNode.value, end = " ")
        self.inorderTraversal(currentNode.right)


    def priorityQueue_Sorting(self, is_max, top):
        '''Creates Priority Queue from the values in the tree.

        Args:
        - self: mandatory reference to this object.
        - elements: is_max : (tells ascending or descending order), top :(range of results)

        Returns:
        None
        '''        
        pq = PriorityQueue()
        sortedList = []
        tempNode = Node()
        pq.insert(self.root)
        
        while not pq.isEmpty():
            tempNode = pq.delete()
            sortedList.append(tempNode)
            
            if tempNode.left != None:
                pq.insert(tempNode.left)
            
            if tempNode.right != None:
                pq.insert(tempNode.right)

        if is_max == False:
            sortedList = sortedList[::-1]
        sub_sortedList = []
        
        for i in range(top):
            sub_sortedList.append(sortedList[i])
        return sub_sortedList




# tree = CartesianTree()
# tree.addNode(5)
# tree.addNode(7)
# tree.addNode(3)
# tree.addNode(13)
# tree.addNode(4)
# print(tree.getRoot())
# tree.inorderTraversal(tree.getRoot())