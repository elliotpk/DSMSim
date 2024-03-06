import pandas as pd

def activeCities():
    smaller_df = pd.read_csv("Database/Network_Database/varuhus.csv")


    larger_df = pd.read_csv("Database/Network_Database/worldcities.csv")

    common_countries = smaller_df['Country'].unique()

    filtered_df = larger_df[larger_df['Country'].isin(common_countries)]

    filtered_df.to_csv("Database/Network_Database/activecities.csv", index=False)