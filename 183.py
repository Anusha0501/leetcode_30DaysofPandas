#183. Customers Who Never Order

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Find customers who never placed an order
    ordered_customers = orders['customerId'].unique()
    never_ordered = customers[~customers['id'].isin(ordered_customers)]

    # Prepare the result DataFrame
    result = never_ordered[['name']].rename(columns={"name": "Customers"})

    return result
