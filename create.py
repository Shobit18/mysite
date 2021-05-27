import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", db="mydata")

myCursor = conn.cursor()

myCursor.execute("""CREATE TABLE Bio
(
id int primary key,
name varchar(20),
role varchar(20)

)
""")

conn.commit()
conn.close()