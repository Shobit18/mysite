import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", db="mydata")

myCursor = conn.cursor()



myCursor.execute("UPDATE bio SET role = 'Pandit' WHERE id=5;")

myCursor.execute("UPDATE bio SET role = 'chemist' WHERE id=2;")
print(" > Data update successfully! ")

conn.commit()
conn.close()