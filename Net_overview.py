import collections

import networkx as nx
import sys
from operator import itemgetter
import matplotlib.pyplot as plt
import csv
import numpy as np

baci_cc_filename = 'data/BACI/country_codes_V202102.csv'
print(f"Python version {sys.version}")
print(f"networkx version: {nx.__version__}")

baci_cc={}
with open(baci_cc_filename) as cc_file:
        csv_reader = csv.DictReader(cc_file)
        line_count = 0

        for row in csv_reader:
                if line_count == 0:
                        line_count += 1

                baci_cc[int(row['country_code'])] = row['country_name_full']

baci_net_filename = 'net/baci_matching_igo.txt'
igo_net_filename = 'net/IGO_selected_politic_and_military.txt'

BACI_net= nx.read_weighted_edgelist(igo_net_filename,  nodetype=int)
print("***BACI****")
#rozmiar i rząd grafu
print("Whole graph",nx.info(BACI_net))
#The largest connected components
gcc =  sorted(nx.connected_components(BACI_net), key = len, reverse = True)
BACI_conn=BACI_net.subgraph(gcc [0])
print("biggest connected component",nx.info(BACI_conn))
# sredni stopień - sredni przepływ
print('average cash flow value: {}'.format(sum(dict(BACI_conn.degree(weight='weight')).values())/float(len(BACI_conn))))
# sredni stopień
print('average degree: {}'.format(sum(dict(BACI_conn.degree()).values())/float(len(BACI_conn))))
top_countries = sorted(BACI_conn.degree(),key=itemgetter(1),reverse=True)[0:19]
print("kod wierzchołka "+" ; "+ "Nazwa państwa"+" ; "+ "Stopień wierzchołka")
for node, deg in top_countries:
        print(str(node)+" ; "+ str(baci_cc[node])+" ; "+ str(deg))
#średnica grafu i średnia ścieżka
if nx.is_connected(BACI_conn):
        print('average path length: {}'.format(nx.average_shortest_path_length(BACI_conn)))
        print('diameter: {}'.format(nx.diameter(BACI_conn)))


#wykres stopni wierzchołków
degree_freq = nx.degree_histogram(BACI_conn)
degrees = range(len(degree_freq))
plt.figure(1)
plt.title("Vertex degree frequency")
# prep axes
plt.xlabel('degree')
#plt.xscale('log')
plt.xlim(1, max(degrees))
plt.ylabel('frequency')
#plt.yscale('log')
plt.ylim(1, max(degree_freq))
# do plot
plt.scatter(degrees, degree_freq, marker='.')
plt.show()

#dystrybuanta

degree_sequence = sorted([d for n, d in BACI_conn.degree()], reverse=True)  # degree sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
cs = np.cumsum(cnt)
plt.loglog(deg, cs, 'bo')
plt.title("Cumulative Distribution plot")
plt.ylabel("Sample with value > Degree")
plt.xlabel("Degree")
plt.show()

#density
print("density: ",nx.density(BACI_conn))
#closeness
BACI_norm_edges = BACI_conn.copy()
for u,v,d in BACI_norm_edges.edges(data=True):
        d['weight']=1000/d['weight']
closeness = nx.closeness_centrality(BACI_norm_edges, distance='weight')
top_countries = sorted(closeness.items(),key=itemgetter(1),reverse=False)[0:11]
print( "Nazwa państwa"+" ; "+ "Bliskość wierzchołka")
for node, deg in top_countries:
        print( str(baci_cc[node])+" ; "+ str(deg))

#betweenness

betweenness_weighted = nx.betweenness_centrality(BACI_norm_edges,weight= 'weight')
top_countries = sorted(betweenness_weighted.items(),key=itemgetter(1),reverse=False)[0:20]
print( "Nazwa państwa"+" ; "+ "Przechodniość wierzchołka")
for node, deg in top_countries:
        print( str(baci_cc[node])+" ; "+ str(deg))
#przechodniość
transitivity= nx.transitivity(BACI_conn)
print("Transitivity: ",transitivity)