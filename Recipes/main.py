import tickets

def ask():
    print('*' * 20)
    print('\n')
    print("Welcome to the shopping vending machine. Get your ticket number and head to counter to get your product")

    while True:
        try:
            my_product = input('Enter your purchase [P] - Perfume , [C] - Clothes ,  [E] - Electronics: ').upper()
            ['P','C','E'].index(my_product)
        except ValueError():
            print("Please Enter a correct value")   
        else:
            break
    tickets.product_choose(my_product)

def start():
    print('*' * 20)
    print('\n')

    while True:
        ask()
        try:
            another_ticket = input("Please select if you want another ticket [Y] - Yes or [N] - No : ").upper()
            ['Y','N'].index(another_ticket) 
        except ValueError:
            print('Please enter a correct value since the enterd value is wrong')
        if another_ticket == 'N':
            print("Thank you for shoping with us")
            break      
start()             
        