import random
from send_email import send_email
from add_food import ProductManager
#reads food_list and takes needed informatiom from there
def read_food_list():
    food_list = []
    try:
        with open('food_list.txt', 'r') as file:
            for line in file:
                _, name, calories_per_100g, food_group, time_preference, status = line.strip().split(',')
                if status.lower() == 'active':
                    food_list.append({
                        'name': name,
                        'calories_per_100g': float(calories_per_100g),
                        'food_group': food_group.lower(),
                        'time_preference': time_preference.lower()
                    })
    except FileNotFoundError:
        print("No products found.")
    return food_list

#checks if at least 10 food is added to the list
def check_minimum_foods(product_manager):
    food_list = read_food_list()
    active_foods = [food for food in food_list if food['food_group'] != 'inactive']
    if len(active_foods) < 10:
        print("There are less than 10 active foods.")
        add_more_foods(product_manager)
        return False
    return True
#If there is less than 10 food on the list user can top up the list
def add_more_foods(product_manager):
    while True:
        add_more = input("Do you want to add more foods? (yes/no): ").lower()
        if add_more == 'yes':
            print("Please add more foods to the list.")
            product_manager.add_product()
            break
        elif add_more == 'no':
            print("Exiting program. You need at least 10 active foods for meal planning.")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def calculate_total_calories(food_list):
    total_calories = {}
    for food in food_list:
        total_calories.setdefault(food['food_group'], 0)
        total_calories[food['food_group']] += food['calories_per_100g']

    return total_calories

def generate_meal_plan(meals_per_day, daily_calories, product_manager):
    if not check_minimum_foods(product_manager):
        return
#coefficients for calories counting
    food_list = read_food_list()
    total_calories = calculate_total_calories(food_list)
    percentages = {
        'dairy': 0.10,
        'fruit': 0.15,
        'vegetables': 0.15,
        'protein': 0.35,
        'grains': 0.25
    }
#calories counting per catogery and per meal
    grams_per_category = {category: (percentages[category] * daily_calories / (total_calories[category] / 100)) if total_calories[category] != 0 else 0 for category in percentages}

    grams_per_meal = {category: grams / meals_per_day for category, grams in grams_per_category.items()}

    preferred_meal_category = input("Do you have a preferred meal category (morning, lunch, dinner)? If not, enter 'anytime': ").lower()

    meal_plan_text = ""
#check available option for users chosen option for food and fills everything else with was is stored with parameter anything.
    for i in range(1, meals_per_day + 1):
        meal_plan_text += f"\nMeal {i}:\n"
        print(f"\nMeal {i}:")
        for category, grams in grams_per_meal.items():

            preferred_foods = [food for food in food_list if food['food_group'] == category and food['time_preference'] == preferred_meal_category]

            if len(preferred_foods) < grams:
                preferred_foods += [food for food in food_list if food['food_group'] == category and food['time_preference'] == 'anytime']
            if preferred_foods:
                food = random.choice(preferred_foods)
                calories = grams * (food['calories_per_100g'] / 100)
                meal_plan_text += f"{category.capitalize()}: {food['name']} - {grams:.2f}g ({calories:.2f} calories)\n"
                print(f"{category.capitalize()}: {food['name']} - {grams:.2f}g ({calories:.2f} calories)")
            else:
                meal_plan_text += f"No available options for {category.capitalize()} in meal {i}.\n"

    with open('last_meal_plan.txt', 'w') as file:
        file.write(meal_plan_text)
    return meal_plan_text

if __name__ == "__main__":
    product_manager = ProductManager()
    meals_per_day = int(input("How many times will you eat per day? "))
    daily_calories = float(input("How many calories do you need to eat per day? "))

    meal_plan_text = generate_meal_plan(meals_per_day, daily_calories, product_manager)
    print(meal_plan_text)

