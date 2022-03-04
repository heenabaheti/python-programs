import json
import os


def delete(contact_id):
    data = read_data()
    read_index = next((i for i, item in enumerate(data) if item["s_id"] == contact_id), None)
    if read_index:
        del data[read_index]
        write_data(data)
        return True
    else:
        return False


def read_file():
    with open("book.json", 'r') as phone_book:
        read_value = json.load(phone_book)
    return read_value


def write_file(value):
    with open("book.json", 'w') as phone_book:
        json.dump(value, phone_book)
        phone_book.close()


def write_data(value):
    updated_data = {'content': value}
    write_file(updated_data)


def read_data():
    data = read_file()
    value = list(data['person'])
    return value


def append_element(contact):
    data = read_file()
    data.append(contact)
    write_data(data)


def get_element_by_sid(s_id):
    data = read_file()
    read_element = next((item for item in data if item["s_id"] == s_id), None)
    return read_element


def get_last_sid():
    data = read_file()
    if len(data) > 0:
        read_element = data[len(data) - 1]
        return read_element["s_id"]
    else:
        return -1


def modify_element_by_sid(contact):
    data = read_data()
    read_index = next((i for i, item in enumerate(data) if item["s_id"] == contact["s_id"]), None)
    if read_index:
        data[read_index] = contact
        write_data(data)
        return contact
    else:
        return None


def delete_element_by_sid(s_id):
    data = read_data()
    read_index = next((index for index, item in enumerate(data) if item["s_id"] == s_id), None)
    if read_index:
        del data[read_index]
        write_data(data)
        return True
    else:
        return False


def sort_elements_by_key(key):
   dat = read_data()
   dat = sorted(dat, key=lambda i: i[key])
   return data


def create_new_book():
    dat = {'contacts': []}
    if not os.path.exists("book.json"):
        write_file(dat)
    else:
        read_dat = read_file()
        if read_dat == None:
            write_file(dat)
        else:
            dat = read_data


def main():
   create_new_book()


if __name__ == "__main__":
    main()

