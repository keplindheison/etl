#!/bin/bash
gsutil -m rsync -r ./etl/datalake/ gs://datalake-katsu/datalake/