
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id_ext INTEGER UNIQUE,
    title TEXT NOT NULL,
    content TEXT,
    date DATETIME,
    enclosure_url TEXT
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    author TEXT,
    content TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

CREATE TABLE enclosures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);
