import sqlite3

def check_tables():
    try:
        conn = sqlite3.connect('/home/hermes/.hermes/workspace/md-podcast/database.db')
        cursor = conn.cursor()
        
        # Get list of all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Tables: {[t[0] for t in tables]}")
        
        # Count records for each table found
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"{table_name} count: {count}")
            
    except Exception as err:
        print(F"Error: {err}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    check_tables()
