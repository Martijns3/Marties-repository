from flask import Flask


# from markupsafe import escape
# app = Flask(__name__)
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/')
# def show_subpath():
#     # show the subpath after /path/
#     return f'Subpath '

from flask import url_for
app = Flask(__name__)
@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))