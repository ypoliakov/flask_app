from flask import redirect, url_for
from sql_requests import delete_post

def delete_post_by_id(post_id):
    delete_post(post_id)
    return redirect(url_for('index'))
