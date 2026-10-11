def Perfume():
    for i in range(1,1000):
        yield f'[Perfume ticket] - {i}'

def Clothes():
    for i in range(1,1000):
        yield f'[Clothes ticket] - {i}'

def Electronics():
    for i in range(1,1000):
        yield f'[Electronics ticket] - {i}'


P = Perfume()
C = Clothes()
E = Electronics()

def product_choose(my_product):
    print('*' * 20)
    print('\n')
    print('Your number is :')


    if my_product == 'P':
        print('Thank you for chosing perfume')
        print('\n')
        print(next(P))
    elif my_product == 'C':
        print('Thank you for chosing Clothes')
        print('\n')
        print(next(C))
    else:
        print('Thank you for chosing Electronics')
        print(next(E))

    print('Please wait for your turn')

        