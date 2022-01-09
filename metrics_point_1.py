#Macierze sąsiedztwa - dadzą one ogólny wgląd w strukturę sieci oraz możliwość obliczenia
# #dystansu Euclidesowego i Jaccard’a dla wersji sieci bez wag i ważonego dystansu Jaccard’a.
import math

import networkx as nx
import numpy as np
from sklearn.preprocessing import normalize

baci_net_filename = 'net/baci_matching_igo.txt'
igo_net_filename = 'net/IGO_selected_politic_and_military.txt'

BACI_net= nx.read_weighted_edgelist(baci_net_filename,  nodetype=int)
IGO_net= nx.read_weighted_edgelist(igo_net_filename,  nodetype=int)

BACI_adjacency_matrix=nx.adjacency_matrix(BACI_net)
IGO_adjacency_matrix=nx.adjacency_matrix(IGO_net,nodelist=list(BACI_net.nodes))

#row normalize matrixes
#row_sums = BACI_adjacency_matrix.sum(axis=1)
BACI_adjacency_matrix_norm =normalize(BACI_adjacency_matrix, axis=1, norm='l1')  #BACI_adjacency_matrix / row_sums

#row_sums = IGO_adjacency_matrix.sum(axis=1)
IGO_adjacency_matrix_norm =normalize(IGO_adjacency_matrix, axis=1, norm='l1') #IGO_adjacency_matrix / row_sums

def euclid_dist(A, B):
    distance = []
    for i in range(0, A.shape[0]):
        d=0
        for k in range(0, A.shape[0]):
            d+=pow(A[i,k]-B[i,k],2)
        distance.append(math.sqrt(d))
    return distance

def jaccard_dist(A, B):
    distance = []
    for i in range(0, A.shape[0]):
        up=0
        low=0
        for k in range(0, A.shape[0]):
            up+=min(A[i,k],B[i,k])
            low += max(A[i, k], B[i, k])
        distance.append(1-(up/low))
    return distance

#calculate Euclide distance
print(BACI_adjacency_matrix_norm.shape)
print(IGO_adjacency_matrix_norm.shape)
distance = jaccard_dist(BACI_adjacency_matrix_norm,IGO_adjacency_matrix_norm)
print(len(distance))
#print(distance)