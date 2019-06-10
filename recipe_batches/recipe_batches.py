#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    if len(recipe) > len(ingredients):
        return 0
    # use math.floor
    batches_possible = 0
    for key in recipe.keys():
        print(recipe[key])
        print(ingredients[key])

        batches_possible_with_current_ingedient = math.floor(
            ingredients[key] / recipe[key])
        print(batches_possible_with_current_ingedient)
        if recipe[key] <= ingredients[key] and batches_possible > batches_possible_with_current_ingedient or batches_possible == 0:
            batches_possible = batches_possible_with_current_ingedient

        elif recipe[key] > ingredients[key]:
            return 0
    return batches_possible


# genius solution, using min
def recipe_batches_erick(recipe, ingredients):
    store = []

    if len(ingredients) != len(recipe):
        return 0
    else:
        for i in recipe:
            for j in ingredients:
                if(i == j):
                    store.append(ingredients[j] / recipe[i])
    num_of_batches = int(min(store))

    return num_of_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'cheese': 10}
    ingredients = {'milk': 198, 'butter': 52, 'cheese': 10}

    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
