# RANDOM MODULE
import random

# FUNCTION FOR THE INSTRUCTIONS AND INFORMATIONS OF THE PROGRAM
def info():
    print("------------------------------------------------------------")
    print('''\nINSTRUCTIONS:
1.You can choose multiple categories for the password by just entering the categories number all together.
2.Symbols used for password creation ['~','@','#','$','%','&','*','?','-','_'].
3.For the default category password will be generated by taking all four categories with uniqueness in it.
4.If input is invalid for the uniqueness then it would be considered yes for uniqueness as default.
5.Uniqueness: Every character of the password will be unique/different.

INFORMATION:
This program generates random password on user validations such as password length or password category.This program uses "random" module of the python which comes with many random functions. Some important of them are "random.randint","random.choice",etc. This program works on many utilities of python which includes functions, if-else, loops, list, strings.''')
print("------------------------------------------------------------")

# FUNCTION FOR NUMERIC PASSWORD
def numericpassword():
    num=[]
    for j in range(0,passwordlength):
        num.append(chr(random.randint(48,57)))
    return num

# FUNCTION FOR SMALL LETTERS PASSWORD
def salphapassword():
    salpha=[]
    for j in range(0,passwordlength):
        salpha.append(chr(random.randint(97,122)))
    return salpha

# FUNCTION FOR CAPITAL LETTERS PASSWORD
def calphapassword():
    calpha=[]
    for j in range(0,passwordlength):
        calpha.append(chr(random.randint(65,90)))
    return calpha

# FUNCTION FOR SYMBOLIC PASSWORD
def symbolspassword():
    symbols=['~','@','#','$','%','&','*','?','-','_']
    symbol=[]
    for j in range(0,passwordlength):
        symbol.append(random.choice(symbols))
    return symbol

# FUNCTION FOR GENERATING PASSWORDS
def passwordgenerator():
    
    # INPUT FOR THE PASSWORD LENGTH
    global passwordlength
    print("------------------------------------------------------------")
    passwordlength=int(input("\nEnter the lenth for the password:"))
    print("------------------------------------------------------------")
    
    # INPUT FOR PASSWORD CATAGORIES
    print('''\nCatagories for the password type:

    1.Integers.
    2.Small Characters.
    3.Capital Characters.
    4.Symbols.
    5.Default (It considers all 4 catagories for a stronger password.).''')
    print("------------------------------------------------------------")
    print("\nNOTE: YOU MAY ENTER SINGLE CATAGORY OR MULTIPLE CATAGORIES FOR YOUR PASSWORD.")
    passwordcatagory=str(input("Choose catogory numbers:"))
    print("------------------------------------------------------------")
    
    # MAIN LIST CREATION OF PASSWORD
    passwordlist=[]
    for i in (passwordcatagory):
        if (i=="1"):
            passwordlist+=numericpassword()
        elif (i=="2"):
            passwordlist+=salphapassword()
        elif (i=="3"):
            passwordlist+=calphapassword()
        elif (i=="4"):
            passwordlist+=symbolspassword()
        elif (i=="5"):
            passwordlist+=numericpassword()
            passwordlist+=salphapassword()
            passwordlist+=calphapassword()
            passwordlist+=symbolspassword()
        else:
            print("\nInvalid Catagory input... Correctly enter the specifications.")
            n=passwordgenerator()
            return n
            
    # SHUFFLING THE ELEMENTS IN THE LIST
    random.shuffle(passwordlist)

    # IF ELSE FOR UNIQUINESS IN THE PASSWORD
    if (passwordcatagory!="5"):
        uniqueness=str(input("\nDo you want every character in your password to be unique?\nEnter y for yes or n for no:"))
        print("------------------------------------------------------------")
        if (uniqueness=="y" or uniqueness=="Y" or uniqueness=="n" or uniqueness=="N"):
            pass
        else:
            print("\nInvalid uniqueness input... Password will be generated on default settings.(It considers yes for uniqueness.)")
            print("------------------------------------------------------------")
            
    print("\n*Click enter to create the password again and again in the same catagory\n*Click 1 and then Enter to change the specifications for a new password.\n*Click 2 and then Enter to return to the Task list.")
    print("------------------------------------------------------------")
    
    anotherpassword=""
    while True:
        anotherpassword=str(input("*"))
        if(anotherpassword==""):
            if(passwordcatagory=="5"):
                finalpasswordlist=random.sample(passwordlist,k=passwordlength)
            else:
                if(uniqueness=="y" or uniqueness=="Y"):
                    finalpasswordlist=random.sample(passwordlist,k=passwordlength)
                elif(uniqueness=="n" or uniqueness=="N"):
                    finalpasswordlist=random.choices(passwordlist,k=passwordlength)
                else:
                    finalpasswordlist=random.sample(passwordlist,k=passwordlength)

            # CREATING THE FINAL PASSWORD
            finalpassword=""

            for i in finalpasswordlist:
                finalpassword+=i

            print("Your password:",finalpassword)
        else:
            break
    return anotherpassword
    
# TASKS OF THE PROGRAM
def tasklist():
    
    print("------------------------------------------------------------")
    print('''\nTASK LIST:\n\n1.Generate Password.\n2.Instructions/Informations.\n3.Exit the program.''')
    print("------------------------------------------------------------")
    choice=int(input("\nEnter your choice:"))
    
    if (choice==1):
        n="1"
        while True:
            if (n=="1"):
                n=passwordgenerator()
            elif (n=="2"):
                tasklist()
                break
            else:
                print("\nInvalid Input!!! Returning to the task list...")
                tasklist()
                break
    elif (choice==2):
        info()
        tasklist()
    elif (choice==3):
        print("------------------------------------------------------------")
        print("\nThankyou for checking out the program...!")
        print("------------------------------------------------------------")
    else:
        print("------------------------------------------------------------")
        print("\nInvalid Input!!! Correctly enter the choice number.")
        tasklist()

tasklist()