from flask import Flask
from apps.dispenser import dispenser_view

app = Flask(__name__)
app.register_blueprint(dispenser_view, url_prefix="/dispenser")


@app.route("/")
def index():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
