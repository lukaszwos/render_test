from flask import Flask, request





app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello"


@app.route('/person', methods=['POST'])
def create_person():
    # POST request
    body = request.get_json()  # Get the request body content
    if body is None:
        return "The request body is null", 400
    if 'first_name' not in body:
        return 'You need to specify the first_name', 400
    if 'last_name' not in body:
        return 'You need to specify the last_name', 400

    return "potato", 200





@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}"


app.run(host='0.0.0.0', port=8080)
