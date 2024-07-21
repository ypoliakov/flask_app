from flask import g

def get_all_posts():
    """Получает все посты из базы данных."""
    db = g.db
    return db.execute('SELECT * FROM posts').fetchall()

def get_post_by_id(post_id):
    """Получает пост по ID."""
    db = g.db
    return db.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()

def insert_post(title, content):
    """Вставляет новый пост в базу данных."""
    db = g.db
    db.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    db.commit()

def delete_post(post_id):
    """Удаляет пост из базы данных."""
    db = g.db
    db.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    db.commit()

def update_post(title, content, post_id):
    """Обновляет пост в базе данных."""
    db = g.db
    db.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
    db.commit()
