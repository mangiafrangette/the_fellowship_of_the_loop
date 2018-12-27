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
from csv import DictReader
from re import search
from anytree import Node
from collections import Counter
from networkx import DiGraph, MultiDiGraph
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
    coupling_strength = 0
    coupling_list = []
    for dict in data:
        if doi_1 == dict["doi"] or doi_2 == dict["doi"] and dict["known refs"]:
            coupling_list.extend(dict["known refs"].split("; "))
    coupling_set = set(coupling_list)
    coupling_strength = len(coupling_list) - len(coupling_set)
    return coupling_strength

def do_aut_coupling(data, sse, aut_1, aut_2):
    aut_coupling_list = []
    for dict in sse.data:
        if (aut_1 in dict["authors"].split("; ") and aut_2 not in dict["authors"].split("; ")) or (aut_2 in dict["authors"].split("; ") and aut_1 not in dict["authors"].split("; ")):
           for dict2 in data:
               if dict["doi"] == dict2["doi"] and dict2["known refs"]:
                   aut_coupling_list.extend(dict2["known refs"].split("; "))
    aut_coupling_set = set(aut_coupling_list)
    aut_coupling_strength = len(aut_coupling_list) - len(aut_coupling_set)
    return aut_coupling_strength


def do_aut_distance(data, sse, aut):
    return None


def do_find_cycles(data, sse):
    return None


def do_cit_count_year(data, sse, aut, year):
    return None
