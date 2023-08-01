def find_number_by_name(name):
    line_number = 0

    with open("name.txt", 'r') as file:
        for line in file:
            line_number += 1
            if name in line:
                break
    file.close()
    
    with open("number.txt", "r") as file:
        current_line = 1
        number=""
        for line in file:
            if current_line == line_number:
                number = line
            current_line += 1
    file.close()
    return number

def find_name_by_number(number):
    line_number = 0

    with open("number.txt", 'r') as file:
        for line in file:
            line_number += 1
            if number in line:
                break
    file.close()
    
    with open("name.txt", "r") as file:
        current_line = 1
        name=""
        for line in file:
            if current_line == line_number:
                name = line
            current_line += 1
    file.close()
    return name 

def number_check(number):
    for i in (number):
        if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i =='9' or i == '0':
            flag1 = False
        else:
            flag1 = True
        
        
    while flag1 == True :
        print("you have endeted non-number")
        number = str(input("What is the name you want to save: "))
        
def dict_name ():
    name = input("Enter who's number you want: ")
    
    print("the number of",name,"is",find_number_by_name(name))   
        
def dict_number ():
    number = input("Enter which number's, name you want: ")
    number_check(number)
    
    print("the name with the number",number,"is",find_name_by_number(number))
            
def save():
    name = str(input("What is the name you want to save: "))
    number = str(input("What is the number you want to save: "))
    number_check(number)
        
    file = open("name.txt", "a")
    file.write(name + "\n")
    file.close()
    file = open("number.txt", "a")
    file.write(number + "\n")
    file.close()
    
while True:
    print("Choose task:") 
    print("1. check")
    print("2. save")
    print("3. exit")
    n = str(input("Enter 1 or 2 or 3 : "))
    
    while n != '1' and n != '3' and n != "2":
        print("Error")
        print("Choose task:")
        print("1. check")
        print("2. save")
        print("3. exit")
        n=str(input("enter 1 or 2 or 3: "))
        
        
    if n== "1":
        print("task selected: check")
        print("choose task:")
        
        print("1. check by name")
        print("2. check by number")
        c = str(input("Enter 1 or 2 : "))
        
        while c != '1' and c != '2':
            print("error")
            print("choose task:")
            print("1. check by name ")
            print("2. check by number")
            c=input("enter 1 or 2 : ")
            
        if c == "1":
            print("Task selected: check by name.")
            dict_name()
            
        if c == "2":
            print("Task selected: check by number.")
            dict_number()
            
    if n == "2":
        print("Task selected: save")
        save()

    if n=="3":
        print("Task seleted: exit")
        break