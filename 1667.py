#1667. Fix Names in a Table

import pandas as pd
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    df = users.sort_values(by = 'user_id', ascending = True)
    df['name'] = df['name'].str.capitalize()
    return df

