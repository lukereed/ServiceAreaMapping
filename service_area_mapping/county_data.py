import pandas as pd


def get_county_data(state_name: str = "Colorado"):
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv")
    df.loc[:, "ServiceArea"] = False
    return df[df["STNAME"] == state_name]
