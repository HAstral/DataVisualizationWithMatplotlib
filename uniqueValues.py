import matplotlib.pyplot as plt
# Import pandas as pd
import pandas as pd
summer_2016_medals=pd.read_csv("summer2016.csv", index_col=0)
# Extract the "Sport" column
sports_column = summer_2016_medals['Sport']

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)