import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
import time
import config

table_customer = "table_customer"


try:
    conn = msql.connect(database=config.db_name, user=config.user, password=config.password, host=config.host)
    print('Database connected.')
    # Creating a cursor object using the cursor() method
except Error as e:
    print("Database not connected", e)


customer_data = pd.read_csv('data/Sales.Customer.csv',sep=';')
customer_data["PersonID"].fillna(0, inplace = True)
customer_data["StoreID"].fillna(0, inplace = True)



try:
    if conn.is_connected():
        cursor = conn.cursor()
        # the connection is not autocommitted by default, so we must commit to save our changes
        conn.autocommit = True
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        for i, row in customer_data.iterrows():
            sql = f"INSERT INTO {table_customer} (customer_id, person_id, store_id, territory_id, account_number, " \
                  f"row_guid, modified_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
except Error as e:
    print("Error while connecting to MySQL", e)

#Closing the conn
conn.close()
