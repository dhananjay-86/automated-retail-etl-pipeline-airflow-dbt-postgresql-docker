import pandas as pd

file_path = "data/raw/customers.csv" 

customers_df = pd.read_csv(file_path) 

print(customers_df.head()) 