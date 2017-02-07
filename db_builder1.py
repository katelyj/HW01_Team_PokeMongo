from pymongo import MongoClient
import csv


#setting up database

server = MongoClient('149.89.150.100')
db = server.PokeMongo
c = db.students
c.remove()
