import networkx as nx
import numpy as np
import matplotlib.pyplot as plot


net_filename = 'net/baci_total.txt'


# Load net
G = nx.read_weighted_edgelist(net_filename, nodetype=int)

print(f'Net { net_filename }:\nN = { G.order() }, M = { G.size() }')


## global characteristics

## similarity matrices

## portrait divergence



## clusterint coefficient

## NetLSD

## bridges and joints