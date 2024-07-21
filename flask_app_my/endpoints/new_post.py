from flask import render_template, request,redirect, url_for
from sql_requests import insert_post

def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        insert_post(title, content)
        return redirect(url_for('index'))
    return render_template('add_post.html')