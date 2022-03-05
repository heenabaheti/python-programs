from data_structure_problem.stack import Stack


def paren_balance(expression):
    open_paren = "({["
    closed_paren = ")}]"

    for bracket in expression:
        if bracket in open_paren:
            Stack.push(bracket)
        elif bracket in closed_paren:
            if Stack.is_Empty():
                balanced = False
                break
            Stack.pop()
    else:
        if Stack.is_Empty():
            balanced = True
        else:
            balanced = False
    if balanced:
        print("Expression '", expression, "' is correct")
    else:
        print("Expression '", expression, "' is incorrect")



def main():
    expression = input("Enter the expression: ")
    print(paren_balance(expression))


if __name__ == "__main__":
    main()

