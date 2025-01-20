#595. Big Countries

import pandas as pd

# Assuming 'tables' contains the input data, and we extract the 'World' table
data = {
    "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
    "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
    "area": [652230, 28748, 2381741, 468, 1246700],
    "population": [25500100, 2831741, 37100000, 78115, 20609294],
    "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000],
}

# Creating a DataFrame
world = pd.DataFrame(data)

# Define the function for filtering big countries
def big_countries(world):
    # Filtering the "big" countries
    big_countries_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]

    # Selecting the required columns
    result_table = big_countries_df[['name', 'population', 'area']]
    return result_table

# Use the function and pass the 'World' table
result = big_countries(world)

# Display the result
print(result)

