from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
   
    unicos_ingredients = set(ingredients)
    
    return (dish_name, unicos_ingredients)

def check_drinks(drink_name, ingredients):
    # Check if any of the ingredients are in the ALCOHOLS set
    if any(ingredient in ALCOHOLS for ingredient in ingredients):
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"
