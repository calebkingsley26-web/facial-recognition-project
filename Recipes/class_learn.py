class person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name =last_name

class Client(person):
    def __init__(self, first_name, last_name,account_number,balance = 0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'client : {self.first_name} {self.last_name} /n {self.account_number} /n {self.balance}'


    def deposit(self,deposit_amt):
        self.deposit_amt = deposit_amt
        print("Deposit accepted")

    def withdraw(self,withdraw_amt):
        if self.balance >= withdraw_amt:
            self.balance -= withdraw_amt

            print("Withdrawal was sucessfully done")

        else:
            print("Insuffienct funds")   

def create_client():
    first_name_ct =input("Enter your first name")
    last_name_ct = input("Enter your last name")
    account_number = input("Enter your Account number")
    client1 = Client(first_name_ct,last_name_ct,account_number)

    return client1

def start():
    my_customer = create_client()
    print(my_customer)
    option = 0

    while option!= 'E':
        print("choose :Deposit (D),Withdraw (W), or E to Exit")
        option= input()
        if option == 'D':
            dep_amount = int(input("Enter the amount you want to deposit"))
            my_customer.deposit(dep_amount)        

        elif option =="W":
            withdraw_amt =int(input("Enter the amount you would want to withdraw"))
            my_customer.withdraw(withdraw_amt)

        print(my_customer)

    print("Thank you for using the bank")

start()       

