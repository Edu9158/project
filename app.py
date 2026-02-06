from flask import Flask
from routes.tracking import bp_tracking
from routes.users import bp_users
import os

def create_app():
    app = flask(__name__)

    app.register_blueprint(bp_tracking, url_prefix='/api/v1/inventory')
    app.register_blueprint(bp_users, url_prefix='/api/v1/users')
    
    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)