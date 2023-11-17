import os
import re
import html
from datetime import datetime, date, timedelta
import json
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To, Content, From, ReplyTo
from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect, generate_csrf, validate_csrf

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET")
csrf = CSRFProtect(app)

# pattern is from Firefox's input type='email'
email_re = re.compile(
    r"^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
)

sg = SendGridAPIClient(os.getenv("SENDGRID_API"))
from_email = From(os.getenv("SENDGRID_FROM_EMAIL"))
to_email = To(os.getenv("SENDGRID_TO_EMAIL"))


def get_emails_remaining():
    d = datetime.today()
    ddate2 = d.strftime("%Y-%m-%d")
    params = {
        "aggregated_by": "day",
        "limit": 1,
        "start_date": ddate2,
        "end_date": ddate2,
        "offset": 1,
    }
    response = sg.client.stats.get(query_params=params)
    datas = json.loads(response.body)
    sent = datas[0]["stats"][0]["metrics"]["requests"]
    remain = 100 - int(sent)
    return remain


@app.route("/contact", methods=["GET", "POST"])
def csrf_token():
    emails_remain = get_emails_remaining()
    if emails_remain == 0:
        return "Unavailable", 507
    if request.method == "GET":
        return generate_csrf()
    else:
        # validate form
        email = request.form.get("contact_us_email", None)
        message = request.form.get("contact_us_message", None)
        if (
            email is None
            or message is None
            or len(email) == 0
            or len(message) == 0
            or not re.fullmatch(email_re, email)
        ):
            return "Invalid", 400
        # sanitize user input (jinja does this already)
        # message = html.escape(message)
        # build email
        subject = f"Contact Request: {email}"
        content = Content(
            "text/html",
            render_template(
                "mail.html",
                contact_email=email,
                contact_message=message,
            ),
        )
        mail = Mail(from_email, to_email, subject, content)
        mail.reply_to = ReplyTo(email)
        response = sg.send(mail)
        return "", response.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=os.getenv("FLASK_DEBUG", False))
