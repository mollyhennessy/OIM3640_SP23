import sqlite3

connect = sqlite3.connect("files/demo.db")
cursor = connect.cursor()

data = ["2022-02-01", 450.68, 453.63, 446.94, 452.95, 123155400]
sql = """INSERT INTO data(Date, Open, High, Low, Close, Volume) 
         VALUES (?,?,?,?,?,?)"""

cursor.execute(sql, data)
connect.commit()
connect.close()
