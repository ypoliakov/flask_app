from flask import render_template
from sql_requests import get_all_posts

def index():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)