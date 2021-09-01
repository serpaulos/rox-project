from sqlalchemy import create_engine
import pandas as pd
#pip install pymysql




my_conn = create_engine("mysql+pymysql://root:cast8570@localhost/rox_project_db")

product_data = pd.read_csv('data/Production.Product.csv',sep=';',decimal=",")

product_data.to_sql(con=my_conn,name='table_product',if_exists='append',index=False)