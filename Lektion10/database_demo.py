import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port='3306',
    user='root',
    password='root',
    database='newslist'
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM emails")
table = mycursor.fetchall()
for row in table:
    print(row)
sql = "SELECT * FROM emails WHERE email LIKE 'ilyas%'"
mycursor.execute(sql)
mycursor.close()
mydb.close()

'''
sql = "INSERT INTO emails (email) VALUES (%s)"
val = ["test@example.com"]
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted")
'''
