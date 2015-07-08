import sqlite3
import getFilesAsOne
import codecs

ThursdayDate = 150629
folderpath = "../downloads/"+str(ThursdayDate)+"/" #ここにあるデータを読みに行きます。

dictlist = getFilesAsOne.getFilesAsOne(folderpath);

finallist = []

for dic in dictlist:
    if (("キャンペーン名" in dic) != True):
        finallist.append((dic["account"],dic["kind"],dic["category"],ThursdayDate,dic["impr"],dic["clicks"],dic["conv"],dic["cost"],dic["imprShare"],dic["avgPos"]))



conn = sqlite3.connect("../biddingDB.db")
c = conn.cursor()
c.executemany("INSERT INTO data (account,kind,category,ThursdayDate,impr,clicks,conv,cost,imprShare,avgPos) VALUES (?,?,?,?,?,?,?,?,?,?)",finallist)
conn.commit()
conn.close()

