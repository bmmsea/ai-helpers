from datetime import datetime

import pandas as pd
import csv, gzip, re, sys, time, tqdm

stat_year = '2023'
parquet_file = f"big.parquet/year={stat_year}/*"
start_time = time.time()

# Load the parquet file into a pandas DataFrame
df = pd.read_parquet(parquet_file)

# Filter the DataFrame to only include data from the year 2023
#df = df[df['year'] == 2023]

columns = ['iframe', 'main_auth_thumbnail', 'title', 'tags', 'categories', 'performers', 'length', 'views', 'likes', 'dislikes', 'date', 'year']
