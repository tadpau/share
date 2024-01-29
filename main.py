from add_food import ProductManager
from active_product import active_disactive_delete_product
from daily_calories import calculate_daily_calories
from meal_plan import generate_meal_plan
from meal_plan_handler import handle_meal_plan_download
from nutrition import find_food_calories


def display_menu():
    print("\nMenu:")
    print("1. Add product.")
    print("2. Find product calories.")
    print("3. Active/Deactive or Delete product.")
    print("4. Find your calorie needs.")
    print("5. Make a meal plan.")
    print("6. Download your latest meal plan.")
    print("7. Exit")

def main():
    product_manager = ProductManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            name = input("Enter the name of the product: ")
            calories_per_100g = float(input("Enter calories per 100g: "))
            food_group = input(f"Enter the food group ({', '.join(ProductManager.ALLOWED_FOOD_GROUPS)}): ").lower()
            preferred_time = input(f"Enter preferred time of usage ({', '.join(ProductManager.ALLOWED_TIME_OF_USAGE)}): ").lower()
            try:
                product_manager.add_product(name, calories_per_100g, food_group, preferred_time)
                print("Product added successfully.")
            except ValueError as e:
                print(e)
        elif choice == '2':
            food_name = input("Enter the name of the food you want to find: ")
            find_food_calories(food_name)
        elif choice == '3':
            active_disactive_delete_product()
        elif choice == '4':
            calculate_daily_calories()
        elif choice == '5':
            meals_per_day = int(input("How many times will you eat per day? "))
            daily_calories = float(input("How many calories do you need to eat per day? "))
            generate_meal_plan(meals_per_day, daily_calories, product_manager)
        elif choice == '6':
            handle_meal_plan_download()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()


