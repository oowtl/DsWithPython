from queue.list_queue import ListQueue

if __name__ == '__main__':
    queue = ListQueue()
    queue.enqueue("Mon")
    queue.enqueue("Tue")
    queue.enqueue(123)
    queue.dequeue()
    queue.enqueue('aaa')
    queue.print_queue()
