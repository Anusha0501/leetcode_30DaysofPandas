#1148. Article Views I

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Find authors who viewed their own articles
    authors_who_viewed_own_articles = views[views['author_id'] == views['viewer_id']]["author_id"].drop_duplicates().sort_values()

    # Prepare the result DataFrame
    result = pd.DataFrame({"id": authors_who_viewed_own_articles})

    return result
