#!/usr/bin/env python

import csv

import proof

def load_data(data):
    # Load the data
    with open('example.csv') as f:
        reader = csv.DictReader(f, fieldnames=['name', 'salary'])
        reader.next()
        data['table'] = list(reader)

def select_rows(data):
    # Select relevant rows from the table
    data['low_income'] = filter(lambda r: int(r['salary']) < 20000, data['table'])

def calculate_average(data):
    # The average of a value in the rows is taken
    data['mean'] = sum([int(r['salary']) for r in data['low_income']]) / len(data['low_income'])

@proof.never_cache
def print_results(data):
    print(data['mean'])

data_loaded = proof.Analysis(load_data)
rows_selected = data_loaded.then(select_rows)
average_calculated = rows_selected.then(calculate_average)
average_calculated.then(print_results)

data_loaded.run()
