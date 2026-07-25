from flask import Flask, render_template, request, redirect, flash, send_from_directory
from flask_mail import Mail, Message
import os

# ==========================================
# Flask Configuration
# ==========================================

app = Flask(__name__)
app.secret_key = "chaithna_portfolio_secret_key"

# ==========================================
# Mail Configuration
# ==========================================

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_TIMEOUT"] = 10

app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")

mail = Mail(app)

# ==========================================
# Home Page
# ==========================================

@app.route("/contact", methods=["POST"])
def contact():

    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    try:
        # Check whether environment variables are loaded
        if not app.config["MAIL_USERNAME"] or not app.config["MAIL_PASSWORD"]:
            raise Exception("MAIL_USERNAME or MAIL_PASSWORD is not set.")

        msg = Message(
            subject=f"New Portfolio Contact: {subject}",
            sender=app.config["MAIL_USERNAME"],
            recipients=[app.config["MAIL_USERNAME"]]
        )

        msg.body = f"""
You have received a new message from your portfolio website.

----------------------------------------
Name    : {name}
Email   : {email}
Subject : {subject}

Message
----------------------------------------

{message}

----------------------------------------
This message was sent from your portfolio contact form.
"""

        print("Connecting to Gmail SMTP...")
        mail.send(msg)
        print("Email sent successfully!")

        flash("Message sent successfully!", "success")

    except Exception as e:
        print("=" * 60)
        print("MAIL ERROR")
        print(type(e).__name__)
        print(str(e))
        print("=" * 60)

        flash(f"Mail Error: {str(e)}", "danger")

    return redirect("/#contact")

# ==========================================
# Resume Download
# ==========================================

@app.route("/resume")
def download_resume():

    return send_from_directory(
        "static/resume",
        "resume.pdf"
    )


# ==========================================
# Error Pages
# ==========================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html"), 404


@app.errorhandler(500)
def server_error(error):
    return "<h1>Internal Server Error</h1>", 500


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
