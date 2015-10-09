"""create PTs for individual districts by copying master pviot.html and
   pulling down filtered SQL"""

import os
import psycopg2
import csv
import shutil

DISTRICTS = [
"Bhaktapur",
"Dhading",
"Dolakha",
"Gorkha",
"Kathmandu",
"Kabhrepalanchok",
"Lalitpur",
"Makawanpur",
"Nuwakot",
"Okhaldhunga",
"Ramechhap",
"Rasuwa",
"Sindhuli",
"Sindhupalchok"
]

BASE_DIR = "/home/ec2-user/thetablesarepivoting/"
MP = pivot.html
MD = db.csv

#delete old folders
for v in DISTRICTS:
    shutil.rmtree(BASE_DIR + v + '/')

#create dirs
for v in DISTRICTS:
    if not os.path.isdir(BASE_DIR+v)
	os.makedirs(BASE_DIR+v)

#copy master pivot to folders
for v in DISTRICTS:
    shutil.copyfile(BASE_DIR + 'all/' + MP, BASE_DIR + DISTRICT + '/' + MP)
    shutil.copyfile(BASE_DIR + 'all/' + MP, BASE_DIR + DISTRICT + '/' + MD)
