from flask import Blueprint, request, jsonify


monitor_bp = Blueprint("monitor_bp", __name__)


@monitor_bp.route('/monitor_index', methods=['POST'])
def monitor_index():
    try:
        result_json_list = "monitor_index"
        return jsonify({"status": "success", "data": result_json_list,"msg": "查询成功"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500
