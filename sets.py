from sets_categories_data import (ALCOHOLS)

def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    unicos_ingredients = set(ingredients)
    
    return (dish_name, unicos_ingredients)

def check_drinks(drink_name, ingredients):
    # Check if any of the ingredients are in the ALCOHOLS set
    if any(ingredient in ALCOHOLS for ingredient in ingredients):
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"
