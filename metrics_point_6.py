import networkx as nx
import numpy as np
import matplotlib.pyplot as plot
import csv

baci_net_filename = 'net/baci_matching_igo.txt'
igo_net_filename = 'net/IGO_selected_politic_and_military.txt'

BACI_net= nx.read_weighted_edgelist(baci_net_filename,  nodetype=int)
IGO_net= nx.read_weighted_edgelist(igo_net_filename,  nodetype=int)

baci_cc_filename = 'data/BACI/country_codes_V202102.csv'

baci_cc={}
with open(baci_cc_filename) as cc_file:
        csv_reader = csv.DictReader(cc_file)
        line_count = 0

        for row in csv_reader:
                if line_count == 0:
                        line_count += 1

                baci_cc[int(row['country_code'])] = row['country_name_full']

### bridges, hubs, joints

## bridges
baci_bridges = nx.bridges(BACI_net)
igo_bridges = nx.bridges(IGO_net)

print('\nBridges:')
print(f"BACI: {list(baci_bridges)}")
print(f"IGO: {list(igo_bridges)}")

## hubs
# hub_score, authority_score = nx.hits()
baci_h, baci_a = nx.hits(BACI_net)
igo_h, igo_a = nx.hits(IGO_net)

# sort
baci_h = {k: v for k, v in sorted(baci_h.items(), key=lambda el: el[1], reverse=True)}
igo_h = {k: v for k, v in sorted(igo_h.items(), key=lambda el: el[1], reverse=True)}

# top
baci_h_top = {k: v for k, v in list(baci_h.items())[:10]}
baci_h_bot = {k: v for k, v in list(baci_h.items())[-10:]}
igo_h_top = {k: v for k, v in list(igo_h.items())[:10]}
igo_h_bot = {k: v for k, v in list(igo_h.items())[-10:]}

print(f'\nHub score:')
print(f'\nBACI')
print(f'Top countries:')
for cc, v in baci_h_top.items():
    print(f'{baci_cc[cc]} ; {v}')
print(f'\nBottom countries:')
for cc, v in baci_h_bot.items():
    print(f'{baci_cc[cc]} ; {v}')

print(f'\nIGO')
print(f'Top countries:')
for cc, v in igo_h_top.items():
    print(f'{baci_cc[cc]} ; {v}')
print(f'\nBottom countries:')
for cc, v in igo_h_bot.items():
    print(f'{baci_cc[cc]} ; {v}')

## joints (articulation points)
baci_ap = nx.articulation_points(BACI_net)
igo_ap = nx.articulation_points(IGO_net)

baci_bc = nx.is_biconnected(BACI_net)
igo_bc = nx.is_biconnected(IGO_net)

print('\nJoints:')
print(f"BACI biconnected: {baci_bc}, joints: {list(baci_ap)}")
print(f"IGO biconnected: {igo_bc}, joints: {list(igo_ap)}")