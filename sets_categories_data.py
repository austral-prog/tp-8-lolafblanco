# pylint: disable-all
# flake8: noqa,

ALCOHOLS = {
    'vodka', 'rum', 'whiskey', 'tequila', 'gin', 'brandy', 'vermouth', 'triple sec',
    'cognac', 'bourbon', 'scotch', 'absinthe', 'liqueur', 'champagne', 'beer', 'wine'
}

def check_drinks(drink_name, ingredients):
    # Check if any of the ingredients are in the ALCOHOLS set
    if any(ingredient in ALCOHOLS for ingredient in ingredients):
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"
