"""create PTs for individual districts by copying master pviot.html and
   pulling down filtered SQL"""

import os
import psycopg2
import csv
import shutil

DISTRICTS = [
"bhaktapur",
"dhading",
"dolakha",
"gorkha",
"kathmandu",
"kabhrepalanchok",
"lalitpur",
"makawanpur",
"nuwakot",
"okhaldhunga",
"ramechhap",
"rasuwa",
"sindhuli",
"sindhupalchok"
]

#AWS: BASE_DIR = "/home/ec2-user/thetablesarepivoting/"
BASE_DIR = '/Users/ewanog/code/git_repos/thetablesarepivoting/districts/'
MP = 'dist_pivot.html'

#pull from SQL to create db file
conn =  psycopg2.connect(os.environ['dbk'])
cur = conn.cursor()
cur.execute("select * from distributions")
row_names = [desc[0] for desc in cur.description]

with open(BASE_DIR + 'all/db.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(row_names)
    for r in cur.fetchall():
        writer.writerow(r)            
f.close()

#remove old, create dirs
for v in DISTRICTS:
    if os.path.isdir(BASE_DIR+v):
        shutil.rmtree(BASE_DIR + v + '/')
    
    os.makedirs(BASE_DIR+v)


#copy master pivot to folders
for v in DISTRICTS:
    shutil.copyfile(BASE_DIR + 'all/' + MP, BASE_DIR + v + '/' + MP)