

#---------------------banking program--------------------



def show_balance(balance):
    print(f"your balance is ${ balance:.2f}")

def deposit():
    amount = float(input("enter an amount to be deposited: "))
    
    if amount < 0:
        print("that's not a valid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    
    amount = float(input("enter amount to be withdraw: "))

    if amount > balance:
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("amount must be greater than 0")
    else:
        return amount


def main(): 
   balance = 0
   is_running = True

   while is_running:
     print("********************************")
     print("banking program")
     print("_______________________________________")
     print("1.show_balance")
     print("2.deposit")
     print("3.withdraw")
     print("4.exit")
     print("**********************************")

     choice = input("enter your choice (1-4): ")
 
     if choice =="1":
        show_balance(balance)
     elif choice =="2":
        balance += deposit()
     elif choice =="3":
       balance -= withdraw(balance)
     elif choice =="4": 
        exit()
     else:
        print("that is not a valid choice")
   print("*******************************************")
   print("Thank you! have a nice day!")
   print("********************************************")

if __name__ == '__main__':
   main()
