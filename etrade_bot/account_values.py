import pandas as pd

# Read the text file and specify the delimiter as " - "
df = pd.read_csv("Etrade_account_values.txt",
                 delimiter=" - ",
                 names=["Date", "Value"],
                 engine="python",
                 encoding='utf-16'
                 )

# Convert the "Date" column to a datetime data type
df["Date"] = pd.to_datetime(df["Date"])

# Remove the "$" and "," characters from the "Value" column and convert it to a numeric data type
df["Value"] = df["Value"].str.replace("$", "").str.replace(",", "").astype(float)

# Save the DataFrame to a CSV file
df.to_csv("Etrade_account_values.csv", index=False)
