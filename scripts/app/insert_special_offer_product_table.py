import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
import time
import config

table_special_offer_product = "table_special_offer_product"


try:
    conn = msql.connect(database=config.db_name, user=config.user, password=config.password, host=config.host)
    print('Database connected.')
    # Creating a cursor object using the cursor() method
except Error as e:
    print("Database not connected", e)


person_data = pd.read_csv('data/Person.Person.csv',sep=';')
person_data["Title"].fillna("NULL", inplace = True)
person_data["MiddleName"].fillna("NULL", inplace = True)
person_data["Suffix"].fillna("NULL", inplace = True)
person_data["AdditionalContactInfo"].fillna("NULL", inplace = True)


try:
    if conn.is_connected():
        cursor = conn.cursor()
        # the connection is not autocommitted by default, so we must commit to save our changes
        conn.autocommit = True
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        for i, row in person_data.iterrows():
            sql = f"INSERT INTO {table_special_offer_product} (business_entity_id, person_type, name_style, title, first_name, " \
                  f"middle_name, last_name, suffix, email_promotion, additional_contact_info, demographics, " \
                  f"rowguid, modified_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
except Error as e:
    print("Error while connecting to MySQL", e)

#Closing the conn
conn.close()
