import mysql.connector as msql
import config

conn = None

try:
    conn = msql.connect(host=config.host, user=config.user, password=config.password)
    print("Mysql connected")
except:
    print("Connection failed")

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
conn.autocommit = True

#Preparing query to create a database
sql_create_db = f"CREATE DATABASE {config.db_name} CHARACTER SET utf8;"

#Creating a database
cursor.execute(sql_create_db)
print(f"Database {config.db_name} created successfully........")

#Closing the conn
conn.close()