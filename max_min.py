import pandas as pd 	
df=pd.read_csv('emp.csv') 	
print(df.shape) 	
print(df) 	
print("Min : ",df['SALARY'].min()) 	
print("Max : ",df['SALARY'].max())
