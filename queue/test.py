from queue.linked_queue import LinkedQueue
from queue.list_queue import ListQueue

if __name__ == '__main__':
    queue = ListQueue()
    queue.enqueue("Mon")
    queue.enqueue("Tue")
    queue.enqueue(123)
    queue.dequeue()
    queue.enqueue('aaa')
    queue.print_queue()

    print("===")
    print("===")
    print("===")

    linked_queue = LinkedQueue()
    linked_queue.enqueue("Mon")
    linked_queue.enqueue("Tue")
    linked_queue.enqueue(123)
    linked_queue.enqueue("Wed")
    linked_queue.dequeue()
    linked_queue.enqueue('aaa')
    linked_queue.print_queue()
