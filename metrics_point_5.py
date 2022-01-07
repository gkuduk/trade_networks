import networkx as nx
import sys
import matplotlib.pyplot as plt

print(f"Python version {sys.version}")
print(f"networkx version: {nx.__version__}")

baci_net_filename = 'net/baci_matching_igo.txt'
igo_net_filename = 'net/IGO_selected_politic_and_military.txt'

BACI_net= nx.read_weighted_edgelist(baci_net_filename,  nodetype=int)
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
#średnica grafu i średnia ścieżka
if nx.is_connected(BACI_conn):
        print('average path length: {}'.format(nx.average_shortest_path_length(BACI_conn)))
        print('average diameter: {}'.format(nx.diameter(BACI_conn)))


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

#density
print("density: ",nx.density(BACI_conn))
#closeness
closeness = nx.closeness_centrality(BACI_conn)
#betweenness
betweenness = nx.betweenness_centrality(BACI_conn)
betweenness_weighted = nx.betweenness_centrality(BACI_conn,weight= 'weight')
#przechodniość?
