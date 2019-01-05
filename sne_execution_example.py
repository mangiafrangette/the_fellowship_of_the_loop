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
# outputs graph construction with list: 0.0006471999999999589, with dict: 0.0004889000000000143
    start = time.perf_counter()
    my_graph = my_sne.citation_graph()
    my_graph.edges()
    end = time.perf_counter()
    print(end - start)
    print(my_graph.edges())
    dict_version = [('Sateli B, Löffler F, König-Ries B, Witte R. (2017). ScholarLens: extracting competences from research publications for the automatic generation of semantic user profiles. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.121', 'Sateli B, Witte R. (2015). Semantic representation of scientific literature: bringing claims, contributions and named entities onto the Linked Open Data cloud. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.37'), ('Fan R, Xu K, Zhao J. (2017). A GPU-based solution for fast calculation of the betweenness centrality in large weighted networks. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.140', 'Mitchell R, Frank E. (2017). Accelerating the XGBoost algorithm using GPU computing. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.127'), ('Schleicher JM, Vögler M, Inzinger C, Dustdar S. (2017). Modeling and management of usage-aware distributed datasets for global Smart City Application Ecosystems. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.115', 'Schleicher JM, Vögler M, Inzinger C, Dustdar S. (2016). Smart Brix—a continuous evolution framework for container application deployments. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.66'), ('Salatino AA, Osborne F, Motta E. (2017). How are topics born? Understanding the research dynamics preceding the emergence of new areas. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.119', 'Wu Y, Venkatramanan S, Chiu DM. (2016). Research collaboration and topic trends in Computer Science based on top active authors. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.41'), ('Destefanis G, Ortu M, Counsell S, Swift S, Marchesi M, Tonelli R. (2016). Software development: do good manners matter?. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.73', 'Graziotin D, Wang X, Abrahamsson P. (2015). How do you feel, developer? An explanatory theory of the impact of affects on programming performance. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.18'), ('Smith AM, Katz DS, Niemeyer KE. (2016). Software citation principles. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.86', 'Starr J, Castro E, Crosas M, Dumontier M, Downs RR, Duerr R, Haak LL, Haendel M, Herman I, Hodson S, Hourclé J, Kratz JE, Lin J, Nielsen LH, Nurnberger A, Proell S, Rauber A, Sacchi S, Smith A, Taylor M, Clark T. (2015). Achieving human and machine accessibility of cited data in scholarly publications. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.1'), ('Krewinkel A, Winkler R. (2017). Formatting Open Science: agilely creating multiple document formats for academic manuscripts with Pandoc Scholar. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.112', 'Smith AM, Katz DS, Niemeyer KE. (2016). Software citation principles. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.86'), ('Kuhn T, Chichester C, Krauthammer M, Queralt-Rosinach N, Verborgh R, Giannakopoulos G, Ngonga Ngomo A, Viglianti R, Dumontier M. (2016). Decentralized provenance-aware publishing with nanopublications. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.78', 'Golden P, Shaw R. (2016). Nanopublication beyond the sciences: the PeriodO period gazetteer. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.44'), ('Wilkinson MD, Verborgh R, Bonino da Silva Santos LO, Clark T, Swertz MA, Kelpin FD, Gray AJ, Schultes EA, van Mulligen EM, Ciccarese P, Kuzniar A, Gavai A, Thompson M, Kaliyaperumal R, Bolleman JT, Dumontier M. (2017). Interoperability and FAIRness through a novel combination of Web technologies. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.110', 'Starr J, Castro E, Crosas M, Dumontier M, Downs RR, Duerr R, Haak LL, Haendel M, Herman I, Hodson S, Hourclé J, Kratz JE, Lin J, Nielsen LH, Nurnberger A, Proell S, Rauber A, Sacchi S, Smith A, Taylor M, Clark T. (2015). Achieving human and machine accessibility of cited data in scholarly publications. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.1'), ('Wilkinson MD, Verborgh R, Bonino da Silva Santos LO, Clark T, Swertz MA, Kelpin FD, Gray AJ, Schultes EA, van Mulligen EM, Ciccarese P, Kuzniar A, Gavai A, Thompson M, Kaliyaperumal R, Bolleman JT, Dumontier M. (2017). Interoperability and FAIRness through a novel combination of Web technologies. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.110', 'Kuhn T, Chichester C, Krauthammer M, Queralt-Rosinach N, Verborgh R, Giannakopoulos G, Ngonga Ngomo A, Viglianti R, Dumontier M. (2016). Decentralized provenance-aware publishing with nanopublications. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.78'), ('Konstantinidis K, Papadopoulos S, Kompatsiaris Y. (2017). Exploring Twitter communication dynamics with evolving community analysis. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.107', 'Nikolov D, Oliveira DF, Flammini A, Menczer F. (2015). Measuring online social bubbles. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.38'), ('Konstantinidis K, Papadopoulos S, Kompatsiaris Y. (2017). Exploring Twitter communication dynamics with evolving community analysis. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.107', 'Topirceanu A, Udrescu M, Vladutiu M, Marculescu R. (2016). Tolerance-based interaction: a new model targeting opinion formation and diffusion in social networks. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.42'), ('Smith AM, Niemeyer KE, Katz DS, Barba LA, Githinji G, Gymrek M, Huff KD, Madan CR, Cabunoc Mayes A, Moerman KM, Prins P, Ram K, Rokem A, Teal TK, Valls Guimera R, Vanderplas JT. (2018). Journal of Open Source Software (JOSS): design and first-year review. PeerJ Computer Science 4. https://doi.org/10.7717/peerj-cs.147', 'Starr J, Castro E, Crosas M, Dumontier M, Downs RR, Duerr R, Haak LL, Haendel M, Herman I, Hodson S, Hourclé J, Kratz JE, Lin J, Nielsen LH, Nurnberger A, Proell S, Rauber A, Sacchi S, Smith A, Taylor M, Clark T. (2015). Achieving human and machine accessibility of cited data in scholarly publications. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.1'), ('Smith AM, Niemeyer KE, Katz DS, Barba LA, Githinji G, Gymrek M, Huff KD, Madan CR, Cabunoc Mayes A, Moerman KM, Prins P, Ram K, Rokem A, Teal TK, Valls Guimera R, Vanderplas JT. (2018). Journal of Open Source Software (JOSS): design and first-year review. PeerJ Computer Science 4. https://doi.org/10.7717/peerj-cs.147', 'Smith AM, Katz DS, Niemeyer KE. (2016). Software citation principles. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.86'), ('Nikolić DD. (2018). Parallelisation of equation-based simulation programs on heterogeneous computing systems. PeerJ Computer Science 4. https://doi.org/10.7717/peerj-cs.160', 'Nikolić DD. (2016). DAE Tools: equation-based object-oriented modelling, simulation and optimisation software. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.54')]
    list_version = [('Sateli B, Löffler F, König-Ries B, Witte R. (2017). ScholarLens: extracting competences from research publications for the automatic generation of semantic user profiles. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.121', 'Sateli B, Witte R. (2015). Semantic representation of scientific literature: bringing claims, contributions and named entities onto the Linked Open Data cloud. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.37'), ('Fan R, Xu K, Zhao J. (2017). A GPU-based solution for fast calculation of the betweenness centrality in large weighted networks. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.140', 'Mitchell R, Frank E. (2017). Accelerating the XGBoost algorithm using GPU computing. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.127'), ('Schleicher JM, Vögler M, Inzinger C, Dustdar S. (2017). Modeling and management of usage-aware distributed datasets for global Smart City Application Ecosystems. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.115', 'Schleicher JM, Vögler M, Inzinger C, Dustdar S. (2016). Smart Brix—a continuous evolution framework for container application deployments. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.66'), ('Salatino AA, Osborne F, Motta E. (2017). How are topics born? Understanding the research dynamics preceding the emergence of new areas. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.119', 'Wu Y, Venkatramanan S, Chiu DM. (2016). Research collaboration and topic trends in Computer Science based on top active authors. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.41'), ('Destefanis G, Ortu M, Counsell S, Swift S, Marchesi M, Tonelli R. (2016). Software development: do good manners matter?. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.73', 'Graziotin D, Wang X, Abrahamsson P. (2015). How do you feel, developer? An explanatory theory of the impact of affects on programming performance. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.18'), ('Smith AM, Katz DS, Niemeyer KE. (2016). Software citation principles. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.86', 'Starr J, Castro E, Crosas M, Dumontier M, Downs RR, Duerr R, Haak LL, Haendel M, Herman I, Hodson S, Hourclé J, Kratz JE, Lin J, Nielsen LH, Nurnberger A, Proell S, Rauber A, Sacchi S, Smith A, Taylor M, Clark T. (2015). Achieving human and machine accessibility of cited data in scholarly publications. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.1'), ('Krewinkel A, Winkler R. (2017). Formatting Open Science: agilely creating multiple document formats for academic manuscripts with Pandoc Scholar. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.112', 'Smith AM, Katz DS, Niemeyer KE. (2016). Software citation principles. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.86'), ('Kuhn T, Chichester C, Krauthammer M, Queralt-Rosinach N, Verborgh R, Giannakopoulos G, Ngonga Ngomo A, Viglianti R, Dumontier M. (2016). Decentralized provenance-aware publishing with nanopublications. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.78', 'Golden P, Shaw R. (2016). Nanopublication beyond the sciences: the PeriodO period gazetteer. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.44'), ('Wilkinson MD, Verborgh R, Bonino da Silva Santos LO, Clark T, Swertz MA, Kelpin FD, Gray AJ, Schultes EA, van Mulligen EM, Ciccarese P, Kuzniar A, Gavai A, Thompson M, Kaliyaperumal R, Bolleman JT, Dumontier M. (2017). Interoperability and FAIRness through a novel combination of Web technologies. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.110', 'Starr J, Castro E, Crosas M, Dumontier M, Downs RR, Duerr R, Haak LL, Haendel M, Herman I, Hodson S, Hourclé J, Kratz JE, Lin J, Nielsen LH, Nurnberger A, Proell S, Rauber A, Sacchi S, Smith A, Taylor M, Clark T. (2015). Achieving human and machine accessibility of cited data in scholarly publications. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.1'), ('Wilkinson MD, Verborgh R, Bonino da Silva Santos LO, Clark T, Swertz MA, Kelpin FD, Gray AJ, Schultes EA, van Mulligen EM, Ciccarese P, Kuzniar A, Gavai A, Thompson M, Kaliyaperumal R, Bolleman JT, Dumontier M. (2017). Interoperability and FAIRness through a novel combination of Web technologies. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.110', 'Kuhn T, Chichester C, Krauthammer M, Queralt-Rosinach N, Verborgh R, Giannakopoulos G, Ngonga Ngomo A, Viglianti R, Dumontier M. (2016). Decentralized provenance-aware publishing with nanopublications. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.78'), ('Konstantinidis K, Papadopoulos S, Kompatsiaris Y. (2017). Exploring Twitter communication dynamics with evolving community analysis. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.107', 'Nikolov D, Oliveira DF, Flammini A, Menczer F. (2015). Measuring online social bubbles. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.38'), ('Konstantinidis K, Papadopoulos S, Kompatsiaris Y. (2017). Exploring Twitter communication dynamics with evolving community analysis. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.107', 'Topirceanu A, Udrescu M, Vladutiu M, Marculescu R. (2016). Tolerance-based interaction: a new model targeting opinion formation and diffusion in social networks. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.42'), ('Smith AM, Niemeyer KE, Katz DS, Barba LA, Githinji G, Gymrek M, Huff KD, Madan CR, Cabunoc Mayes A, Moerman KM, Prins P, Ram K, Rokem A, Teal TK, Valls Guimera R, Vanderplas JT. (2018). Journal of Open Source Software (JOSS): design and first-year review. PeerJ Computer Science 4. https://doi.org/10.7717/peerj-cs.147', 'Starr J, Castro E, Crosas M, Dumontier M, Downs RR, Duerr R, Haak LL, Haendel M, Herman I, Hodson S, Hourclé J, Kratz JE, Lin J, Nielsen LH, Nurnberger A, Proell S, Rauber A, Sacchi S, Smith A, Taylor M, Clark T. (2015). Achieving human and machine accessibility of cited data in scholarly publications. PeerJ Computer Science 1. https://doi.org/10.7717/peerj-cs.1'), ('Smith AM, Niemeyer KE, Katz DS, Barba LA, Githinji G, Gymrek M, Huff KD, Madan CR, Cabunoc Mayes A, Moerman KM, Prins P, Ram K, Rokem A, Teal TK, Valls Guimera R, Vanderplas JT. (2018). Journal of Open Source Software (JOSS): design and first-year review. PeerJ Computer Science 4. https://doi.org/10.7717/peerj-cs.147', 'Smith AM, Katz DS, Niemeyer KE. (2016). Software citation principles. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.86'), ('Nikolić DD. (2018). Parallelisation of equation-based simulation programs on heterogeneous computing systems. PeerJ Computer Science 4. https://doi.org/10.7717/peerj-cs.160', 'Nikolić DD. (2016). DAE Tools: equation-based object-oriented modelling, simulation and optimisation software. PeerJ Computer Science 2. https://doi.org/10.7717/peerj-cs.54')]
    print(sorted(dict_version) == sorted(list_version))
