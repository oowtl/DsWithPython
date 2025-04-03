from queue.list_queue import ListQueue
from stack.list_stack import ListStack


def is_palindrome(sentence) -> bool:
    s = ListStack()
    q = ListQueue()

    for i in range(len(sentence)):
        s.push(sentence[i])
        q.enqueue(sentence[i])

    while not q.is_empty() and s.pop() == q.dequeue():
        {}
    if q.is_empty():
        return True
    else:
        return False

def main():
    print("Palindrome Check!")

    str1 = 'lioninoil'
    t1 = is_palindrome(str1)
    print(str1, " is Palindrome?", t1)

    str2 = 'lionisnoil'
    t2 = is_palindrome(str2)
    print(str2, " is Palindrome?", t2)

if __name__ == '__main__':
    main()