FirstName = []
LastName = []
Age = []
Year = 2020
User = 0

# users personal data
while True:
    FirstInput = input("what is your first name? ")
    if FirstInput  == "":
        break

    FirstName.append(FirstInput)

    SecondInput = input("what is your last name? ")
    LastName.append(SecondInput)

    ThirdInput = int(input("what is your age? "))
    Age.append(ThirdInput)
    User += 1

# output user name and password of users
for x in range(User):
    Username = (FirstName[x][:1]) + (LastName[x]) + ("@Huawow.io")
    Password = (FirstName[x]) + (LastName[x][:1]) + str(Year - Age[x] - 9)
    print(Username + "|" + Password)
    print("-------------------------")

    