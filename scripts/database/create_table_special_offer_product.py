import mysql.connector as msql
import config

table_product = "table_product"

conn = None

try:
    conn = msql.connect(database=config.db_name, user=config.user, password=config.password, host=config.host)
    print('Database connected.')
except:
    print('Database not connected.')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
conn.autocommit = True

# Preparing query to create table
sql_create_table = (f"""
    CREATE TABLE IF NOT EXISTS {table_product}(
    id  int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name	varchar(40) NOT NULL,
	product_number       varchar(200) NOT NULL,	
    make_flag		DECIMAL NOT NULL,
	finished_goods_flag      char(10) NOT NULL,
	color		char(10) NOT NULL,
    SafetyStockLevel ,
    ReorderPoint                ,
    StandardCost               ,
    ListPrice                  ,
    Size                       ,
    SizeUnitMeasureCode        ,
    WeightUnitMeasureCode             ,
    Weight                           ,
    DaysToManufacture                  ,
    ProductLine                       ,
    Class                             ,
    Style                                                  ,
    ProductSubcategoryID                                  ,
    ProductModelID                                        ,
    SellStartDate                                          ,
    SellEndDate                                            ,
    DiscontinuedDate                                      ,
    rowguid                                                ,
    ModifiedDate                                           ,
    )
""")

# Creating table
cursor.execute(sql_create_table)
print(f"Table {table_product} created successfully........")

# Closing the conn
conn.close()
