def asknumber():

    while True:

        try:
            Number = int(input("Enter a number :"))

        except: 
            print(f'The Entered Number is not a valid number at all')

        else:
            print(f'Thank you for entering a valid number and the number is : {Number}')
            break
    print('Thank you!')

asknumber()


    