import pandas as pd 	
require_cols = [1]
df = pd.read_excel('demo1.xlsx',usecols = require_cols) 	
print(df.shape) 	
print(df)