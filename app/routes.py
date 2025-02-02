from flask import Flask, request, jsonify
from .rate_limiter import RateLimiter
from .ip_blocker import IPBlocker
from .utils import get_ip_details, setup_logger
from config import Config

app = Flask(__name__)
logger = setup_logger()
rate_limiter = RateLimiter()
ip_blocker = IPBlocker()

@app.before_request
def check_for_attack():
    try:
        client_ip = request.remote_addr
        
        if ip_blocker.is_blocked(client_ip):
            return jsonify({"error": "IP blocked"}), 403
        
        if rate_limiter.is_over_limit(client_ip):
            ip_blocker.block_ip(client_ip, "DDoS threshold exceeded")
            attacker_details = get_ip_details(client_ip)
            logger.warning("DDoS attack detected", extra={
                **attacker_details,
                "threshold": Config.REQUEST_LIMIT
            }), 429

    except Exception as e:
        logger.error("Error in request processing", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

@app.route('/')
def home():
    return jsonify({"status": "protected"})

@app.route('/blocked-ips')
def list_blocked_ips():
    cursor = ip_blocker.conn.execute("SELECT * FROM blocked_ips")
    return jsonify(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=False)
