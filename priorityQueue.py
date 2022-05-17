


class PriorityQueue:
    
    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self,data):
        self.queue.append(data)

    def get(self):
        return self.queue.pop()

    def delete(self):
        try:
            maxIndex = 0
            for i in range(len(self.queue)):
                if self.queue[i].value > self.queue[maxIndex]:
                    maxIndex = i
            item = self.queue[maxIndex]
            del self.queue[maxIndex]
            return item
        except IndexError:
            print()
            exit()

myQueue = PriorityQueue()

myQueue.insert(1)
myQueue.insert(5)
myQueue.insert(9)
myQueue.insert(2)
myQueue.insert(4)
print(myQueue)
print(myQueue.delete())