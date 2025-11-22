from flask import Blueprint, request, jsonify


task_bp = Blueprint("task_bp", __name__)


@task_bp.route('/task_index', methods=['POST'])
def task_index():
    try:
        result_json_list = "task_index"
        return jsonify({"status": "success", "data": result_json_list,"msg": "查询成功"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500
