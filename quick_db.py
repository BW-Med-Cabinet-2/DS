from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgres://wuzxngxn:g4YPfv7O48ZkAMbbX7_D1FYlFj6sZJux@lallah.db.elephantsql.com:5432/wuzxngxn")
df = pd.read_csv('toking.csv')
df.to_sql("strains", con=engine) 