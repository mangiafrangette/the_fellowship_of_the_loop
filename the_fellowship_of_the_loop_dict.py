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

def do_citation_graph(data, sse):
    cit_graph = DiGraph()

    for doi, dict in data.items():
        if dict["known refs"]:
            searched_doi = [ricerchina(sse, dict["doi"])]
            current_pretty_node = sse.pretty_print(searched_doi)[0]

            for ref in dict["known refs"].split("; "):
                searched_ref = [ricerchina(sse, ref)]
                pretty_ref_node = sse.pretty_print(searched_ref)[0]
                cit_graph.add_edge(current_pretty_node, pretty_ref_node)
    return cit_graph
