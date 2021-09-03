from sqlalchemy import (create_engine, exc)
import config
import pandas as pd

try:
    engine = create_engine(f"mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db_name}", echo=False)
    print('Database connected.')
except exc.SQLAlchemyError as e:
    print("Database not connected", e)


sales_order_detail_table_data = pd.read_csv('dados_manipulados/SalesOrderDetail_dados_manipulados.csv', decimal=",")

sales_order_detail_table_data.to_sql(con=engine,name='sales_order_detail_table',if_exists='append',index=False)
