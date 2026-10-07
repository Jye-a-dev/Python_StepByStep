from flask import Flask, request, make_response, redirect, url_for, jsonify

app = Flask(__name__)
# Gợi ý cho JSON response:


@app.route('/')
def index():
    return '<h1>Hello Flask Developers!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    return '''
    <h2>Request Information</h2>
    <p><strong>Method:</strong> {}</p>
    <p><strong>URL:</strong> {}</p>
    <p><strong>User-Agent:</strong> {}</p>
    <p><strong>Remote IP:</strong> {}</p>
    '''.format(request.method, request.url, user_agent, request.remote_addr)

@app.route('/cookie')
def set_cookie():
    response = make_response('<h1>Cookie has been set!</h1>')
    response.set_cookie('username', 'flask_user')
    return response

@app.route('/redirect-test')
def redirect_test():
    return redirect(url_for('index'))

# Optional: Error handler
@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Page Not Found</h1>', 404

@app.route('/api/users/<int:user_id>')
def get_user_api(user_id):
    user_data = {
        'id': user_id,
        'name': f'User {user_id}',
        'email': f'user{user_id}@example.com'
    }
    return jsonify(user_data)
