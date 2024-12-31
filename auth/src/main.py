from flask import Flask
from config import Config
import os

from auth.login import login
from auth.logout import logout
from auth.register import register
from auth.session import sessionHandler
from auth.checkPerms import checkPerms
from auth.resetPassword import resetPassword

app = Flask(__name__)
app.config.from_object(Config)

# Use the custom session interface

app.add_url_rule("/auth/login", None, login, methods=["POST"])
app.add_url_rule("/auth/logout", None, logout, methods=["POST"])
app.add_url_rule("/auth/register", None, register, methods=["POST"])
app.add_url_rule("/auth/session", None, sessionHandler, methods=["POST"])
app.add_url_rule("/auth/checkPerms", None, checkPerms, methods=["POST"])
app.add_url_rule("/auth/resetPassword", None, resetPassword, methods=["POST"])


if __name__ == '__main__':
    app.run(debug=os.environ["DEBUG"], host="0.0.0.0", port=3000)
