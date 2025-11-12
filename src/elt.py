import pandas as pd
from sqlalchemy import create_engine

# Reads the data from the web as a CSV 
file_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

df = pd.read_csv(file_url) 

# Create a connection to PostgreSQL  
connection_string = "postgresql://postgres:postgres@localhost:5432/wine"

engine = create_engine(connection_string)

# Connection   
connection = engine.connect() 

# Write the data to the database 
df.to_sql(name="wine_data_from_python", con=connection, if_exists="replace")   
  
