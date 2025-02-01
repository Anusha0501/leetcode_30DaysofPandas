#178. Rank Scores

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    #Sorting the table in descending Order
    scores=scores.sort_values(by=['score'],ascending=False)

    #Using 'rank' to rank the rows in descending method
    #'dense' method gives ranks continuous without any gap. 
    scores['rank']=(scores['score'].rank(method='dense',ascending=False))

    return scores[['score','rank']]

