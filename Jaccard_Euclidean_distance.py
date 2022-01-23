#Macierze sąsiedztwa - dadzą one ogólny wgląd w strukturę sieci oraz możliwość obliczenia
# #dystansu Euclidesowego i Jaccard’a dla wersji sieci bez wag i ważonego dystansu Jaccard’a.
import math
import csv
import networkx as nx
from operator import itemgetter
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

baci_cc_filename = 'data/BACI/country_codes_V202102.csv'

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

def euclid_dist_matrix(A,B):
    distance=[[0]*A.shape[0]]*A.shape[0]
    for i in range(0, A.shape[0]):
        for k in range(0, A.shape[0]):
            distance[i][k]=math.sqrt(pow(A[i,k]-B[i,k],2))
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

def jaccard_dist_matrix(A,B):
    distance=[[0]*A.shape[0]]*A.shape[0]
    for i in range(0, A.shape[0]):
        up=0
        low=0
        for k in range(0, A.shape[0]):
            up+=min(A[i,k],B[i,k])
            low += max(A[i, k], B[i, k])
            distance[i][k]=(1-(up/low))
    return distance

#calculate Euclide distance
print(BACI_adjacency_matrix_norm.shape)
print(IGO_adjacency_matrix_norm.shape)
distance = jaccard_dist(BACI_adjacency_matrix_norm,IGO_adjacency_matrix_norm)
distance_to_code ={}
for node in range(0,len(BACI_net.nodes())):
    distance_to_code[list(BACI_net.nodes())[node]]=distance[node]
top_countries = sorted(distance_to_code.items(),key=itemgetter(1),reverse=False)[0:10]
print( "Nazwa państwa"+" ; "+ "Odległość")
for node, deg in top_countries:
        print( str(baci_cc[node])+" ; "+ str(deg))

print(sum(distance_to_code.values())/len(distance_to_code.values()))

#JACCARD MATRIX
distance_jaccard = jaccard_dist_matrix(IGO_adjacency_matrix_norm.todense(),BACI_adjacency_matrix_norm.todense())
#EUCLID MATRIX
distance_euclid = euclid_dist_matrix(IGO_adjacency_matrix_norm.todense(),BACI_adjacency_matrix_norm.todense())
#print(distance_euclid)

plt.imshow(distance_jaccard)
plt.show()