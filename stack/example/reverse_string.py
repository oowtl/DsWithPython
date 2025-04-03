from stack.list_stack import ListStack


def reverse(str):
    st = ListStack()

    for i in range(len(str)):
        st.push(str[i])

    out = ""

    while not st.is_empty():
        out += st.pop()

    return out

def main():
    input = "Test Seq 1234567"
    answer = reverse(input)
    print("Input: ", input)
    print("Output: ", answer)

if __name__ == '__main__':
    main()