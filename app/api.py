from flask import Blueprint, jsonify, current_app

bp = Blueprint('api', __name__)


@bp.route("/currencies")
def get_currencies():
    """Get available currencies."""
    return jsonify({
        "status": "success",
        "result": current_app.config['CURRENCIES']
    })


@bp.route("/convert/<int:amount>/<string:cur_from>/<string:cur_to>")
@bp.route("/convert/<float:amount>/<string:cur_from>/<string:cur_to>")
def convert(amount: float, cur_from: str, cur_to: str):
    """Convert from one currency to another."""
    try:
        return jsonify({
            "status": "success",
            "result": current_app.rates.convert(amount, cur_from, cur_to)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": e.args[0]
        })
