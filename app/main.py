from flask import Flask

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    return app

api = create_app()

@api.route("/")
def hello():
    return "Hello World from Flask in a uWSGI Nginx Docker container with \
     Python 3.7 (default)"

if __name__ == "__main__":
    api.run(host='0.0.0.0', debug=True, port=80)
