import os
from datetime import date 

import juno
import pandas as pd
from juno.constants import *

#from etl.constants import RIOT_TOKEN

RIOT_TOKEN = os.environ['RIOT_TOKEN']


def run():
    juno.authenticate(RIOT_TOKEN)

    queue = QUEUE[0]
    tier = TIER[0]
    division = DIVISION[0]

    for key in PLATFORM.keys():
        league = juno.LeagueExp(key)
        document = league.get_entries_by_queue_tier_division(queue, tier, division)

        df = pd.DataFrame(document)
        df = pd.DataFrame(document['content'])

        file_name = date.today()
        folder = key.lower()
        df.to_parquet(df.to_parquet(f'gs://datalake-katsu/league-exp/{folder}/{file_name}.parquet'))
    return 'Ok'

    
print(run())
