from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

ONLINE_REDIS_URI = ''

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri=ONLINE_REDIS_URI
)
def rate_limit_exceeded(e):
    from flask import jsonify
    return jsonify(error="ratelimit exceeded", message=str(e.description)), 429
