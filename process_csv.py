import csv,json

data = {
	'max': 1,
	'data': []
}

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
    	[lat, lon] = row[-2:]

    	data['data'].append({'lat': lat, 'lng': lon, 'count': 1})


with open('data.json', 'w') as o:
	json.dump(data, o)