from person import Person
import file_management as file


class MyPhoneBook:
    def __init__(self):
       file.create_new_book()

    @staticmethod
    def to_dict(person):
        return {"s_id": person.s_id, "f_name": person.f_name, "l_name": person.l_name, "phone": person.phone,
                "email": person.email, "address": person.address}

    @staticmethod
    def to_class(person_dict):
        contact = Person(person_dict["s_id"], person_dict["f_name"], person_dict["l_name"], person_dict["phone"],
                         person_dict["email"], person_dict["address"])
        return contact

    def add_contact(self):
        s_id = file.get_last_sid()
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        phone = int(input("Enter Phone Number: "))
        email = input("Enter Email Address: ")
        address = input("Enter Full Postal Address: ")
        add_data = Person(s_id + 1, f_name, l_name, phone, email, address)
        add_contact_dict = self.to_dict(add_data)

        file.append_element(add_contact_dict)
        return f_name

    def get_all_contacts(self):
        all_contacts = file.read_data()
        for var in all_contacts:
            contact = self.to_class(var)
            print("S.id :{0}, Name: {1} {2}, Phone: {3}, Email Id: {4}, Address: {5}".format(contact.s_id + 1, contact.f_name, contact.l_name, contact.phone, contact.email, contact.address))

    def get_contact(self):
        name = int(input("Enter name to Get Contact details: "))
        temp = file.get_element_by_sid(name)
        contact = self.to_class(temp)
        return "Contacts are: Name: {} {}, Phone: {}, Email Id: {}, Address: {}".format(contact.f_name, contact.l_name, contact.phone, contact.email, contact.address)

    @staticmethod
    def delete_contact():
        s_no = int(input("Enter Serial No. to Delete Contact details: "))
        deleted = file.delete_element_by_sid(s_no - 1)
        return "Contact with Serial {} deleted successfully.".format(s_no) if deleted else "No Contact found"

    def modify_contact(self):
        s_no = int(input("Enter Serial No. to Modify Contact details: "))
        fetched_contact_dict = file.get_element_by_sid(s_no - 1)
        while True:
            if fetched_contact_dict:
                contact = self.to_class(fetched_contact_dict)
                f_name = input("Enter First Name ({}): ".format(contact.f_name))
                l_name = input("Enter Last Name ({}): ".format(contact.l_name))
                phone = input("Enter Phone Number ({}): ".format(contact.phone))
                email = input("Enter Email Address ({}): ".format(contact.email))
                address = input("Enter Full Postal Address ({}): ".format(contact.address))
                contact = Person(s_no - 1, f_name, l_name, phone, email, address)
                contact_dict = self.to_dict(contact)
                file.modify_element_by_sid(contact_dict)
                return "Contact updated by Serial {}: Name: {} {}, Phone: {}, Email Id: {}, Address: {}".format(s_no, contact.f_name, contact.l_name, contact.phone, contact.email, contact.address)


def main():
    print("Inside Phone Book Main")
    phone_book = MyPhoneBook()


if __name__ == "__main__":
    main()
