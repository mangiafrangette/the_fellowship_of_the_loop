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
#print(my_sse.coauthor_network("Tim, Clark"))

my_sne = ScholarlyNetworkEngine("metadata_sample.csv", "citations_sample.csv")
my_graph = my_sne.citation_graph()
#print(my_graph.edges())

start = time.perf_counter()
for dict1 in my_sse.data:
    for dict2 in my_sse.data:
        (my_sne.coupling(dict1["doi"], dict2["doi"]))
end = time.perf_counter()
print(end - start) # da start a qua printa il tempo

print(my_sne.coupling("10.7717/peerj-cs.110", "10.7717/peerj-cs.147")) # questo printa il coupling_strenght

print(my_sne.aut_coupling("Tim, Clark", "Ariel, Rokem")) #printa aut_coupling
print(my_sne.aut_coupling("Arfon M., Smith", "Ariel, Rokem")) #printa aut_coupling escludendo coauthroships

# test di tempo per aut_coupling SBAGLIATO
start = time.perf_counter()
for dict_1 in my_sse.data:
    for dict_2 in my_sse.data:
        aut_split_1 = dict_1["authors"].split("; ")
        aut_split_2 = dict_2["authors"].split("; ")
        for item in aut_split_1:
            for item2 in aut_split_2:
                (my_sne.coupling(item, item2))
end = time.perf_counter()
print(end - start)

#test solo per correttezza risultati di aut_distance
aut_distance_graph = my_sne.aut_distance("Mark D., Wilkinson")
print(aut_distance_graph.edges())
print(aut_distance_graph.edges(data=True))


