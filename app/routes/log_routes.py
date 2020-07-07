
from flask import Blueprint
from app.log.log_error import get_errors
import json


log_routes = Blueprint("log_routes", __name__)


@log_routes.route("/log/get_logs", methods=["GET"])
def get_logs():
    logs = get_errors()
    return json.dumps(logs)
