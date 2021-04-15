# import pandas as pd
# dataframe1 = pd.read_excel('demo1.xlsx')
# print(dataframe1)
# import pandas as pd
# df = pd.read_csv('demo1.csv')
# print(df.head())
import pandas as pd
data = [ ('Rushit',21),
	    ('Nishu',25),
	    ('Shreya',22),
	    ('Himani',21),
	    ('Nidhi',21) ]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df)
