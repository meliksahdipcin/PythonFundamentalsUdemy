def add(n1,n2):
    print(n1+n2)

number1 = 20
number2 = input("give a number: ") #string value

try:
    add(number1,number2)
except:
    print("An error occured.")
else:
    print("Function worked successfully.")
    
    
try:
    f = open("testfile","w")
    f.write("Write a test line")
except TypeError:
    print("You have a typing error.")
except OSError:
    print("You have an OS error.")
except:
    print("There was an error.")
finally:
    print("This always runs.")


def ask_for_int():
    
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("That's not a number!")
            continue
        else:
            print("Yes thank you!")
            break
        finally:
            print("End of try/except/finally")
            print("This always runs.")
        
ask_for_int()
