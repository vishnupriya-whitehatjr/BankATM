print("Welcome to the fastest Banking System!")
ac_num = int(input("Enter your Registed Bank Account Number"))
pin_num = int(input("Enter your pin number"))
def choose(i):
    switcher={
        1:balance(),
        2:deposit(),
        3:withdraw()
    }
    return switcher.get(i,"Invalid input")
def balance():
    print("balance is 25000")
def deposit():
    print("hey")
def withdraw():
    print("good")
if (ac_num == 282828) : 
    if( pin_num == 2222):
        print("Welcome, Please choose your transaction of your choice: ")
        print("1.Balance Enquiry")
        print("2.Deposit")
        print("3.Withdrawl")
        choice =int(input("We are waiting for your options.... "))
        choose(cho)
    else:
        print("Wrong pin number!")

else:
    print("Account doesnot exists,Sorry!!")
