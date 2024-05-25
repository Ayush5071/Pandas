import pandas as pd 
import re
df = pd.read_csv('pokemon_data.csv')
# print(df.head(5))
df_txt = pd.read_csv('pokemon_data.txt',delimiter='\t')
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(df_txt.head(5))
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(df.columns) #printing headers
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(df['Name'][0:5])
# print(df.Name)
# print(df[['Name','HP','Attack']][0:3])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(df.iloc[0:3]) # integer location ,,,, useful for printing rows
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(df.iloc[2,1])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# for i,j in df.iterrows(): # index,rows
#     print(j[['Name','HP']])
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# conditionalLocation = df.loc[df['Type 1']=="Fire"]
# print(conditionalLocation)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(df.describe()) #for describing statistical parameters columns wise
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# print(df.sort_values(['Type 1','HP'],ascending=[1,0]))
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# df['Total'] = df['HP'] + df['Speed']
### can be done using iloc
# df['Total1'] = df.iloc[:,4:10].sum(axis=1) ## 1 is horzontal axis

# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# # df = df.drop(columns=['Total'])
# print(df)
# df.to_csv('pokenew.csv',index=False) #to save the new csv file
# df.to_excel('pokenew.xlsx',index=False) #to save the new excel file
# df.to_csv('pokenew.txt',index=False,sep='\t')
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#filtering Data
# filtered_data = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 75)]
# filtered_data = filtered_data.reset_index(drop=True)  #drop -> gives old index as index columns along with new index in correct order
# print(filtered_data)
# filtered_data.to_csv('filtered_data.csv')
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# df = df.loc[(df['Name'].str.contains('Mega'))]
# print(df.reset_index(drop=True))
# ###Using Regex 
# df = df.loc[df['Type 1'].str.contains('fire|grass',flags=re.I,regex=True)] ## flags=re.I ,that means ignore case !!! very usful indeed 
# print(df)
## SUPER OP HOW TO FILTER ON PHRASE/PIECE OF WORDS!!!!!
# Phrase_specific = df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I,regex=True)] ### pi[a-z]* --> pi should be there in word,qand other words rage is a-z ,*->can be 0 or more,^->that pi should be in start
# print(Phrase_specific.reset_index())
# print(">>>>>>>>>>>>>>>>>>>>>>>> CONDITIONAL CHANGES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# df.loc[df['Type 1'] == 'Fire','Type 1'] = 'Flamer' ## df.loc[*condition,parameter] = value .... column get replaced by value after fulfilling the condition 
# df.loc[df['Attack']>100 ,['Generation','Legendary']] = ['Test 1','Test 2']
# print(df)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>> AGGREGATE STATISTICS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# grouped = df.groupby(['Type 1']).sum()
# grouped2 = df.groupby(['Type 1']).count() #### at alst add ['count'] to get specifically count of each type of bugs
# print(grouped2.drop(columns=['Name','Type 2']))
# # for name,group in grouped :
# #     print(name,group)
# df['count'] = 1
# Nested_Group = df.groupby(['Type 1','Type 2']).count()
# print(Nested_Group['count'])

print(">>>>>>>>>>>>>>>>>>>>>>> CHUNKING SIZE OF CSV FOR LARGE DATASET >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('pokemon_data.csv',chunksize=5):
    results = df.groupby(['Type 1']).count()
    new_df = pd.concat([new_df,results])
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(new_df.drop(columns = ['Type 1']))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

