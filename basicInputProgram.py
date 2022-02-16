strUsername = "Hello InputName, How are you?"
varUsername = input("Enter User Name: ")
if len(varUsername) < 3:
	print("User Name must have 3 characters.")
else:
	print(strUsername.replace("InputName", varUsername))