# outputs getting edges with list: 0.0004309999999999592, 0.0004283000000000481, with dict: 0.0004733000000000098
    return my_graph
# print(test_citation_graph(my_sne))

# for dicts version
def test_coupling_dicts(my_sne):
    start = time.perf_counter()
    for doi1 in my_sne.data:
        for doi2 in my_sne.data:
            my_sne.coupling(doi1, doi2)
    end = time.perf_counter()
    print(end - start)
# outputs pc fra: 0.5779999999999998, with dicts: 0.02035980000000004
    return my_sne
print(test_coupling_dicts(my_sne))

# for list version
def test_coupling(my_sne):
    start = time.perf_counter()
    for doi1 in my_sse.data:
        for doi2 in my_sse.data:
            my_sne.coupling(doi1, doi2)
    end = time.perf_counter()
    print(end - start)
# outputs pc fra: 0.5779999999999998, with dicts: 0.03266860000000005
    return my_sne
# print(test_coupling(my_sne))

# controllo correttezza risultati:
# list_output for my_sne.coupling("10.7717/peerj-cs.86", "10.7717/peerj-cs.110") = 1
# dicts_output for my_sne.coupling("10.7717/peerj-cs.86", "10.7717/peerj-cs.110") = 1
# ---
# list_output for my_sne.coupling("10.7717/peerj-cs.58", "10.7717/peerj-cs.14") = 0
# dicts_output for my_sne.coupling("10.7717/peerj-cs.58", "10.7717/peerj-cs.14") = 0
# ---
# list_output for my_sne.coupling("10.7717/peerj-cs.78", "10.7717/peerj-cs.78") = 1
# dicts_output for my_sne.coupling("10.7717/peerj-cs.78", "10.7717/peerj-cs.78") = 1


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
