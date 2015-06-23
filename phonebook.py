# -*- coding utf-8 -*-

def menu() :
    print(""" 1. Print phone number \n
              2. Add number \n
              3. Delete number \n
              4. Find number \n
              5. Download number \n
              6. Save number \n
              7. Quit phone book""");
    print()

def printNumbers(numbers) :
    print("Phone list:")
    for key, value in numbers.items() :
        print("Name: ", key, "Number: ", value)

def addNumber(numbers, name, number) :
    numbers[name] = number
    
def deleteNumber(numbers, name) :
    if name in numbers :
        del numbers[name]
    else :
        print(name, "not found")
        
def findNumber(numbers, name) :
    if name in numbers :
        return name + "The number is " + numbers[name]
    else :
        return name + " was not found"

def downloadNumber(numbers, filename) :
    in_file = open(filename, "rt")
    while True :
        in_line = in_file.readline()
        if not in_line :
            break
        in_line = in_line[:-1]
        name, number = in_line.split(",")
        numbers[name] = number
    in_line.close()
        
def saveNumber(numbers, filename) :
    out_file = open(filename, "wt")
    for key, value in numbers.items() :
        out_file.write(key + "," + value + "\n")
    out_file.close()
        
phoneList ={}
menuChoice = 0
loop = True
menu()
while loop == True :
    menuChoice = int(input("Choose and Print operation number"))
    if menuChoice == 1:
        printNumbers(phoneList)
    elif menuChoice == 2:
        print("Add new number:")
        name = input("Print new name")
        number = input("Print new number")
        addNumber(phoneList, name, number)
    elif menuChoice == 3:
         name = input("Print new name")
         deleteNumber(phoneList, name)
    elif menuChoice == 4:
        name = input("Find name")
        print(findNumber(phoneList, name))
    elif menuChoice == 5:
        filename = input("Filename to load: ")
        downloadNumber(phoneList, filename)
    elif menuChoice == 6:
        filename = input("Filename to save: ")
        saveNumber(phoneList, filename)
    elif menuChoice == 7:
        loop = False
    else:
        menu()
 
print("Goodbye")
        