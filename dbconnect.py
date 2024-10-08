import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine('mssql+pymssql://admin:test123@192.168.11.253:1433/MitchellDB')

conn = engine.connect()

sql = "SELECT * FROM Users;"

stmt = text("INSERT INTO Users (UserName,Passphrase,UserType,Active) VALUES ('test','test123','user','Yes')")
conn.execute(stmt)
conn.commit()


df = pd.read_sql_query(sql,conn)
print(df.head())
