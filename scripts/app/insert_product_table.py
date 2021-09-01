import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
import time
import config

table_product = "table_product"


try:
    conn = msql.connect(database=config.db_name, user=config.user, password=config.password, host=config.host)
    print('Database connected.')
    # Creating a cursor object using the cursor() method
except Error as e:
    print("Database not connected", e)


product_data = pd.read_csv('data/Production.Product.csv',sep=';',decimal=",")
product_data["Color"].fillna("NULL", inplace = True)
product_data["Size"].fillna("NULL", inplace = True)
product_data["SizeUnitMeasureCode"].fillna("NULL", inplace = True)
product_data["WeightUnitMeasureCode"].fillna("NULL", inplace = True)
product_data['Weight'] = product_data['Weight'].astype(float)
product_data["Weight"].fillna("NULL", inplace = True)
product_data["ProductLine"].fillna("NULL", inplace = True)
product_data["Class"].fillna("NULL", inplace = True)
product_data["Style"].fillna("NULL", inplace = True)
product_data["ProductSubcategoryID"].fillna("NULL", inplace = True)
product_data["ProductModelID"].fillna("NULL", inplace = True)
product_data["SellEndDate"].fillna("NULL", inplace = True)
product_data["DiscontinuedDate"].fillna("NULL", inplace = True)


try:
    if conn.is_connected():
        cursor = conn.cursor()
        # the connection is not autocommitted by default, so we must commit to save our changes
        conn.autocommit = True
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        for row in product_data:
            sql = f"INSERT INTO {table_product} (ProductID, Name, ProductNumber, MakeFlag, FinishedGoodsFlag, Color," \
                  f" SafetyStockLevel, ReorderPoint, StandardCost, ListPrice, Size, SizeUnitMeasureCode, " \
                  f"WeightUnitMeasureCode, Weight, DaysToManufacture, ProductLine, Class, Style, ProductSubcategoryID, " \
                  f"ProductModelID, SellStartDate, SellEndDate, DiscontinuedDate, rowguid, ModifiedDate) " \
                  f"VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
except Error as e:
    print("Error while connecting to MySQL", e)

#Closing the conn
conn.close()
