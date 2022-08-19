import pandas as pd

#Read CSV
file_path = ("../Resources/cities.csv")

cities_df = pd.read_csv(file_path)

table = cities_df.to_html(index=False)
print(table)
