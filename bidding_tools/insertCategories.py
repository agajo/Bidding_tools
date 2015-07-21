import sqlite3
conn = sqlite3.connect('../biddingDB.db')
cur = conn.cursor()

import csv
import re
with open('../4_categories.csv','r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        categories = row#一つ取り出したいだけ

for category in categories:
    match = re.match('【([0-9]{3})】',category)
    number = match.group(1)

    cur.execute('INSERT INTO category (categoryID,categoryName) VALUES (?,?)',(number,category))

conn.commit()
conn.close()
    
