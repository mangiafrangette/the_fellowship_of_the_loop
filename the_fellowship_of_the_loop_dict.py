import csv
from collections import Counter, defaultdict
from networkx import nx, MultiDiGraph, Graph
from ancillary_functions import *

def process_citation_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = defaultdict(dict)
        for row in reader:
            data[row["doi"]] = dict(row)
    return data
