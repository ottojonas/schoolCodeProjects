class Queue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.queue = self.createArray(maxSize)
        self.head = self.tail = -1

    def createArray(self, maxSize):
        return [None] * maxSize

    def enqueue(self, item):
        if self.isFull():
            return "Queue is full"
        else:
            self.tail = (self.tail + 1) % self.maxSize
            self.queue[self.tail] = item
            if self.head == -1:
                self.head = self.tail
            return "Enqueued"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            temp = self.queue[self.head]
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.maxSize
            return temp

    def isFull(self):
        return (self.tail + 1) % self.maxSize == self.head

    def isEmpty(self):
        return self.head == -1


class CircularQueue(Queue):
    def __init__(self, maxSize):
        super().__init__(maxSize)
        self.numberOfItems = 0
        self.maxSize = maxSize

    def circularEnqueue(self, data, maxSize):
        if self.numberOfItems == maxSize:
            print("Queue is full")
        else:
            self.enqueue()
            self.numberOfItems += 1

    def circularDequeue(self):
        if self.head == -1:
            print("Circular Queue is empty\n")
        else:
            self.dequeue()
            self.numberOfItems = -1

    def circularIsFull(self):
        return self.isFull()

    def ciruclarIsEmpty(self):
        return self.isEmpty()

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head + 1
        else:
            return self.maxSize - (self.head - self.tail - 1)


myQueue = Queue(3)
myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")
myQueue.enqueue("D")
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())

circleQueue = CircularQueue(3)
circleQueue.circularEnqueue("A")
circleQueue.circularEnqueue("B")
circleQueue.circularEnqueue("C")
circleQueue.circularEnqueue("D")
print(circleQueue.circularDequeue())
print(circleQueue.circularDequeue())
print(circleQueue.circularDequeue())
print(circleQueue.circularDequeue())
