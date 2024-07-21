from flask import Blueprint
from endpoints.index import index
from endpoints.get_post import get_post
from endpoints.new_post import new_post
from endpoints.del_post import delete_post_by_id
from endpoints.edit_post import edit_post

def init_routes(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/<int:post_id>', 'get_post', get_post)
    app.add_url_rule('/new', 'new_post', new_post, methods=['GET', 'POST'])
    app.add_url_rule('/delete/<int:post_id>', 'delete_post', delete_post_by_id, methods=['POST'])
    app.add_url_rule('/edit/<int:post_id>', 'edit_post', edit_post, methods=['GET', 'POST'])
