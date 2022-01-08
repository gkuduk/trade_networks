import sys
import csv

input_filename = 'data/BACI/BACI_HS12_Y2014_V202102.csv'
output_filename = 'net/baci_matching_igo.txt'

baci_cc_filename = 'data/BACI/country_codes_V202102.csv'
igo_cc_filename = 'data/IGO/country_codes.csv'

igo_net_filename = 'net/IGO_selected_politic_and_military.txt'

if (len(sys.argv) == 2):
    input_filename = sys.argv[1]
if (len(sys.argv) == 3):
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]


net = {}
baci_cc = {}
igo_cc = {}
selected_igo = []

with open(input_filename) as csv_file:
    
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        
        found = False
        
        if row['i'] in net and row['j'] in net[row['i']]:
            net[row['i']][row['j']] += float(row['v'])
            found = True
        
        if not found and row['j'] in net and row['i'] in net[row['j']]:
            net[row['j']][row['i']] += float(row['v'])
            found = True
        
        if not found:
            if row['i'] not in net:
                net[row['i']] = {}
            net[row['i']][row['j']] = float(row['v'])
        
        line_count += 1
    
    print(f'Processed {line_count} lines.')


with open(baci_cc_filename) as cc_file:
    
    csv_reader = csv.DictReader(cc_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        
        baci_cc[row['country_code']] = row['country_name_full']
        line_count += 1

with open(igo_cc_filename) as cc_file:
    csv_reader = csv.reader(cc_file, delimiter=';')
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        
        igo_cc[row[2]] = row[0]
        line_count += 1

with open(igo_net_filename) as txt_file:
    lines = txt_file.read().splitlines()
    
    for line in lines:
        row = line.split(' ')

        if row[0] not in selected_igo:
            selected_igo.append(row[0])
        if row[1] not in selected_igo:
            selected_igo.append(row[1])


for idx, el in enumerate(selected_igo):
    if el in igo_cc:
        selected_igo[idx] = igo_cc[el]
    

with open(output_filename, 'w') as txt_file:
    for el in net:
        if baci_cc[el] not in selected_igo:
            continue
        for el2 in net[el]:
            if baci_cc[el2] in selected_igo:
                txt_file.write(f'{ el } { el2 } { net[el][el2] }\n')
