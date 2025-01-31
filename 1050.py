#1050. Actors and Directors Who Cooperated At Least Three Times

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    return actor_director.groupby(by=["actor_id", "director_id"], as_index=False).size().query("size >= 3").drop(labels="size", axis=1)
    
