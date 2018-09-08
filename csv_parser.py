#Simple csv parser to get data into a list containing dicts

import csv

file = 'contact_list.csv'

def parse_csv_to_list(file_name):

    f = open(file_name, 'r')
    reader = csv.reader(f)

    #index of columns
    fields = reader.next()
    index_by_name = {
        'name': fields.index('Name'),
        'last_name': fields.index('Last Name'),
        'email': fields.index('Email'),
        'phone': fields.index('Phone')
    }

    all_rows = list()
    # reader.next()  #jump header row
    for row in reader:
        this_row = dict()
        this_row['name'] = row[index_by_name['name']]
        this_row['last_name'] = row[index_by_name['last_name']]
        this_row['email'] = row[index_by_name['email']]
        this_row['phone'] = row[index_by_name['phone']]

        all_rows.append(this_row)

    return all_rows

print 'list: {}'.format(parse_csv_to_list(file))
