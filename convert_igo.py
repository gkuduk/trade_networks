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

    baci_net_filename='net/baci_matching_igo.txt'
    baci_cc_filename = 'data/BACI/country_codes_V202102.csv'
    igo_cc_filename = 'data/IGO/country_codes.csv'
    selected_baci=[]
    igo_cc= {}
    baci_cc={}
    with open(baci_net_filename) as txt_file:
        lines = txt_file.read().splitlines()

        for line in lines:
            row = line.split(' ')

            if row[0] not in selected_baci:
                selected_baci.append(row[0])
            if row[1] not in selected_baci:
                selected_baci.append(row[1])

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

    with open(output_filename, 'w') as txt_file:
        count= {}
        for el in countries_conn:

            if countries_conn[el]!=0:
                if igo_cc[el[0]] not in baci_cc.values():
                    # print(igo_cc[str(el[0])])
                    count[el[0]] = igo_cc[el[0]]
                if igo_cc[el[0]] in baci_cc.values():
                    # print(igo_cc[str(el[0])])
                    txt_file.write(f'{el[0]} {el[1]} {countries_conn[el]}\n')
        print(len(count))
        print(count)
