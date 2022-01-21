import networkx as nx
import matplotlib.pyplot as plot
import netlsd

baci_net_filename = 'net/baci_matching_igo.txt'
igo_net_filename = 'net/IGO_selected_politic_and_military.txt'

BACI_net= nx.read_weighted_edgelist(baci_net_filename,  nodetype=int)
IGO_net= nx.read_weighted_edgelist(igo_net_filename,  nodetype=int)

## NetLSD

# compute signatures
baci_sig = netlsd.heat(BACI_net)
igo_sig = netlsd.heat(IGO_net)

# l2 (euclidan) distance of signatures
distance = netlsd.compare(baci_sig, igo_sig)

print(len(baci_sig))
print(distance)