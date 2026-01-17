# API ETL Pipeline

## Overview
ETL pipeline that extracts user data from a public API,
transforms nested JSON fields, and loads the data into SQLite.

## Steps
- Extract data from REST API
- Transform nested JSON
- Load into database

## Tech Stack
- Python
- Requests
- Pandas
- SQLite

## Run
```bash
pip install -r requirements.txt
python etl/pipeline.py