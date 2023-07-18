from typing import List
from copy import deepcopy

from pyscript import Element

from starbucks_kmeans.kmeans import GraphPoint, KmeansPoint, kmeans
from starbucks_kmeans.utils import read_csv, convert_list_of_str_to_float, list_pythag, list_calculate_mean

'''
-------------
INITALIZATION
-------------
'''
CSV_DATA = read_csv(file_path="./assets/data/starbucks_drinks.csv")
DRINK_DATA = [
    GraphPoint(location=convert_list_of_str_to_float(data[1:]), name=data[0])
    for data in CSV_DATA
]
# freeing some memory, no longer need the CSV
del CSV_DATA

active_drinks:List[GraphPoint] = []
# A little cheaty foresight after playing around some
drink_id_mapping = {
    1: "Savory Espressos",
    2: "Non-Coffee Frozens",
    3: "Savory Teas",
    4: "Coffee Fraps",
    5: "Coldbrews",
    6: "Hot Non-Coffees",
    7: "Iced Espressos",
    8: "Iced Teas",
    9: "Refreshers",
    10: "Sweet Espressos",
}

'''
------
KMEANS
------
'''
kmeans_points = [
    KmeansPoint(location=DRINK_DATA[0].location, point_id=1),   # Americano
    KmeansPoint(location=DRINK_DATA[1].location, point_id=2),   # Blended Strawberry Lemonade
    KmeansPoint(location=DRINK_DATA[13].location, point_id=3),  # Chai Tea
    KmeansPoint(location=DRINK_DATA[17].location, point_id=4),  # Chocolate Java Mint Frappuccino
    KmeansPoint(location=DRINK_DATA[19].location, point_id=5),  # Cinnamon Caramel Cream Cold Brew
    KmeansPoint(location=DRINK_DATA[44].location, point_id=6),  # Hot Chocolate
    KmeansPoint(location=DRINK_DATA[48].location, point_id=7),  # Iced Blonde Vanilla Latte
    KmeansPoint(location=DRINK_DATA[51].location, point_id=8),  # Iced Chai Tea Latte
    KmeansPoint(location=DRINK_DATA[90].location, point_id=9),  # Pink Drink
    KmeansPoint(location=DRINK_DATA[104].location, point_id=10),  # White Chocolate Mocha
]

kmeans(kmeans_points=kmeans_points, graph_points=DRINK_DATA)

'''
--------------------
DRINK RECOMMENDATION
--------------------
'''
def find_recommended_drink():
    global DRINK_DATA, active_drinks

    drink_data_copy = deepcopy(DRINK_DATA)
    
    if not active_drinks:
        for index in range(5):
            elm = Element(f'recommend-{index+1}')
            elm.element.innerHTML = ""

        elm = Element(f'recommend-name')
        elm.element.innerHTML = "Name:"
        elm = Element(f'recommend-category')
        elm.element.innerHTML = "Category:"
        elm = Element(f'recommend-like')
        elm.element.innerHTML = ""
        return
    
    # Finding the mean of the selected drinks
    personal_preference = list_calculate_mean(
        lists=[drink.location for drink in active_drinks]
    )

    # Finding the distance that all drinks have from your mean of data
    for drink in drink_data_copy:
        drink.nearest_value_distance = list_pythag(
            point_a=personal_preference, point_b=drink.location
        )
    # sorting the drinks (closest to zero is top of list)
    drink_data_copy.sort(key=lambda drink: drink.nearest_value_distance)

    for index in range(5):
        elm = Element(f'recommend-{index+1}')
        elm.element.innerHTML = drink_data_copy[index].name

    elm = Element(f'recommend-name')
    elm.element.innerHTML = f"Name: <span class = 'drink-text-alt'>{drink_data_copy[0].name}<span>"
    elm = Element(f'recommend-category')
    elm.element.innerHTML = f"Category: <span class = 'drink-text-alt'>{drink_id_mapping[drink_data_copy[0].nearest_value_id]}<span>"
    elm = Element(f'recommend-like')
    like_html = "<ul>"
    for drink in DRINK_DATA:
        if drink.nearest_value_id != drink_data_copy[0].nearest_value_id:
            continue
        like_html += f"<li class = 'h5 drink-text' >{drink.name}</li>"
    like_html += "</ul>"
    elm.element.innerHTML = like_html


def toggle_recommended_drink(drink_id:int):
    global DRINK_DATA, active_drinks

    if DRINK_DATA[drink_id] in active_drinks:
        active_drinks.remove(DRINK_DATA[drink_id])
    else:
        active_drinks.append(DRINK_DATA[drink_id])
    
    find_recommended_drink()

    return

def clear_drinks():
    global DRINK_DATA, active_drinks
    active_drinks = []
    for i, drink in enumerate(DRINK_DATA):
        drink_name = drink.name.lower().replace(" ","-")
        drink_elm = Element(drink_name)
        drink_elm.element.checked = False
    
    find_recommended_drink()

    return