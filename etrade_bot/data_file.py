import pandas as pd

df = pd.read_csv("transaction_history.csv", skiprows=2)

data_dict = df.to_dict()

transaction_sum = df["Quantity"].sum()
commission_sum = df["Commission"].sum()

transfers = df.groupby("TransactionType")["Amount"].sum()

total_transfers = transfers.loc["Transfer"]


print(transfers)
print(commission_sum)
print(total_transfers)
print(91.62-48.65)

