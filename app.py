import os
from flask import Flask, request, jsonify, send_from_directory
from conversation import send_message
from context import ContextStorage

app = Flask(__name__, static_folder='./build')

context_storage = ContextStorage()

@app.route('/test')
def test():

    return """
    <h1>Hello heroku</h1>

    <img src="http://loremflickr.com/600/400" />
    """

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    print('path',path)
    if path != "" and os.path.exists("./build/" + path):
        return send_from_directory('./build', path)
    else:
        return send_from_directory('./build', 'index.html')


@app.route('/message', methods=['post'])
def message():
    data = request.get_json(silent=True)
    context = context_storage.get_context(data['user_id'])
    response = send_message(data['text'], context)
    context_storage.set_context(data['user_id'], response['context'])
    return jsonify(**response)


if __name__ == '__main__':
    app.run(
        debug=os.environ.get("DEBUG", False),
        use_reloader=True)
