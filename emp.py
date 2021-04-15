import pandas as pd 	
df=pd.read_csv('emp.csv') 	
print(df.shape) 	
print(df) 	
print("----------------------------------------------")
df1 = df.fillna({'EMPID':105,'EMP_NAME':'NIDHI MAKWANA'}) 	
print(df1) 