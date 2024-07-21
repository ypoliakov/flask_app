from flask import render_template, request, redirect, url_for
from sql_requests import get_post_by_id, update_post

def edit_post(post_id):
    post = get_post_by_id(post_id)
    if post is None:
        return "Post not found", 404
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        update_post(title, content, post_id)
        return redirect(url_for('index'))
    return render_template('edit_post.html', post=post)
