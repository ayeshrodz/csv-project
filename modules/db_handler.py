import sqlite3
import pandas as pd # type: ignore
import time

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def insert_csv_to_db(csv_file, db_file, config):
    start_time = time.time()
    print("Starting database insertion...")

    conn = create_connection(db_file)
    cursor = conn.cursor()

    # Load CSV into DataFrame
    df = pd.read_csv(csv_file)

    # Insert DataFrame into SQLite table
    df.to_sql('data', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

    end_time = time.time()
    print(f"Database insertion completed in {end_time - start_time:.2f} seconds.")