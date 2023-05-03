import sqlite3

def create_table():
    conn = sqlite3.connect('qc.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS active_samples
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                sample_name TEXT NOT NULL,
                wet_sample_weight REAL NOT NULL,
                plate_weight REAL NOT NULL)''')

    conn.commit()
    conn.close()

def insert_sample(sample_name, wet_sample_weight, plate_weight):
    conn = sqlite3.connect('qc.db')
    c = conn.cursor()

    c.execute("INSERT INTO active_samples (sample_name, wet_sample_weight, plate_weight) VALUES (?, ?, ?)", (sample_name, wet_sample_weight, plate_weight))

    conn.commit()
    conn.close()

def main():
    # create_table()

    while True:
        print("Enter sample details:")
        sample_name = input("Sample name: ")
        wet_sample_weight = float(input("Wet sample weight: "))
        plate_weight = float(input("Plate weight: "))

        insert_sample(sample_name, wet_sample_weight, plate_weight)

        print("Sample details have been saved.")

        continue_input = input("Add another sample? (Y/N): ")
        if continue_input.lower() != 'y':
            break

if __name__ == '__main__':
    main()
