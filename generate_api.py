
import json
import sqlite3
import os

def load_posts(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, post_id_ext, title, content, date, enclosure_url FROM posts")
        posts = [dict(row) for row in cursor.fetchall()]
        return posts
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

def generate_static_json(db_path, output_path):
    posts = load_posts(db_path)
    if not posts:
        print("No posts found in database.")
        return
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(posts)} posts to {output_path}")

if __name__ == "__main__":
    db_path = "/home/hermes/.hermes/workspace/md-podcast/database.db"
    output_path = "/home/hermes/.hermes/workspace/md-podcast/posts.json"
    generate_static_json(db_path, output_path)
