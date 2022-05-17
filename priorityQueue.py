


class PriorityQueue:
    
    def __init__(self,is_numeric:bool) -> None:
        '''Constructor for priority Queue Class. 

        Args:
        - self: mandatory reference to this object.
        - elements: is_numeric: tells if data to be sorted is numeric number 

        Returns:
        None
        '''
        self.is_numeric_field = is_numeric
        self.queue = []

    def __str__(self) -> str:
        '''String Representation. 

        Args:
        - self: mandatory reference to this object.
        - elements: 

        Returns:
        String Representation for Queue Class 
        '''
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        '''Checks if queue is empty.. 

        Args:
        - self: mandatory reference to this object.
        - elements: 

        Returns:
        Boolean
        '''
        return len(self.queue) == 0

    def insert(self,data):
        '''Inserts data in queue.. 

        Args:
        - self: mandatory reference to this object.
        - elements: data

        Returns:
        None
        '''
        self.queue.append(data)

    def get(self):
        '''Gets data from the queue. 

        Args:
        - self: mandatory reference to this object.
        - elements: 

        Returns:
        Element from the queue
        '''
        return self.queue.pop()

    def delete(self):
        '''delete element from the queue. 

        Args:
        - self: mandatory reference to this object.
        - elements: 

        Returns:
        deleted item from the queue.
        '''
        try:
            maxIndex = 0
            for i in range(len(self.queue)):
                if self.is_numeric_field:
                    if float(self.queue[i].value) > float(self.queue[maxIndex].value):
                        maxIndex = i
                elif not self.is_numeric_field:
                    if (self.queue[i].value) > (self.queue[maxIndex].value):
                        maxIndex = i

            item = self.queue[maxIndex]
            del self.queue[maxIndex]
            return item
        except IndexError:
            print()
            exit()

#myQueue = PriorityQueue()

#myQueue.insert(1)
#myQueue.insert(5)
#myQueue.insert(9)
#myQueue.insert(2)
#myQueue.insert(4)
#print(myQueue)
#print(myQueue.delete())