from circular_linked_list.circular_linked_list import CircularLinkedList


class LinkedQueue:
    def __init__(self):
        self.__queue = CircularLinkedList()

    def enqueue(self, item):
        return self.__queue.append(item)

    def dequeue(self):
        return self.__queue.pop(0) # 첫 번째 요소 삭제 후 반환

    def front(self):
        return self.__queue.get(0) # 첫 번째 요소 반환

    def is_empty(self):
        return self.__queue.is_empty()

    def dequeue_all(self):
        return self.__queue.clear()

    def print_queue(self):
        print("Queue from front : ", end=" ")
        for i in range(self.__queue.size()):
            print(self.__queue.get(i), end=" ")
        print()