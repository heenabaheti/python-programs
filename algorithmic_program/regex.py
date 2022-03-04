import re


def regexName(message):
    name = re.sub("<name>", str(input("Enter your name")), message)
    print(name)


def regexContactNum(message):
    contactNum = re.sub("91-9908514276", int(input("Enter your number")), message)
    print(contactNum)


def regexFullname(message):
    fullName = re.sub("mohammed mosin", str(input("Enter your full name")), message)
    print(fullName)


def regexDate(message):
    date = re.sub("01/01/2016", str(input("Enter date")), message)
    print(date)


def errorhandler():
    print("Invalid choice")
message = '''
Hello, <name> We have your full
name as <full Name> in our system. your contact number is <number>.
Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.
    '''
print(message)
print('''
   1.Name
   2.Contact Number
   3.Full Name
   4.Date
''')
choice = int(input("Enter your choice"))
operations = {
    1: regexName,
    2: regexContactNum,
    3: regexFullname,
    4: regexDate
}

result = operations.get(choice)
print(result)
