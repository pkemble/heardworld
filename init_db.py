
import sqlite3
import os

def init_db():
    db_path = '/home/hermes/.hermes/workspace/md-podcast/database.db'
    schema_path = '/home/hermes/.hermes/workspace/md-podcast/schema.sql'
    
    if not os.path.exists(db_path):
        print(f'Creating database at {db_path}')
    
    conn = sqlite3.connect(db_path)
    try:
        with open(schema_path, 'r') as f:
            schema = f.read()
        conn.executescript(schema)
        print('Schema applied successfully.')
    except sqlite3.OperationalError as e:
        if 'already exists' in str(e):
            print('Tables already exist, skipping creation.')
        else:
            print(f'Error: {e}')
            return 1
    except Exception as e:
        print(f'Error: {e}')
        return 1
    finally:
        conn.close()
    return 0

if __name__ == '__main__':
    exit(init_db())
