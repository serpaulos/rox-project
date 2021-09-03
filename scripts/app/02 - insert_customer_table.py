from sqlalchemy import (create_engine, exc)
import config
import pandas as pd

try:
    engine = create_engine(f"mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db_name}", echo=False)
    print('Database connected.')
except exc.SQLAlchemyError as e:
    print("Database not connected", e)


customer_data = pd.read_csv('dados_manipulados/customer_dados_manipulados.csv')

customer_data.to_sql(con=engine,name='customer_table',if_exists='append',index=False)
