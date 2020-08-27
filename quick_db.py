from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgres://USER:PASSWORD@SERVER:5432/USER")
df = pd.read_csv('toking.csv')
df.to_sql("strains", con=engine) 
