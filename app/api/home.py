from flask import Blueprint, request, jsonify


home_bp = Blueprint("home_bp", __name__)


@home_bp.route('/home_index', methods=['POST'])
def home_index():
    try:
        result_json_list = "home_index"
        return jsonify({"status": "success", "data": result_json_list,"msg": "查询成功"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500
