import random
# lucky draw program
# Given N distinct Coupon Numbers, how many random numbers do you
# need to generate distinct coupon number? This program simulates this random
# process.


distinctNumber = int(input("How many Distinct coupon You Want: "))
coupon_number = int(input("Enter Your lucky number"))
randomList = []
count = 0
# generating random number and storing them into the list
while True:
    number = random.randint(1111, 9999)
    count += 1
    if number not in randomList:
        randomList.append(number)
    if len(randomList) == distinctNumber:
        break
print("Total Number of Random number Generated: ", count)
print("Lucky Coupon Numbers Are :")

# printing the list
for i in range(0, len(randomList)):
    print(randomList[i], end=" ")
print()

if coupon_number in randomList:
    print("Congratulations! you got lottery")
else:
    print("Better luck next time")
