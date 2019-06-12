from flask import Flask, render_template, request
from flaskext.mail import Mail, Message

mail=Mail(app)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'gansteamtcu@gmail.com',
	MAIL_PASSWORD = 'GansInSecurity'
	)
# import sendgrid
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import *

# sg = sendgrid.SendGridAPIClient('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')
# message = Mail(
#     from_email='kimhoang7994@gmail.com',
#     to_emails='kimhoang7994@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/authors")
def authors():
    return render_template("authors.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/form', methods=['POST'])
def form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    mail = Mail()
    return render_template("contact.html")  

if __name__ == "__main__":
    app.run(debug=True)
