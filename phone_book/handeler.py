from phone_book import MyPhoneBook


def hello():
    while True:
        print("Welcome to Your Phone Book.")
        printing_value = ["1. Add Contact", "2. Modify Contact.", "3. Delete Contact ", "4. See all Contacts",
                          "5. Get Contact by Name.", "6. Sorted Contact"]
        for ps in range(len(printing_value)):
            print(printing_value[ps])
        number = int(input("enter your choice  "))
        if number == 1:
            MyPhoneBook().add_contact()
        if number == 2:
            MyPhoneBook().modify_contact()
        if number == 3:
            MyPhoneBook().delete_contact()
        if number == 4:
            MyPhoneBook().get_all_contacts()
        if number == 5:
            MyPhoneBook().get_contact()
        if 0 > number < 6:
            print("Invalid number entered. Please try again: ")


def main():
   hello()

if __name__ == "__main__":
    main()
        
