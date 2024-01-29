#displaying all the products listed in the food_list
def display_products():
    try:
        with open('food_list.txt', 'r') as file:
            print("ID\tName\t\tStatus")
            print("--------------------------------")
            for line in file:
                product_id, name, _, _, _, status = line.strip().split(',')
                print(f"{product_id}\t{name.ljust(15)}\t{status}")
    except FileNotFoundError:
        print("No products found.")

#overwritting status of the food stored
def update_status(product_id, new_status):
    try:
        with open('food_list.txt', 'r') as file:
            lines = file.readlines()

        with open('food_list.txt', 'w') as file:
            for line in lines:
                current_id, *rest = line.strip().split(',')
                current_status = rest[-1].strip().lower()
                new_status_lower = new_status.lower()
                if current_id == product_id and current_status != new_status_lower:
                    line = line.replace(f",{current_status},", f",{new_status_lower},")
                file.write(line)
    except FileNotFoundError:
        print("No products found.")

#deleting product from the list
def delete_product(product_id):
    try:
        with open('food_list.txt', 'r') as file:
            lines = file.readlines()
        with open('food_list.txt', 'w') as file:
            for line in lines:
                current_id, _, _, _, _, _ = line.strip().split(',')
                if current_id != product_id:
                    file.write(line)
    except FileNotFoundError:
        print("No products found.")

#user commands to change status of the food listed
def active_disactive_delete_product():
    display_products()
    product_id = input("Enter the ID of the product you want to modify or delete: ")
    action = input("Choose action: A for Active, D for Disactive, DEL for Delete): ").upper()

    if action == 'A':
        update_status(product_id, 'active')
        print("Product status updated to Active.")
    elif action == 'D':
        update_status(product_id, 'disactive')
        print("Product status updated to Disactive.")
    elif action == 'DEL':
        delete_product(product_id)
        print("Product deleted.")
    else:
        print("Invalid action. Please choose A for Active, D for Disactive, or DEL for Delete.")

if __name__ == "__main__":
    active_disactive_delete_product()
