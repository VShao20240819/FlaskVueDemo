from flask import Flask
from flask_cors import CORS
from .api.home import home_bp
from .api.monitor import monitor_bp
from .api.operation import operation_bp
from .api.task import task_bp


def create_app():
    app = Flask(
        __name__,
        static_folder="../frontend/dist",      # Vue 打包输出目录
        template_folder="../frontend/dist"     # Vue index.html
    )

    CORS(app)

    app.register_blueprint(home_bp, url_prefix='/api/home')
    app.register_blueprint(monitor_bp, url_prefix='/api/monitor')
    app.register_blueprint(operation_bp, url_prefix='/api/operation')
    app.register_blueprint(task_bp, url_prefix='/api/task')

    return app
