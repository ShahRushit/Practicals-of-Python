import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
    user='root',
    passwd='root',
    db='demo')
cursor = mydb.cursor()

csv_data = csv.reader('demo1.csv')
for row in csv_data:

    cursor.execute('INSERT INTO demo1(No, Name, Age )VALUES(%d, "%s", %d)',row)
#close the connection to the database.
cursor.close()
print ("Done")