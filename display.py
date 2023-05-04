import sqlite3
import pandas as pd

def display_samples(conn):
    df = pd.read_sql_query("SELECT * FROM active_samples", conn)
    print(df)

def delete_sample(conn, sample_id):
    c = conn.cursor()
    c.execute("DELETE FROM active_samples WHERE id=?", (sample_id,))
    conn.commit()
    print(f"Sample with ID {sample_id} has been deleted.")

def main():
    conn = sqlite3.connect('qc.db')
    
    display_samples(conn)

    while True:
        delete_input = input("Do you want to delete a sample? (Y/N): ")
        if delete_input.lower() != 'y':
            break

        sample_name = input("Enter the sample name you want to delete: ")
        df = pd.read_sql_query("SELECT * FROM active_samples WHERE sample_name=?", conn, params=(sample_name,))
        print("Possible samples:")
        print(df)

        sample_id = int(input("Enter the ID of the sample you want to delete: "))
        delete_sample(conn, sample_id)

    conn.close()

if __name__ == '__main__':
    main()