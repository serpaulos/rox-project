from sqlalchemy import (create_engine, exc)
import config
import pandas as pd

try:
    engine = create_engine(f"mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db_name}", echo=False)
    print('Database connected.')
except exc.SQLAlchemyError as e:
    print("Database not connected", e)


sales_order_header_table_data = pd.read_csv('data/Sales.SalesOrderHeader.csv',sep=';',decimal=",")

sales_order_header_table_data.to_sql(con=engine,name='sales_order_header_table',if_exists='append',index=False)
