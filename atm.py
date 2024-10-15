user = "pavan"
password = 1234
balance = 100
user_name = input("Enter Your Name :")
if user_name == user:
    for i in range(1,4):
        pass_word = int(input("Enter Your password :"))
        if pass_word == password:
            print("log in succesful")
            print("1 withdraw\n2 deposit\n3 balance enquiry\n4 change PIN\n5 EXIT")
            option = int(input("Enter your Option :"))
            if option == 1:
                a = int(input("Enter your Amount:"))
                if a <= balance:
                    balance -= a
                    print(balance)
                else :
                    print("LIMIT is exceeded")
            elif option == 2:
                a = int(input("enter your amount :"))
                if a >= 100:
                    balance += a
                    print("succesfully deposited")
                    print(balance)
                else:
                    print("your amount is less than 100")
            elif option == 3:
                a = int(input("enter password:"))
                if a == password:
                    print(balance)
                else :
                    print("invalid password")
            elif option == 4:
                a = int(input("enter password:"))
                if a == password:
                    b = int(input("enter new password:"))
                    print("password changed sucesfully")
                else :
                    print("incorrect password")
else:
    print("log in fail")
    print(i,"attempt is completed")
    print(2-i,"attempts is remaining")
if (i == 2):
    print("account is blocked")
        
