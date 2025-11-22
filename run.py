from flask import send_from_directory
from app import create_app


app = create_app()

# 前端页面路由
@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')


# 如果使用 Vue Router（前端有多页面路由）
@app.route('/<path:path>')
def static_proxy(path):
    try:
        return send_from_directory(app.template_folder, path)

    except:
        # 如果路径不存在（比如 Vue 前端路由），返回 index.html
        return send_from_directory(app.template_folder, 'index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
