from flask import Blueprint

dispenser_view = Blueprint("dispenser", __name__)


@dispenser_view.route("/")
def dispenser():
    return "Hello, I'm the dispenser"


@dispenser_view.route("/name")
def dispenser_name():
    return "name"
