#!/usr/bin/python

import math

# Space Complexity O(1)
# Time Complexity O(n)


def recipe_batches(recipe, ingredients):
    lowest = None
    for item in recipe:
        if item not in ingredients.keys():
            return 0
        amount = ingredients[item]//recipe[item]
        if not amount:
            return 0
        if lowest is None or lowest > amount:
            lowest = amount
    return lowest


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}."
          .format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
