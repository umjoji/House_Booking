#!/usr/bin/python3
"""Generates a list of states from csv"""

import csv

def create_states():
    states = []
    # get state names from file
    with open("nigeria_cities.csv", "r") as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            city, state = row
            states.append(state)
    states = list(set(states))
    states.sort()
    states.remove(states[0])
    return states
    # with open()
    # print(states)
    # print(len(states))

def create_file_from_list(filename, list_name):
  with open(filename, "w") as f:
    for element in list_name:
       f.write('create State name="{}"\n'.format(element.replace(' ', '_')))


create_file_from_list("create_states.txt", create_states())
# print(address_generator())
