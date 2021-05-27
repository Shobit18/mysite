import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", db="mydata")

myCursor = conn.cursor()



myCursor.execute("DELETE FROM bio WHERE id = 6;")
print(" > Data Deleted1! ")

conn.commit()
conn.close()