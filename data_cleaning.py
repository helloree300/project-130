import pandas as pd

finalData_df = pd.read_csv("data_merger.csv")
print(finalData_df)

finalData_df.columns

finalData_df.drop(columns=['Luminosity'], inplace=True)
finalData_df.dropna()
print(finalData_df)

finalData_df.describe()
finalData_df.info()
finalData_df.dtypes

finalData_df.to_csv('final_data.csv', index = True, index_label = "id")
print('final_data.csv Downloaded Successfully!')