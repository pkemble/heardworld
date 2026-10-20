import sqlite3
import json

def update_schema():
    try:
        conn = sqlite3.connect('/home/hermes/.hermes/workspace/md-podcast/database.db')
        cursor = conn.cursor()
        
        # Ensure enclosures table exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enclosures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id INTEGER NOT NULL,
                url TEXT NOT NULL,
                FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
            );
        """)
        
        # Ensure comments table is correctly structured (redundant but safe)
        # We rely on the schema file as the source of truth
        
        conn.commit()
        print("Schema update successful (enclosures checked).")
    except Exception as e:
        print(f"Error updating schema: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    update_schema()
