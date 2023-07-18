import csv
import copy
import math
from typing import List


"""
CSV / DATA LOADING
------------------
"""
def read_csv(file_path: str) -> List[str]:
    """A function to load csv

    Args:
        file_path (str): A path to the file

    Returns:
        List[str]: The CSV rows
    """
    # init
    data = []
    # load
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(list(row.values()))
    return data


def convert_list_of_str_to_float(my_list: List[str]) -> List[float]:
    """A function to convert a list of strings into a list of floats

    Args:
        my_list (List[str]): A list of strings

    Returns:
        List[float]: A list of floats
    """
    return [float(item) for item in my_list]


"""
MATH
----
"""
def list_pythag(point_a: List[float], point_b: List[float]) -> float:
    """A function to preform the pythag theorm on 2 lists, given that they are of matching sizes

    Args:
        point_a (List[float]): the location of the first point
        point_b (List[float]): the location of the second point

    Returns:
        float: _description_
    """
    vector_delta_squared = [
        (axis_a - axis_b) ** 2 for axis_a, axis_b in zip(point_a, point_b)
    ]
    return math.sqrt(sum(vector_delta_squared))


def list_calculate_mean(lists: List[List[float]]) -> List[float]:
    """A function to find the mean value of a lists of lists assuming all are same size
    ex.
    input:  [ [ 0, 0, 1 ], [ 1, 0, 1 ] ]
    output: [ .5, 0, 1 ]

    Args:
        lists (List[List[float]]): A list of lists to find the mean of

    Returns:
        List[float]: the mean of the lists
    """
    # init
    mean_list = []
    list_length = len(lists)
    # cool way to itterate over the transumation of the lists (works only for 2D lists)
    for values in zip(*lists):
        # finding the mean and appending it to our mean_list
        mean = sum(values) / list_length
        mean_list.append(mean)

    return mean_list

if __name__ == "__main__":
    data = read_csv('../assets/data/starbucks_drinks.csv')
    html_automation = open("template.html","w")
    my_code = ""
    for index, drink in enumerate(data):
        my_code += f'''
<!-- {drink[0]} -->
<div class = "row" >
    <div class = "col-sm-1"></div>
    <div class = "col-sm-10">
        <input class="form-check-input" type="checkbox" value="" id="{drink[0].lower().replace(' ','-')}" onclick="console.log({index})">
        <label class="form-check-label" for="{drink[0].lower().replace(' ','-')}">{drink[0].capitalize()}</label>
    </div>
    <div class = "col-sm-1"></div>
</div>
'''
    html_automation.write(my_code)
    html_automation.close()