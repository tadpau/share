#call for API and check for users provided food nutrition
import requests

def find_food_calories(food_name):
    url = "https://nutritional-data.p.rapidapi.com/"

    querystring = {"name": food_name}

    headers = {
        "X-RapidAPI-Key": "xxxxx",
        "X-RapidAPI-Host": "nutritional-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            for food_info in data['result']:
                name = food_info['name']
                calories = food_info['calories']
                print(f"{name}, Calories: {calories}")
        else:
            print("No information found for the specified food.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    food_name = input("Enter the name of the food you want to find: ")
    find_food_calories(food_name)




