import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", db="mydata")

myCursor = conn.cursor()



myCursor.execute("INSERT INTO bio(id, name, role) VALUES(1, 'Shobit','Student');")
print(" > Data Inserted!! ")

# myCursor.execute("INSERT INTO bio(id, name, role) VALUES(4, 'Dev','Visitor');")


# myCursor.execute("INSERT INTO bio(id, name, role) VALUES(6, 'Sonu','Boxer');")
# print(" > Data Inserted!! ")



conn.commit()
conn.close()