from datetime import datetime

import pandas as pd
import csv, gzip, re, sys, time, tqdm

parquet_file = 'big.parquet'
start_time = time.time()

# Load the parquet file into a pandas DataFrame
df = pd.read_parquet(parquet_file)

# Filter the DataFrame to only include data from the year 2023
df = df[df['year'] == 2023]

