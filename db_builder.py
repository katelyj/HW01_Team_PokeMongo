from pymongo import MongoClient
import csv


#setting up database

server = MongoClient('149.89.150.100')
db = server.PokeMongo
c = db.students


#csv data

f1 = open("peeps.csv", "r")
peeps = csv.DictReader(f1)

f2 = open("courses.csv", "r")
courses = csv.DictReader(f2)


#putting data in the database

for p in peeps:
	d = {}
	d['name'] = p['name']
	d['age'] = int(p['age'])
	d['id'] = int(p['id'])
	for co in courses:
		if co['id'] == p['id']:
			d[co['code']] = int(co['mark'])
	f2.seek(0)
	c.insert_one(d)

f1.close()
f2.close()
