class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)
        return self.array

    def pop(self):
        self.array.pop()
        return self.array

    def is_Empty(self):
        if self.array is []:
            return " Stack is Empty"
        return "Stack is NOT Empty"

    def size_of_stack(self):
        if self.array is []:
            return "Stack is Empty"
        else:
            return len(self.array)

    def top(self):
        return self.array[-1]

    def display_values(self):
        print(self.array)


def main():
    st = Stack()
    while True:
        print("*************")
        print("1: Add into Stack")
        print("2: Delete From Stack")
        print("3: Printing value")
        print("4: Size of stack")
        print("5: Quit")
        val = int(input("Enter your preference "))
        if val == 1:
            value = input("Enter value to insert in stack :")
            st.push(value)
            st.display_values()
        if val == 2:
            a = st.pop()
            print("element which is deleted is :", a)
            st.display_values()
        if val == 3:
            print("Elements in list are :")
            st.display_values()
        if val == 4:
            print("size of stack", st.size_of_stack())
            st.size_of_stack()
        if val == 5:
            break

if __name__ == '__main__':
    main()
