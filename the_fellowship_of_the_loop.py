# -*- coding: utf-8 -*-
# Copyright (c) 2018,
# Sebastian Barzaghi <sebastian.barzaghi@studio.unibo.it>,
# Martina Dello Buono <martina.dellobuono@studio.unibo.it>,
# Fabio Mariani <fabio.mariani6@studio.unibo.it>,
# Silvio Peroni <silvio.peroni@unibo.it>
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

# The following importing line is used to include in the definition of this class
# the particular functions implemented by a group. The 'my_test_group' module specified
# here is just a placeholder, since it defines only the signature of the various
# functions but it returns always None.

import csv
from csv import DictReader
from re import search
from anytree import Node
from collections import Counter
from networkx import DiGraph, MultiDiGraph


def process_citation_data(file_path):
    with open("citations_sample.csv", 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [dict(row) for row in reader]
    return data


def do_citation_graph(data, sse):
    cit_graph = MultiDiGraph()

    for dict in data:
        if dict["known refs"]:
            searched_doi = sse.search(dict["doi"], "doi", False)
            current_pretty_node = sse.pretty_print(searched_doi)[0]

            for ref in dict["known refs"].split("; "):
                searched_ref = sse.search(ref, "doi", False)
                pretty_ref_node = sse.pretty_print(searched_ref)[0]
                cit_graph.add_edge(current_pretty_node, pretty_ref_node)

    return cit_graph

def do_coupling(data, sse, doi_1, doi_2):
    return None


def do_aut_coupling(data, sse, aut_1, aut_2):
    return None


def do_aut_distance(data, sse, aut):
    return None


def do_find_cycles(data, sse):
    return None


def do_cit_count_year(data, sse, aut, year):
    return None
