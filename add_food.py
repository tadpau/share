class ProductManager:
    ALLOWED_FOOD_GROUPS = ['dairy', 'vegetables', 'fruit', 'grains', 'protein']
    ALLOWED_TIME_OF_USAGE = ['morning', 'lunch', 'dinner', 'anytime']

    def __init__(self):
        pass

#checking for available product IDs for the next food to be added
    @staticmethod
    def get_next_product_id(file_path='food_list.txt'):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                existing_ids = {int(line.split(',')[0]) for line in lines}
                next_id = 1
                while next_id in existing_ids:
                    next_id += 1
                return next_id
        except FileNotFoundError:
            return 1

#adding products to the list and checking if they are matching guidelines
    @staticmethod
    def add_product(name, calories_per_100g, food_group, preferred_time, file_path='food_list.txt'):
        if food_group not in ProductManager.ALLOWED_FOOD_GROUPS:
            raise ValueError(f"Invalid food group. Please choose from: {ProductManager.ALLOWED_FOOD_GROUPS}")

        if preferred_time not in ProductManager.ALLOWED_TIME_OF_USAGE:
            raise ValueError(f"Invalid time of usage. Please choose from: {ProductManager.ALLOWED_TIME_OF_USAGE}")

        product_id = ProductManager.get_next_product_id(file_path)
        with open(file_path, 'a') as file:
            file.write(f"{product_id},{name},{calories_per_100g},{food_group},{preferred_time},active\n")
        return product_id

