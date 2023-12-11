import requests

def get_food_data(food_name):
    url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

    query_params = {
        "nutrition-type": "cooking",
        "category[0]": "generic-foods",
        "health[0]": "alcohol-free",
        "ingr": food_name  # Add a parameter for the food name
    }

    headers = {
        "X-RapidAPI-Key": "9f266e8bd5msh2ef26fbb786638dp1ec1dcjsn95d802f33f18",
        "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=query_params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()

        if not data.get('hints'):
            print("No nutritional information found for this food.")
            return None

        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
        return None

def display_food_info(food_data):
    if not food_data:
        print("Failed to retrieve food data.")
        return

    # Extract relevant information for display
    food_name = food_data.get('hints', [{}])[0].get('food', {}).get('label', 'Unknown Food')
    nutrients = food_data.get('hints', [{}])[0].get('food', {}).get('nutrients', {})

    # Display information
    print(f"Food Name: {food_name}")
    print("Nutritional Information:")
    print(f"  - Calories: {nutrients.get('ENERC_KCAL', 'N/A')} kcal")
    print(f"  - Protein: {nutrients.get('PROCNT', 'N/A')} g")
    print(f"  - Fat: {nutrients.get('FAT', 'N/A')} g")
    print(f"  - Carbohydrates: {nutrients.get('CHOCDF', 'N/A')} g")

def main():
    while True:
        food_name = input("Enter a food name to get nutritional information (or 'exit' to quit): ")
        
        if food_name.lower() == 'exit':
            print("Thank you for using the app.")
            break
        
        food_data = get_food_data(food_name)
        display_food_info(food_data)

if __name__ == "__main__":
    main()