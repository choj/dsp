import pandas as pd
fac_data = pd.read_csv("faculty.csv", sep=',\s|,')

fac_data.email.to_csv("emails.csv", index=False)