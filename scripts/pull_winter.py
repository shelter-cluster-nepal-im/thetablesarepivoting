"""create PTs for individual districts by copying master pviot.html and
   pulling down filtered SQL"""

import os
import psycopg2
import csv
import shutil

#AWS: BASE_DIR = "/home/ec2-user/thetablesarepivoting/"
BASE_DIR = '/home/ec2-user/thetablesarepivoting/winter/table/'

#pull from SQL to create db file
conn =  psycopg2.connect(os.environ['dbk'])
cur = conn.cursor()
cur.execute("select dist_code,hlcit_code,district,vdc,priority,above_1500,num_hh_damage,pct_damage,target_hh from winterisation where in_db is true")
row_names = ["District Code", "HLCIT Code", "District", "VDC", "Priority", "Above 1500M", "# of Damaged HH", "Total Damage %",
                        "Target HH"]
with open(BASE_DIR + 'winter_data.csv', 'wb') as f: 
    writer = csv.writer(f)
    writer.writerow(row_names)
    for i,r in enumerate(cur.fetchall()):
	writer.writerow(r)            
f.close()
