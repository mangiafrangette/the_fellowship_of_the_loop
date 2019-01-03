# -*- coding: utf-8 -*-
# Copyright (c) 2018, Silvio Peroni <essepuntato@gmail.com>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.
#
#
# This file is just a stub of the particular module that every group should
# implement for making its project work. In fact, all these functions returns None,
# which is not compliant at all with the specifications that have been provided at
# https://comp-think.github.io/2018-2019/slides/14%20-%20Project.html

import csv
from collections import Counter
from networkx import nx, DiGraph, MultiDiGraph
from ancillary_functions import *

def process_citation_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [dict(row) for row in reader]
    return data


def do_citation_graph(data, sse): #spiegazione nel commit così non si sporca il codice
    cit_graph = MultiDiGraph()

    for dict in data:
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
    for dict in data:
        if doi_1 == dict["doi"] and dict["known refs"]:
            coupling_list.extend(dict["known refs"].split("; "))
        if doi_2 == dict["doi"] and dict["known refs"]:
            coupling_list.extend(dict["known refs"].split("; "))
    coupling_set = set(coupling_list)
    coupling_strength = len(coupling_list) - len(coupling_set)

    return coupling_strength


def do_aut_coupling(data, sse, aut_1, aut_2):
    aut_1_coupling_list = []
    aut_2_coupling_list = []
    for dict in sse.data:
        aut_split = dict["authors"].split("; ")
        if aut_1 in aut_split and aut_2 not in aut_split:
            dict_citations1 = ricerchina2(data, dict["doi"])
            if dict_citations1["known refs"]:
                aut_1_coupling_list.extend(dict_citations1["known refs"].split("; "))
        if aut_2 in aut_split and aut_1 not in aut_split:
            dict_citations2 = ricerchina2(data, dict["doi"])
            if dict_citations2["known refs"]:
                aut_2_coupling_list.extend(dict_citations2["known refs"].split("; "))
    intersection = set(aut_1_coupling_list).intersection(set(aut_2_coupling_list))
    aut_coupling_strength = len(intersection)
    
    return aut_coupling_strength


def do_aut_distance(data, sse, aut):
    coauthors_to_do = list()
    coauthors_to_do.append(aut)
    coauthors_done = set()
    current_coauthors = []
    coauthors_graph = Graph()
    coauthors_graph.add_node(aut)

    while coauthors_to_do:
        for a in coauthors_to_do:
            if a not in coauthors_done:
                for dict in sse.data:
                    if a in dict['authors'].split('; '):
                        current_coauthors.extend(dict['authors'].split('; '))
                        current_coauthors.remove(a)
                        coauthors_to_do.extend(current_coauthors)
                counted_coauthors = Counter(current_coauthors).items()
                for name, count in counted_coauthors:
                    coauthors_graph.add_edge(a, name, co_authored_papers=count)
                    current_coauthors.clear()
                coauthors_to_do.remove(a)
                coauthors_done.add(a)
                number_edges = nx.shortest_path_length(coauthors_graph, source=a, target=aut)
                coauthors_graph.add_node(a, distance=number_edges)
            else:
                coauthors_to_do.remove(a)
    
    return coauthors_graph


def do_find_cycles(data, sse):
    citation_graph = do_citation_graph(data, sse)
    cycles_list = []
    cycles_list.extend(tuple(i) for i in list(nx.simple_cycles(citation_graph)))
    
    return cycles_list


def do_cit_count_year(data, sse, aut, year):
    result_cit_year = {}

    if year:
        for dict in sse.data:
            if aut in dict["authors"].split("; ") and int(dict["year"]) >= year:
                for dict2 in data:                                              # for lento per la storia di ricerchina2
                    if dict["doi"] == dict2["doi"]:
                        if int(dict["year"]) not in result_cit_year.keys():
                            result_cit_year[int(dict["year"])] = 0
                        result_cit_year[int(dict["year"])] += int(dict2["cited by"])
        for year in range(int(year), max(result_cit_year)): # forse potresti trovare il max durante il ciclo e andare leggermente + veloce, provare
            if year not in result_cit_year.keys():
                    result_cit_year[year] = 0
    else:
        for dict in sse.data:
            if aut in dict["authors"].split("; "):
                for dict2 in data:
                    if dict["doi"] == dict2["doi"]:
                        if int(dict["year"]) not in result_cit_year.keys():
                            result_cit_year[int(dict["year"])] = 0
                        result_cit_year[int(dict["year"])] += int(dict2["cited by"])
        for year in range(min(result_cit_year), max(result_cit_year)):
            if year not in result_cit_year.keys():
                    result_cit_year[year] = 0
    
    return result_cit_year
