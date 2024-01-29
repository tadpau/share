from send_email import send_email
#read last generated and stored meal from meal plan
def read_last_meal_plan():
    try:
        with open('last_meal_plan.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

#user promt if he wants to download and download itself
def handle_meal_plan_download():
    last_meal_plan = read_last_meal_plan()

    if last_meal_plan:
        print("\nLast Generated Meal Plan:")
        print(last_meal_plan)

        download_option = input("Do you want to download the last meal plan? (yes/no): ").lower()

        if download_option == 'yes':
            receiver_email = input("Enter your email address: ")
            send_email(receiver_email, "Your Last Meal Plan", last_meal_plan)
            print("Email sent successfully. Check your email for the last meal plan.")
        else:
            print("Meal plan download was canceled.")
    else:
        print("No last meal plan found.")

if __name__ == "__main__":
    handle_meal_plan_download()

