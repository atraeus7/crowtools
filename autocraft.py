import pyautogui as page
import time


def click_in_crowfall():
    reset_location = (1742, 1116)
    page.moveTo(reset_location)
    page.mouseDown()
    page.mouseUp()


def load_resource(name: str, qty: int):
    location = page.locateCenterOnScreen('resources/' + name + '.png', confidence=0.9, grayscale=True)
    if location:
        page.moveTo(location)

        for _ in range(0, qty):
            page.mouseDown(button='right')
            page.mouseUp(button='right')


def assemble():
    # Click Assemble
    assemble_loc = page.locateCenterOnScreen('resources/assemble.png', confidence=0.9)
    page.moveTo(assemble_loc)
    page.mouseDown(button='left')
    page.mouseUp(button='left')
    time.sleep(1)

    # Click Next
    next_loc = page.locateCenterOnScreen('resources/next.png', confidence=0.9)
    if next_loc:
        page.moveTo(next_loc)
        page.mouseDown(button='left')
        page.mouseUp(button='left')
        time.sleep(1)

    # Click Make Item
    make_loc = page.locateCenterOnScreen('resources/make_item.png', confidence=0.9)
    if make_loc:
        page.moveTo(make_loc)
        page.mouseDown(button='left')
        page.mouseUp(button='left')
        time.sleep(1)
    else:
        make_loc = page.locateCenterOnScreen('resources/make_item_2.png', confidence=0.9)
        if make_loc:
            page.moveTo(make_loc)
            page.mouseDown(button='left')
            page.mouseUp(button='left')
            time.sleep(1)
        else:
            return False

    # Click Take Item
    take_loc = page.locateCenterOnScreen('resources/take.png', confidence=0.9)
    if take_loc:
        page.moveTo(take_loc)
        page.mouseDown(button='left')
        page.mouseUp(button='left')
        time.sleep(1)
    else:
        take_loc = page.locateCenterOnScreen('resources/take2.png', confidence=0.9)
        if take_loc:
            page.moveTo(take_loc)
            page.mouseDown(button='left')
            page.mouseUp(button='left')
            time.sleep(1)
        else:
            return False

    return True


def open_menu(path: list):
    for token in path:
        location = page.locateCenterOnScreen('resources/' + token + '.png', confidence=0.9)
        if location:
            page.moveTo(location)
            page.mouseDown()
            page.mouseUp()


def close_menu():
    location = page.locateCenterOnScreen('resources/close_all.png', confidence=0.9)
    page.moveTo(location)
    page.mouseDown()
    page.mouseUp()


def assemble_qty(menu, resource_list, qty):
    """
    Assemble qty items

    :param menu:
    :param resource_list: [(name,qty)]
    :param qty
    :return:
    """
    click_in_crowfall()
    open_menu(menu)

    for _ in range(qty):
        for resource in resource_list:
            load_resource(resource[0], resource[1])

        if not assemble():
            close_menu()
            return False

    close_menu()

    return True


def assemble_all(menu, resource_list):
    """
    Assemble all items

    :param menu:
    :param resource_list: [(name,qty)]
    :return:
    """

    click_in_crowfall()
    open_menu(menu)

    done = False

    while not done:
        for resource in resource_list:
            load_resource(resource[0], resource[1])
        if not assemble():
            done = True

    close_menu()


# Meat burgundy
def make_meat(meat, mushroom):
    # Make Cooking Foil
    cooking_foil_path = ['cooking_menu', 'components_menu', 'cooking_foil_menu']
    assemble_all(cooking_foil_path, [('copper', 1)])

    # Make Cooking Pot
    cooking_pot_path = ['cooking_menu', 'components_menu', 'large_cooking_pot_menu']
    assemble_all(cooking_pot_path, [('tin', 1)])

    # Grind Up Items
    item_list = ['garlic', 'ginseng', 'nightshade', 'mandrake_root']
    grind_path = ['cooking_menu', 'components_menu', 'grind_food_items_bulk_menu']

    for item in item_list:
        assemble_all(grind_path, [(item, 1)])

    # Red Wine
    red_wine_path = ['cooking_menu', 'head_chef_menu', 'red_wine_menu']
    ingredients = [('water_flask', 1), ('apple', 1), ('empty_flask', 1), ('sugarcane', 1), ('yeast', 1)]
    assemble_all(red_wine_path, ingredients)

    # Meat Burgundy
    meat_burgundy_path = ['cooking_menu', 'head_chef_menu', 'meat_burgundy_menu']
    assemble_all(meat_burgundy_path,
                 [('crushed_herbs', 1), ('large_cooking_pot', 1), (meat, 1), ('wild_rice', 1), (mushroom, 1),
                  ('carrot', 1), ('red_wine', 1)])


if __name__ == '__main__':
    red_wine_path = ['cooking_menu', 'head_chef_menu', 'red_wine_menu']
    ingredients = [('water_flask', 1), ('apple', 1), ('empty_flask', 1), ('sugarcane', 1), ('yeast', 1)]
    assemble_all(red_wine_path, ingredients)

# assemble_qty(['cooking_menu', 'campfire_cooking_menu', 'yeast_menu'],
#              [('b_mushroom', 1), ('water_flask', 1), ('cooking_foil', 1)], 2)
