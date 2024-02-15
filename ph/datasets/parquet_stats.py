from datetime import datetime

import pandas as pd
import csv, gzip, re, sys, time, tqdm

parquet_file = 'big.parquet'
start_time = time.time()

