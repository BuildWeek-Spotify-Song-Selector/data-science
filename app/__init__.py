
from flask import Flask
import threading, webbrowser
from flask_cors import CORS

from app.routes.home_routes import home_routes
from app.routes.database_routes import database_routes
from app.routes.model_routes import model_routes
from app.routes.spotipy_routes import spotipy_routes
from app.routes.log_routes import log_routes



def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_routes)
    app.register_blueprint(database_routes)
    app.register_blueprint(model_routes)
    app.register_blueprint(spotipy_routes)
    app.register_blueprint(log_routes)

    CORS(app)

    return app

if __name__ == "__main__":
    my_app = create_app()

    port = 5003
    host = "127.0.0.1"
    url = f"http://127.0.0.1:{port}"

    threading.Timer(0.5, lambda: webbrowser.open(url) ).start()
    print("Starting Flask_API")

    my_app.run(host=host, port=port, debug=False)
