import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import Flask, request
from flask_wtf.csrf import CSRFProtect, generate_csrf

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET")
csrf = CSRFProtect(app)


@app.route("/csrf", methods=["GET"])
def _csrf_token():
    return generate_csrf()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=os.getenv("FLASK_DEBUG", False))
