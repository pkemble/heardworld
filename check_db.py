import sqlite3

def check_db():
    try:
        conn = sqlite3.connect('/home/hermes/.hermes/workspace/md-podcast/database.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM posts")
        p = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM comments")
        c = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM enclosures")
        e = cursor.fetchone()[0]
        
        print(f"Posts: {p}, Comments: {0 if c is None else c}, Enclosures: {e}")
        
    except Exception as err:
        print(f"Error: {err}")
    finally:
        conn.close()

if __name__ == '__main__':
    check_db()
