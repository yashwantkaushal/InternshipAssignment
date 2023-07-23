import pandas as pd
from pandas_profiling import ProfileReport


df = pd.read_excel('Omnify-Analyst.xlsx')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Omnify.html")