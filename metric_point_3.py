import matplotlib.pyplot as plt
import sys, os
import itertools
import networkx as nx
import numpy as np
from portrait_divergence import portrait_divergence, portrait_py,weighted_portrait


baci_net_filename = 'net/baci_matching_igo.txt'
igo_net_filename = 'net/IGO_selected_politic_and_military.txt'

BACI_net= nx.read_weighted_edgelist(baci_net_filename,  nodetype=int)
IGO_net= nx.read_weighted_edgelist(igo_net_filename,  nodetype=int)

BACI_adjacency_matrix=nx.adjacency_matrix(BACI_net)
IGO_adjacency_matrix=nx.adjacency_matrix(IGO_net,nodelist=list(BACI_net.nodes))

#row normalize matrixes
BACI_adjacency_matrix_norm = 1000* BACI_adjacency_matrix / BACI_adjacency_matrix.sum()
IGO_adjacency_matrix_norm = 1000* IGO_adjacency_matrix / IGO_adjacency_matrix.sum()

BACI_net= nx.from_numpy_matrix(BACI_adjacency_matrix_norm )
IGO_net= nx.from_numpy_matrix(IGO_adjacency_matrix_norm )

net=BACI_net

portrait = portrait_py(net)
print(portrait)
fig, ax = plt.subplots(1,1)
img=ax.imshow(portrait, cmap='viridis', interpolation='nearest', aspect='auto',extent=[0,len(portrait[0]),0,len(portrait)])
#plt.imshow(portrait, cmap='viridis', interpolation='nearest', aspect='auto',extent=[0,len(portrait[0]),0,len(portrait)])
y_lab=[]
y_tics=[]
for i in range(0,len(portrait)):
    y_lab.append(i)
    y_tics.append(i+0.5)
ax.set_yticks(y_tics)
ax.set_yticklabels(y_lab)
fig.colorbar(img)
plt.show()

portrait = weighted_portrait(net)
print(portrait)
plt.imshow(portrait, cmap='viridis', interpolation='nearest', aspect='auto',extent=[0,len(portrait[0]),0,len(portrait)])
plt.colorbar()
plt.show()