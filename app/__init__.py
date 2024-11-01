from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register your blueprint
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app

app = create_app()
