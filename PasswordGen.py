"""
Python Password Generator
Jack Jolley
Date: 3/27/2020
"""
import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

def GetRandomChar():
    value = round(random.random(), 2)
    #print(value)

    if value >= 0 and value <= 0.24:
        #print("lower")
        returnVal = random.choice(lowercase)
    elif value >= 0.25 and value <= 0.49:
        #print("upper")
        returnVal = random.choice(uppercase)
    elif value >= 0.50 and value <= 0.74:
        #print("numbers")
        returnVal = random.choice(numbers)
    elif value >= 0.75 and value <= 1:
        #print("characters")
        returnVal = random.choice(characters)

    #print(returnVal)
    return returnVal

def GeneratePassword():
    passwordArray = []
    passwordLength = random.randint(12,16)
    for i in range(passwordLength):
        #print(i)
        passwordArray.append(GetRandomChar())

    #print(passwordArray)
    output = ''.join(passwordArray)
    print("Password Generated: " + output + "\n")

    newQuestion = input("Would you like to generarte a new password (Y/N):\n ")
    AskQuestion(newQuestion)

def AskQuestion(question):
    if question == "Y" or question == "y":
        print("Generating Password..........")
        GeneratePassword()
    elif question == "N" or question == "n":
        print("Goodbye")
        exit()
    else:
        print("Input not recognised....")

GetRandomChar()

passQuestion = input("Would you like to generarte a new password (Y/N):\n ")
AskQuestion(passQuestion)





