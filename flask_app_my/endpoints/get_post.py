from flask import render_template
from sql_requests import get_post_by_id

def get_post(post_id):
    post = get_post_by_id(post_id)
    return render_template('post.html', post=post)