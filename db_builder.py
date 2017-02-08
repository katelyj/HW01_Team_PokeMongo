from pymongo import MongoClient
import csv


#setting up database

#server = MongoClient('127.0.0.1')
server = MongoClient('149.89.150.100')
db = server.PokeMongo
c = db.students
c.remove() # Clear Collection

# print c.count()

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
    course_list = []
    for co in courses:
        if co['id'] == p['id']:
            course_list += [ {'code' : co['code'], 
                              'mark' : int(co['mark']) } ]
    d['courses'] = course_list
    print d
    c.insert_one(d)
    f2.seek(0)

f1.close()
f2.close()

# print c.count()
