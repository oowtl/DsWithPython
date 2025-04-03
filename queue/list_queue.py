class ListQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.__queue[0]

    def is_empty(self):
        return len(self.__queue) == 0

    def dequeue_all(self):
        self.__queue.clear()

    def print_queue(self):
        print("Queue from front : ", end = ' ')
        for i in range(len(self.__queue)):
            print(self.__queue[i], end = ' ')
        print()
