from pathlib import Path
from os import system

#show_start_menu

my_path = Path(Path.home(),'Recipes')

def count_receipe(path):
    counter = 0

    for txt in Path(path).glob('**/*/.txt'):
        count_receipe +=1
    return counter


def start():
    system("clear")
    print( '*' * 50)
    print("Welcome to the recipe admnistrator")
    print( '*' * 50)
    print('\n')
    print(f'The recipes are in my path{my_path}')
    print(f'Total Reciepes that are avaiable in the system is : {count_receipe(my_path)}')


start()
menu =0

if menu ==1:
    #shows category
    #Chosse a category
    #show recipe
    #chosse a recipe
    #read a reciepe
    #go back to menu
    pass
elif menu ==2:
    #show categories
    #chosse a category
    #create a new recipe
    # go back
    pass

elif menu ==3:
    #create catgroy
    #go back to menu
    pass
elif menu == 4:
    #shows category
    #Chosse a category
    #show recipe
    #chosse a recipe
    #emliminate reciepe
    #go back to menu
    pass

elif menu ==5:
    #shows category
    #Chosse a category
    #eliminate the category
    #go back to menu
    pass
elif menu == 6:
    #end program
    pass
