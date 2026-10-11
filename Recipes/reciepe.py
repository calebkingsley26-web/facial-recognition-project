from pathlib import Path
from os import system

# Root recipe folder
my_path = Path(__file__).resolve().parent


def count_recipe(path):
    return len(list(Path(path).rglob("*.txt")))


def start():
    system("clear")  # Use "cls" if you're on Windows

    print("*" * 50)
    print("WELCOME TO THE RECIPE ADMINISTRATOR")
    print("*" * 50)

    print(f"\nRecipe directory: {my_path}")
    print(f"Total recipes available: {count_recipe(my_path)}\n")

    while True:
        print("""
        [1] Read Recipe
        [2] Create Recipe
        [3] Create Category
        [4] Delete Recipe
        [5] Delete Category
        [6] Exit
        """)

        choice = input("Choose an option: ")

        if choice.isnumeric() and int(choice) in range(1, 7):
            return int(choice)

        print("Invalid choice. Try again.\n")


def show_categories(path):
    categories = list(Path(path).iterdir())

    print("\nAvailable Categories:\n")

    for i, category in enumerate(categories, start=1):
        print(f"[{i}] {category.name}")

    return categories


def choose_category(category_list):
    while True:
        choice = input("\nChoose a category: ")

        if choice.isnumeric() and int(choice) in range(1, len(category_list) + 1):
            return category_list[int(choice) - 1]

        print("Invalid choice.")


def show_recipes(path):
    recipes = list(Path(path).glob("*.txt"))

    print("\nAvailable Recipes:\n")

    for i, recipe in enumerate(recipes, start=1):
        print(f"[{i}] {recipe.stem}")

    return recipes


def choose_recipe(recipe_list):
    while True:
        choice = input("\nChoose a recipe: ")

        if choice.isnumeric() and int(choice) in range(1, len(recipe_list) + 1):
            return recipe_list[int(choice) - 1]

        print("Invalid choice.")


def read_recipe(recipe):
    print("\n" + "=" * 40)
    print(recipe.read_text())
    print("=" * 40)
    input("\nPress Enter to continue...")


def create_recipe(path):
    while True:

        recipe_name = input("Recipe name: ").strip() + ".txt"

        new_path = Path(path, recipe_name)

        if new_path.exists():
            print("Recipe already exists.\n")
            continue

        print("Write your recipe (press Enter when finished):")
        recipe_content = input()

        new_path.write_text(recipe_content)

        print("\nRecipe created successfully!")
        input("\nPress Enter to continue...")
        break


def create_category(path):
    while True:

        category_name = input("Category name: ").strip()

        new_path = Path(path, category_name)

        if new_path.exists():
            print("Category already exists.\n")
            continue

        new_path.mkdir()

        print("\nCategory created successfully!")
        input("\nPress Enter to continue...")
        break


def delete_recipe(recipe):
    recipe.unlink()
    print("\nRecipe deleted successfully!")
    input("\nPress Enter to continue...")


def delete_category(category):
    try:
        category.rmdir()
        print("\nCategory deleted successfully!")
    except OSError:
        print("\nCategory is not empty. Delete all recipes first.")

    input("\nPress Enter to continue...")


# ---------------- MAIN PROGRAM ---------------- #

while True:

    menu = start()

    if menu == 1:

        categories = show_categories(my_path)
        category = choose_category(categories)

        recipes = show_recipes(category)

        if len(recipes) == 0:
            print("\nNo recipes found.")
            input("\nPress Enter to continue...")
            continue

        recipe = choose_recipe(recipes)
        read_recipe(recipe)

    elif menu == 2:

        categories = show_categories(my_path)
        category = choose_category(categories)

        create_recipe(category)

    elif menu == 3:

        create_category(my_path)

    elif menu == 4:

        categories = show_categories(my_path)
        category = choose_category(categories)

        recipes = show_recipes(category)

        if len(recipes) == 0:
            print("\nNo recipes found.")
            input("\nPress Enter to continue...")
            continue

        recipe = choose_recipe(recipes)

        delete_recipe(recipe)

    elif menu == 5:

        categories = show_categories(my_path)
        category = choose_category(categories)

        delete_category(category)

    elif menu == 6:

        print("\nThank you for using the Recipe Administrator!")
        break