from datetime import datetime

import pandas as pd
import csv, gzip, re, sys, time, tqdm

stat_year = '2023'
parquet_file = f"big.parquet/year={stat_year}"
start_time = time.time()

def load_data():
    # Load the parquet file into a pandas DataFrame
    df = pd.read_parquet(parquet_file)
    return df

columns = ['iframe', 'main_auth_thumbnail', 'title', 'tags', 'categories', 'performers', 'length', 'views', 'likes', 'dislikes', 'date', 'year']

if __name__ == '__main__':
    df = load_data()
    top_videos = df.nlargest(10, 'views')
    #print(top_videos)
    
    for index, row in top_videos.iterrows():
        print(row['iframe_src'].replace('/embed/', '/view_video.php?viewkey='))
