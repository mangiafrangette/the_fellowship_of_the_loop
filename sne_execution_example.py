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

# import the class 'ScholarlyNetworkEngine' from the local file 'sne.py'
from sne import ScholarlySearchEngine, ScholarlyNetworkEngine
import time
# create a new object of the class 'ScholarlyNetworkEngine' specifying the input CSV files to process
#my_sne = ScholarlyNetworkEngine("metadata_sample.csv", "citation_sample.py")

# my_sne.<method> ...
my_sse = ScholarlySearchEngine("metadata_sample.csv")
my_sne = ScholarlyNetworkEngine("metadata_sample.csv", "citations_sample.csv")

def test_citation_graph(my_sne):
    start = time.perf_counter()
    my_graph = my_sne.citation_graph()
    end = time.perf_counter()
    print(end - start)
# outputs graph construction: 0.0006471999999999589, 0.0004990999999999746
    start = time.perf_counter()
    my_graph = my_sne.citation_graph()
    my_graph.edges()
    end = time.perf_counter()
    print(end - start)
# outputs getting edges: 0.0004309999999999592, 0.0004283000000000481
    return my_graph
# print(test_citation_graph(my_sne))


def test_coupling(my_sne):
    start = time.perf_counter()
    for dict1 in my_sse.data:
        for dict2 in my_sse.data:
            my_sne.coupling(dict1["doi"], dict2["doi"])
    end = time.perf_counter()
    print(end - start)
# outputs: 0.5619739, 0.5779999999999998
    return my_sne
# print(test_coupling(my_sne))


def test_aut_coupling(my_sne):
    start = time.perf_counter()
    my_sne.aut_coupling("Mark D., Wilkinson", "Arfon M., Smith")
    end = time.perf_counter()
    print(end - start)
    print(my_sne.aut_coupling("Mark D., Wilkinson", "Arfon M., Smith"))
# outputs for Mark...: 0.0001841000000002424
    start = time.perf_counter()
    my_sne.aut_coupling("Bo, Xiao", "Chewei, Huang")
    end = time.perf_counter()
    print(end - start)
    print(my_sne.aut_coupling("Bo, Xiao", "Chewei, Huang"))
# outputsfor Bo...: 0.00012900000000004574
    return my_sne
# print(test_aut_coupling(my_sne))

def test_aut_distance(my_sne):
    start = time.perf_counter()
    aut_distance_graph = my_sne.aut_distance("Mark D., Wilkinson")
    end = time.perf_counter()
    print(end - start)
# outputs: 0.010217700000000107, 0.009736399999999978, 0.011074499999999987
    start = time.perf_counter()
    aut_distance_graph.edges.data("co_authored_papers")
    end = time.perf_counter()
    print(end - start)
    print(aut_distance_graph.edges.data("co_authored_papers"))
# outputs: 0.009627599999999958, 1.1999999999900979e-05
    start = time.perf_counter()
    aut_distance_graph.edges.data("distance")
    end = time.perf_counter()
    print(end - start)
    print(aut_distance_graph.edges.data("distance"))
# outputs: 0.01012040000000014, 8.89999999997837e-06
    return aut_distance_graph
# print(test_aut_distance(my_sne))

def test_find_cycles(my_sne):
    start = time.perf_counter()
    my_sne.find_cycles()
    end = time.perf_counter()
    print(end - start)
# outputs: 0.001483499999999971, 0.001196299999999928
    return my_sne.find_cycles()
# print(test_find_cycles(my_sne))

def test_cit_count_year(my_sne):
    start = time.perf_counter()
    my_sne.cit_count_year("Michel, Dumontier", 2013)
    end = time.perf_counter()
    print(end - start)
    
# outputs: 0.0002022999999999886, 0.00018609999999996685
    return my_sne.cit_count_year("Michel, Dumontier", 2013)
# print(test_cit_count_year(my_sne))
