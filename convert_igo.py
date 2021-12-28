import csv
from collections import defaultdict

input_filename = 'data/IGO/IGO_selected_politic_and_military.csv'
output_filename = 'net/IGO_selected_politic_and_military.txt'

with open(input_filename, encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';')
    line_count = 0

    net = []
    countries_codes= {}
    organizations_members = defaultdict(list)
    organizations_members_value= defaultdict(list)
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        else:
            countries_codes[row['ccode']]=row['state']
            organizations_members[row['Attribute']].append(row['ccode'])
            organizations_members_value[row['Attribute']].append(row['Value'])


    countries =[]
    for country_code in countries_codes:
        countries.append(country_code)


    countries_conn = {}
    for i in range(0, len(countries)):
        for j in range(i+1, len(countries)):
            countries_conn[(countries[i],countries[j])]=0


    for org in organizations_members:
        for i in range(0, len(organizations_members[org])):
            for j in range(i+1, len(organizations_members[org])):
                if int(organizations_members_value[org][i]) == 0 or int(organizations_members_value[org][j])==0:
                    continue
                if int(organizations_members_value[org][i]) == 3 or int(organizations_members_value[org][j])==3:
                    continue
                elif int(organizations_members_value[org][i]) == -9 and int(organizations_members_value[org][j]) ==-9:
                    continue
                if int(organizations_members_value[org][i]) == 1 and int(organizations_members_value[org][j]) == 1:
                    countries_conn[(organizations_members[org][i], organizations_members[org][j])] +=1
                else:
                    print(organizations_members_value[org][i])
                    print(organizations_members_value[org][j])
                    print("")

    with open(output_filename, 'w') as txt_file:
        for el in countries_conn:
            if countries_conn[el]!=0:
                txt_file.write(f'{el[0]} {el[1]} {countries_conn[el]}\n')
