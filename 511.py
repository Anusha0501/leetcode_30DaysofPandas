#511. Game Play Analysis I

import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login_date = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login_date.columns = ['player_id', 'first_login']
    return first_login_date
