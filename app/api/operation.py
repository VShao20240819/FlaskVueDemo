from flask import Blueprint, request, jsonify


operation_bp = Blueprint("operation_bp", __name__)


@operation_bp.route('/operation_index', methods=['POST'])
def operation_index():
    try:
        result_json_list = "operation_index"
        return jsonify({"status": "success", "data": result_json_list,"msg": "查询成功"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500
