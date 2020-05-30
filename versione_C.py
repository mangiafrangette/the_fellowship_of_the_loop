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


from csv import DictReader
from networkx import *
import collections
from collections import Counter
from collections import deque
import time

def process_citation_data(file_path):
    data = dict()

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        for x in reader:
            data[x['doi']] = dict(x)
            data[x['doi']]['known refs'] = set(data[x['doi']]['known refs'].split("; ")).difference({''})
            # data[x['doi']]['pos'] = bin_search(sse.data, "doi", x['doi'])

    return collections.OrderedDict(sorted(data.items()))

def bin_search(dict_list, key, value_to_search, lo=None, hi=None):
    if lo is None:
        lo = 0
    elif lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(dict_list)
    while lo < hi:
        mid = (lo + hi) // 2
        if dict_list[mid][key] < value_to_search:
            lo = mid + 1
        else:
            hi = mid
    return lo



def do_citation_graph(data, sse):
    cit_network = DiGraph()

    for row in data:
        print(data[row]["known refs"])
        if data[row]["known refs"]:
            print("dentro con ", data[row]["doi"])
            pos = bin_search(sse.data, "doi", row)
            print("doi with known refs  ", sse.data[pos]["doi"])
            current_pretty_node = sse.pretty_print([sse.data[pos]])[0]
            for doi_of_cited_node in data[row]['known refs']:
                print("to search: ", doi_of_cited_node)
                pos = bin_search(sse.data, "doi", doi_of_cited_node)
                print("found: ", sse.data[pos]["doi"])
                cit_network.add_edge(current_pretty_node, sse.pretty_print([sse.data[pos]])[0])
            print()

    return cit_network


def do_coupling(data, sse, doi_1, doi_2):
    return len(data[doi_1]["known refs"].intersection(data[doi_2]["known refs"]))


def do_aut_coupling1(data, sse, aut_1, aut_2):
    refs_1_list = list()
    refs_2_list = list()
    for row in sse.data:
        if aut_1 in row["authors"]:
            refs_1_list.extend(data[row["doi"]]["known refs"])
        elif aut_2 in row["authors"]:
            refs_2_list.extend(data[row["doi"]]["known refs"])

    return len(set(refs_1_list).intersection(set(refs_2_list)))

def do_aut_coupling(data, sse, aut_1, aut_2):
    refs_1_set = set()
    refs_2_set = set()
    for row in sse.data:
        if data[row["doi"]]["known refs"]:
            coauthors = row["authors"].split("; ")
            if aut_1 in coauthors and aut_2 not in coauthors:
                refs_1_set.update(data[row["doi"]]["known refs"])
            elif aut_2 in coauthors and aut_1 not in coauthors:
                refs_2_set.update(data[row["doi"]]["known refs"])

    return len(refs_1_set.intersection(refs_2_set))

def do_aut_distance1(data, sse, aut, visited_aut=set(), step=0, coauthor_network=Graph()):
    visited_aut.add(aut)

    coauthors = list()
    coauthor_network.add_node(aut)
    for row in sse.data:
        coauthors_splitted = row['authors'].split('; ')
        if aut in coauthors_splitted:
            for current_coauthor in coauthors_splitted:
                if current_coauthor not in visited_aut:
                    coauthors.append(current_coauthor)

    if coauthors:
        for name, count in Counter(coauthors).items():

            coauthor_network.add_edge(aut, name, co_authored_papers=count)
            if name not in visited_aut:
                coauthor_network = networkx.compose(coauthor_network, do_aut_distance(data, sse, name, visited_aut, step + 1, coauthor_network))

    if step == 0:
        for nodo in coauthor_network.nodes.items():
            # coauthor_network.nodes[nodo[0]]['shortest_path'] = shortest_path(coauthor_network, aut, nodo[0])
            coauthor_network.nodes[nodo[0]]['distance'] = shortest_path_length(coauthor_network, aut, nodo[0])

    return coauthor_network


def do_aut_distance(data, sse, aut):
    coauthorship_dict = dict()
    for row in sse.data:
        splitted_coauthors = row["authors"].split("; ")
        for author in splitted_coauthors:
            if author not in coauthorship_dict:
                coauthorship_dict[author] = list()
            coauthorship_dict[author].extend(splitted_coauthors)
            coauthorship_dict[author].remove(author)

    to_visit = deque()
    to_visit.append(aut)
    visited = set()
    step = 0
    coauthor_network = Graph()
    while len(to_visit) > 0:
        curr_aut = to_visit.pop()
        visited.add(curr_aut)
        #coauthor_network.add_node(curr_aut, distance=step)
        for curr_coauthor, count in Counter(coauthorship_dict[curr_aut]).items():
            #coauthor_network.add_node(curr_coauthor)
            coauthor_network.add_edge(curr_aut, curr_coauthor, co_authored_papers=count)
            #coauthor_network.nodes[curr_coauthor]['distance'] = shortest_path_length(coauthor_network, aut, curr_coauthor)
            if curr_coauthor not in visited:
                to_visit.append(curr_coauthor)

        #step += 1

    for nodo in coauthor_network.nodes.items():
        coauthor_network.nodes[nodo[0]]['distance'] = shortest_path_length(coauthor_network, aut, nodo[0])

    return coauthor_network





def do_find_cycles(data, sse):
    #print(list(networkx.simple_cycles(do_citation_graph(data, sse))))
    #return list(networkx.simple_cycles(do_citation_graph(data, sse)))

    return [tuple(l) for l in list(networkx.simple_cycles(do_citation_graph(data, sse)))]


def do_cit_count_year(data, sse, aut, year):
    result_dict = dict()

    for article in sse.data:
        if year is None or int(article["year"]) >= year:
            if article["year"] not in result_dict:
                result_dict[article["year"]] = 0
            if aut in article["authors"].split("; "):
                result_dict[article["year"]] += int(data[article["doi"]]["cited by"])

    return result_dict
