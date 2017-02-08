from pymongo import MongoClient
import csv

def average(data):
    classes = len(data)
    if classes == 0:
        return "N/A"
    total = 0
    for course in data:
        total += course['mark']
    return float(total) / classes


#setting up database

#server = MongoClient('127.0.0.1')
server = MongoClient('149.89.150.100')
db = server.PokeMongo
c = db.students

# printing averages

students = c.find()
for student in students:
    print "Name: %-*sID: %s\tAverage: %.2f"%(15, student['name'],
                                              student['id'],
                                              average(student['courses']))

# populating with teachers

f = open("teachers.csv", "r")
teachers = csv.DictReader(f)

t = db.teachers
t.remove() # Clear collection
for teacher in teachers:
    d = {}
    d['name'] = teacher['teacher']
    d['course'] = teacher['code']
    d['period'] = teacher['period']
    student_list = c.find( { 'courses.code' : d['course'] } )
    students = []
    for student in student_list:
        students += [ student['id'] ]
    d['students'] = students
    # print d
    t.insert_one(d)

# print t.count()

