#!/usr/bin/python3
"""Generates a list of cities from csv"""

import csv

def create_cities_dict(filename):
    cities = {}
    # get city names from file
    with open(filename, "r") as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            city, state = row
            cities[city] = state
    return cities

def create_states_id_dict(filename):
    states_id_dict = {}
    with open(filename, "r") as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            id, state = row
            states_id_dict[state] = id
    # print(states_id_dict)
    return states_id_dict

def create_cities_file():
    with open("create_cities.txt", "w") as f:
        states_id_dict = create_states_id_dict("state.csv")
        cities_dict = create_cities_dict("nigeria_cities.csv")
        for key, value in cities_dict.items():
            for key1, value1 in states_id_dict.items():
                if key1 == cities_dict[key]:
                    f.write('create City state_id="{}" name="{}"\n'.format(states_id_dict[key1], key.replace(' ', '_')))

create_cities_file()




# def create_file_from_list(filename, list_name):
#   with open(filename, "w") as f:
#     for element in list_name:
#        f.write("create State name='{}'\n".format(element))

# create_states_id_dict("state.csv")
# create_file_from_list("create_cities.txt", create_cities())
# print(address_generator())
