


from priority_queue import PriorityQueue


class Node:

    def __init__(self, film = None, genre = None, LeadStudio = None, imbd = None, year = None) -> None:
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
        self.root = node
        self.last = node

    def findLowestNode(self, node:Node, value):
        if float(node.value) > float(value):
            return node
        elif (node.parent != None):
            return self.findLowestNode(node.parent, value)
        return None 

    def getRoot(self):
        return self.root 

    def addNode(self,row, index):
        
        newNode = Node(row[0],row[1],row[2],row[3],row[4])
        newNode.value = row[index]
        
        if self.root.value == 0:
            self.root = newNode
            self.last = newNode
            return 
     
        max_Node = self.findLowestNode(self.last,row[index])

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
        
        if (currentNode == None):
            return 
        self.inorderTraversal(currentNode.left)
        print(currentNode.value, end = " ")
        self.inorderTraversal(currentNode.right)

    def deleteNode(self):
        pass

    #def find_max_node(self, node:Node, value):
#
    #    if node.value > value:
    #        return node
    #    elif node.parent != None:
    #        return self.find_max_node(node.parent,value)
    #    else:
    #        return None
        
    def priorityQueue_Sorting(self, is_max, top):
        
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