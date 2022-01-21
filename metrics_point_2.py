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

## clustering coefficients

baci_cls_coef = nx.clustering(BACI_net)
igo_cls_coef = nx.clustering(IGO_net)

# sort
baci_cls_coef = {k: v for k, v in sorted(baci_cls_coef.items(), key=lambda el: el[1], reverse=True)}
igo_cls_coef = {k: v for k, v in sorted(igo_cls_coef.items(), key=lambda el: el[1], reverse=True)}

# top n, bottom n
baci_cls_coef_top = {k: v for k, v in list(baci_cls_coef.items())[:10]}
baci_cls_coef_bot = {k: v for k, v in list(baci_cls_coef.items())[-10:]}
igo_cls_coef_top = {k: v for k, v in list(igo_cls_coef.items())[:10]}
igo_cls_coef_bot = {k: v for k, v in list(igo_cls_coef.items())[-10:]}

baci_avg_cls = nx.average_clustering(BACI_net)
igo_avg_cls = nx.average_clustering(IGO_net)

print(f'\nClustering coefficient:')
print(f'\nBACI')
print(f'Top countries:')
for cc, v in baci_cls_coef_top.items():
    print(f'{baci_cc[cc]} ; {v}')
print(f'\nBottom countries:')
for cc, v in baci_cls_coef_bot.items():
    print(f'{baci_cc[cc]} ; {v}')
print(f'\naverage = {baci_avg_cls}')

print(f'\nIGO')
print(f'Top countries:')
for cc, v in igo_cls_coef_top.items():
    print(f'{baci_cc[cc]} ; {v}')
print(f'\nBottom countries:')
for cc, v in igo_cls_coef_bot.items():
    print(f'{baci_cc[cc]} ; {v}')
print(f'\naverage = {igo_avg_cls}')
