from code.classes import grid

from code.algorithms import random

if __name__ == "__main__":

    # choose which data folder we pick
    data_folder = "district_1"

    # choose the data file name
    data_file = "district-1"

    # Create a grid from our data
    test_grid = grid.Grid(f"data/{data_folder}/{data_file}_houses.csv", f"data/{data_folder}/{data_file}_batteries.csv")
    # print(test_grid)
    print("hoi")

    random.random_assignment(test_grid)

    print("Hoi2")
    b_list = test_grid.batteries[1]
    print(b_list.connect)


