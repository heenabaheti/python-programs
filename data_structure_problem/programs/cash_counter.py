from data_structure_problem.queue import QueueStructure


def cash_counter(self):
    """This is a function where people come to deposit cash or withdraw cash
    Input: Asking individuals to deposit or withdraw the amount
    """

    cash = 10000  # Initiating a variable which consists of the amount the bank has

    while True:
        print("1 --> Deposit Cash")
        print("2 --> Withdraw Cash")
        print("3 --> Exit")
        # Taking user inputs for the type of transaction
        choice = int(input("Please enter a value: "))
        # If the user wants to deposit the cash
        if choice == 1:
            amount = int(input("Enter the amount  to deposit: "))
            QueueStructure.enqueue(amount)
            cash += amount
            print("your balance is", cash)
            print("Thank You! Cash Deposited Successfully")
        # If the user wants to withdraw cash
        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            QueueStructure.dequeue()
            if cash >= amount:
                cash -= amount
                print("Thank You! Cash Withdrawal Successful")
            else:
                # If the withdrawal amount is more than the cash available
                print("Insufficient Balance!")
        # If the user wants to exit
        elif choice == 3:
            quit()
