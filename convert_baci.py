import sys
import csv

input_filename = 'data/BACI/BACI_HS12_Y2014_V202102.csv'
output_filename = 'net/baci.txt'

if (len(sys.argv) == 2):
    input_filename = sys.argv[1]
if (len(sys.argv) == 3):
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]



with open(input_filename) as csv_file:
    
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    net = {}
    
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
        
        line_count +=1
    
    print(f'Processed {line_count} lines.')
    
    with open(output_filename, 'w') as txt_file:
        for el in net:
            for el2 in net[el]:
                txt_file.write(f'{ el } { el2 } { net[el][el2] }\n')

