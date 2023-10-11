from flask import Flask

from apps.dispenser import dispenser_view
from db.database import db

# App setup
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dispensers.db"
db.init_app(app)

# Blueprints
app.register_blueprint(dispenser_view, url_prefix="/dispenser")


@app.route("/")
def index():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
