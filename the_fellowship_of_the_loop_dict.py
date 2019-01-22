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

from collections import *
from csv import DictReader
from collections import Counter
from networkx import *


def process_citation_data(file_path):

    with open(file_path, 'r', encoding='utf-8') as csvfile:  # csvfile it's a variable
        reader = DictReader(csvfile)  # DictReader it's a module needed for reading .csv files
        data = defaultdict(dict)  # our data structure: in defaultdict(dict) the values assigned to keys are dictionaries
        for row in reader:  # iteration over "rows" in .csv file
            data[row["doi"]] = dict(row)  # the keys of the macrodict are values contained under "doi" column. their values are subdictionaries.
            data[row["doi"]]["known refs"] = set(data[row["doi"]]["known refs"].split()).difference({""})
    return data


def do_citation_graph(data, sse):
    cit_graph = DiGraph()  # is not possible to have more than one edge going in to same direction between two nodes.

    for doi, dict in data.items():  # data is our macrodictionary. items() returns (key, value) tuple pairs
        if dict["known refs"]:
            searched_doi = [meta_search(sse, dict["doi"])]  # must be a list with one element because of pretty print
            current_pretty_node = sse.pretty_print(searched_doi)[0]  # [0] is to access the list

            for ref in dict["known refs"].split("; "):
                searched_ref = [meta_search(sse, ref)]  # same search but with the doi present in known refs
                pretty_ref_node = sse.pretty_print(searched_ref)[0]
                cit_graph.add_edge(current_pretty_node, pretty_ref_node)  # actual creation of the graph.
    return cit_graph


def do_coupling(data, sse, doi_1, doi_2):
    coupling_list = []
    coupling_strength = 0
    if doi_1 in data and doi_2 in data:  # added in case the searched doi are not in data.
        if data[doi_1]["known refs"]:
            coupling_list.extend(data[doi_1]["known refs"].split("; "))  # add all the dois contained in known refs to coupling_list
        if data[doi_2]["known refs"]:
            coupling_list.extend(data[doi_2]["known refs"].split("; "))  # same as above
        coupling_set = set(coupling_list)
        coupling_strength = len(coupling_list) - len(coupling_set)
        return coupling_strength
    else:
        return "These DOIs are not in our database. The coupling strength is " + str(coupling_strength)


def do_aut_coupling(data, sse, aut_1, aut_2):
    aut_1_coupling_set = set()
    aut_2_coupling_set = set()
    for dict_sse in sse.data:  # for every dict in metadata
        if data[dict_sse["doi"]]["known refs"]:  # with the previous iteration we found the doi in meta to use for accessing the macrodict's value "known refs"
            aut_split = dict_sse["authors"].split("; ")
            if aut_1 in aut_split and aut_2 not in aut_split:  # it allows to avoid coauthorships
                aut_1_coupling_set.update(data[dict_sse["doi"]]["known refs"].split("; "))
            if aut_2 in aut_split and aut_1 not in aut_split:
                aut_2_coupling_set.update(data[dict_sse["doi"]]["known refs"].split("; "))
    intersection = aut_1_coupling_set.intersection(aut_2_coupling_set)  # intersection finds common DOIs between two sets
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
    return [tuple(l) for l in list(networkx.simple_cycles(do_citation_graph(data, sse)))]


def do_cit_count_year(data, sse, aut, year):
    result_cit_year = {}

    if year:
        for dict in sse.data:
            if aut in dict["authors"].split("; ") and int(dict["year"]) >= year:
                if int(dict["year"]) not in result_cit_year.keys():
                    result_cit_year[int(dict["year"])] = 0
                result_cit_year[int(dict["year"])] += int(data[dict["doi"]]["cited by"])
        for year in range(int(year), max(result_cit_year)): # forse potresti trovare il max durante il ciclo e andare leggermente + veloce, provare
            if year not in result_cit_year.keys():
                    result_cit_year[year] = 0
    else:
        for dict in sse.data:
            if aut in dict["authors"].split("; "):
                if int(dict["year"]) not in result_cit_year.keys():
                    result_cit_year[int(dict["year"])] = 0
                result_cit_year[int(dict["year"])] += int(data[dict["doi"]]["cited by"])
        for year in range(min(result_cit_year), max(result_cit_year)):
            if year not in result_cit_year.keys():
                    result_cit_year[year] = 0
    return result_cit_year


def meta_search(sse, doi_to_search): # given a "doi" (in cit.csv), it'll look the correspondent dict in meta.csv

    for dict in sse.data:
        if doi_to_search == dict["doi"]:
            return dict
