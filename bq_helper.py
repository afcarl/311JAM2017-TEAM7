import pandas as pd

def get_query(query):
    df = pd.read_gbq(query, project_id='np-hacks',verbose=True, private_key='auth_key.json', dialect='standard')
    return df