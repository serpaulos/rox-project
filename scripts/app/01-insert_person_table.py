from sqlalchemy import (create_engine, exc)
import config
import pandas as pd

try:
    engine = create_engine(f"mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.db_name}", echo=False)
    print('Database connected.')
except exc.SQLAlchemyError as e:
    print("Database not connected", e)


person_data = pd.read_csv('dados_manipulados/person_dados_manipulados.csv')

person_data.to_sql(con=engine,name='person_table',if_exists='append',index=False)
