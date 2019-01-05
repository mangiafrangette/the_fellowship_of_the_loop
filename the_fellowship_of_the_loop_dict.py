from csv import DictReader
from collections import Counter, defaultdict
from networkx import nx, MultiDiGraph, Graph
from ancillary_functions import *

def process_citation_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
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

def do_coupling(data, sse, doi_1, doi_2):
    coupling_list = []
    coupling_strength = 0
    if data[doi_1]["known refs"]:
        coupling_list.extend(data[doi_1]["known refs"].split("; "))
    if data[doi_2]["known refs"]:
        coupling_list.extend(data[doi_2]["known refs"].split("; "))
    coupling_set = set(coupling_list)
    coupling_strength = len(coupling_list) - len(coupling_set)
    return coupling_strength
