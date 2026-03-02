import os
import importlib
from flask import Flask

from Managers.Herald import Herald
from Managers.Maggie import Maggie
from Managers.ConfigManager import ConfigManager

def register_blueprints(app):
    package_name = "ViewHandlers"
    package_path = os.path.join(os.path.dirname(__file__), package_name)

    for filename in os.listdir(package_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{package_name}.{filename[:-3]}"
            module = importlib.import_module(module_name)

            if hasattr(module, "result"):
                app.register_blueprint(module.result)

def create_app():
    app = Flask(__name__)
    app.maggie = Maggie("./data/events.json")
    app.herald = Herald("./data/announcements.json")
    app.secret_key = ConfigManager("key.cfg").get_key()
    register_blueprints(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
