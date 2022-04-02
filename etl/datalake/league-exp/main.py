from datetime import date, datetime, timedelta

import juno
import pandas as pd
from juno.constants import *

from etl.constants import RIOT_TOKEN


def _utc_to_br():
    return datetime.today() - timedelta(hours=3)


def _date_to_str(date):
    return date.strftime('%d-%m-%Y-%H:%M.parquet')


def run(request):
    juno.authenticate(RIOT_TOKEN)

    queue = QUEUE[0]
    tier = TIER[0]
    division = DIVISION[0]

    league = juno.LeagueExp()
    document = league.get_entries_by_queue_tier_division(queue, tier, division)

    df = pd.DataFrame(document)
    df = pd.DataFrame(document['content'])

    date = _utc_to_br()
    file_name = _date_to_str(date)

    df.to_parquet(df.to_parquet(f'gs://datalake-katsu/league-exp/{file_name}'))
