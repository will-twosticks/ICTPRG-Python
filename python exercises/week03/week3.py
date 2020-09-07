#question 1
"""
name = input("what is your name? ")

if (name == "frank") or (name == "george"):
    print("welcome " + name)
"""
#question 2
"""
currentYear = 2020
drinkingAge = 18
askedYear = int(input("what year were you born? "))

if currentYear - askedYear >= drinkingAge:
    print("Come in and drink")
else:
    print("go away child")
"""
#question 3
"""
username = input("what is your username? ")
dpassword = int(input("what is your password? "))

if (username == "bob") and (password == "1234"):
    print("access granted")
else:
    print("access denied")
"""
#question 4 
"""
username = input("what is your username? ")
password = input("what is your password? ")

if (username == "bob") and (password == "password1234"):
    print("access granted")
elif (username == "fred") and (password == "happypass122"):
    print("access granted")
elif (username == "lock") and (password == "passwithlock44"):
    print("access granted")
else:
    print("access denied")
"""
#question 5
"""
High Distinction 	100 - 90
Distinction 	89- 80
Credit 	79 - 70
Pass 	69 - 50
"""
highdistinction = 90
distinction = 80
credit = 70
passed = 50

score = int(input("what is your score? "))

if score >= highdistinction:
    print("you got a high distinction")
elif score >= distinction:
    print("you got a distinction")
elif score >= credit:
    print("you got a credit")
elif score >= passed:
    print("you got a pass")
else:
    print("you failed")