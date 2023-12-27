import pandas as pd


url = "https://raw.githubusercontent.com/abd-ul-ahad/csv-files/master/train.csv"


df = pd.read_csv(url)


df.to_csv("dataset.csv", index=False)


print(df.head())
