import sqlite3

connect = sqlite3.connect("files/demo.db")
cursor = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS data")
sql = """CREATE TABLE data(

            Date text,
            Open real,
            High real,
            Low real,
            Close real,
            Volume)"""

cursor.execute(sql)
connect.commit()
connect.close()

#