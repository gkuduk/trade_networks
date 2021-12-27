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
    
    net = []
    
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        
        found = False
        for idx, val in enumerate(net):
            if (val[0] == row['i'] and val[1] == row['j']) or (val[1] == row['i'] and val[0] == row['j']):
                net[idx][2] += float(row['v'])
                found = True
                break
        
        if not found:
            net.append([row['i'], row['j'], float(row['v'])])
        line_count +=1
    
    print(f'Processed {line_count} lines.')
    
    with open(output_filename, 'w') as txt_file:
        for el in net:
            txt_file.write(f'{el[0]} {el[1]} {el[2]}\n')

