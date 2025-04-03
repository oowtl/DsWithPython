from .list_stack import ListStack

if __name__ == '__main__':
    st1 = ListStack()
    print(st1.top())
    st1.push(100)
    st1.push(200)
    print("Top is", st1.top())
    st1.pop()
    st1.push("Monday")
    st1.print_stack()
    print("is Empty?", st1.is_empty())
