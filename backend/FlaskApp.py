from flask import Flask
from flask_cors import CORS

from auth.ProcessLoginLogout import ToLoginLogout
from auth.CreateDeleteAccount import ToCreateDeleteAccount
from dashboard_api.ToFetchTemplate import ToFetchTemplate

app = Flask(__name__)

app.secret_key = 'oievjuonebioierpa'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_HTTPONLY'] = True

CORS(app, supports_credentials=True)

app.register_blueprint(ToLoginLogout,url_prefix="/auth")
app.register_blueprint(ToCreateDeleteAccount,url_prefix="/auth")
app.register_blueprint(ToFetchTemplate, url_prefix="/dashboard_api/")

@app.after_request
def headers_control(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response


@app.route('/')
def main_route():
    return 'whats up?'

if __name__ == '__main__':
    app.run(debug=True)
