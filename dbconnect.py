import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text

ip = input("Enter: IP address\n")
db = input("Enter: DB name\n")
engine = create_engine(f'mssql+pymssql://admin:test123@{ip}:1433/{db}')

conn = engine.connect()

sql = "SELECT * FROM Users;"

stmt = text("INSERT INTO Users (UserName,Passphrase,UserType,Active) VALUES ('test4','test123','user','Yes')")
conn.execute(stmt)
conn.commit()


df = pd.read_sql_query(sql,conn)
print(df)
