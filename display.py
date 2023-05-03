import sqlite3
import pandas as pd

def display_samples():
    conn = sqlite3.connect('qc.db')

    df = pd.read_sql_query("SELECT * FROM active_samples", conn)
    print(df)

    conn.close()

def main():
    display_samples()

if __name__ == '__main__':
    main()

