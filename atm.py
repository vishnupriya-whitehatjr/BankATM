print("Welcome to the fastest Banking System!")
ac_num = int(input("Enter your Registed Bank Account Number"))
pin_num = int(input("Enter your pin number"))
balance = 25000
if (ac_num == 2) : 
    if( pin_num == 8):
        print("Welcome, Please choose your transaction of your choice: ")
        print("1.Balance Enquiry")
        print("2.Deposit")
        print("3.Withdrawl")
        choice =int(input("We are waiting for your options.... "))
        if(choice == 1):
            print("Balance is:",balance)
        elif(choice == 2):
            deposit = int(input("Enter amount you want to deposit: "))
            balance = balance+deposit
            print("Balance is:",balance)
        elif(choice == 3):
            withdraw = int(input("Enter amount you want to deposit: "))
            balance = balance-withdraw
            print("Balance is:",balance)
        else:
            print("Invalid Input!")            

    else:
        print("Wrong pin number!")

else:
    print("Account doesnot exists,Sorry!!")
