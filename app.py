from chalice import Chalice

app = Chalice(app_name='helloworld')


@app.route('/', api_key_required=True)
def index():
    return {'hello': 'world'}


@app.route('/hello/{name}', api_key_required=True)
def hello_name(name):
    return {'hello': name}


# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.json_body
#     # Suppose we had some 'db' object that we used to
#     # read/write from our database.
#     # user_id = db.create_user(user_as_json)
#     return {'user_id': user_id}
#
# See the README documentation for more examples.
#
