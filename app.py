from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)
run_with_ngrok(app)  
public_key = "pk_test_51H7J7yJwiDVNZZDoyR6SKCYw44B9IAfhBIZFbk6T50XQ0jmmbHTdhJowDp9jkRgBpzF9amg4CbXEnEMpIoBemh8U00b2uZNk9A"
stripe.api_key = "sk_test_51H7J7yJwiDVNZZDoWs4MPVzoC7lDW52LivCKT2CaKRTB2M1lFUNj3OEyaFMpiW50s8HMz1MerkXJZxy9lhengFpt00ON002ma6"
@app.route('/')
def index():
    return render_template('index.html', public_key=public_key)


@app.route('/payment', methods=['POST'])
def payment():
    suma = 199999
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source = request.form['stripeToken'])
    charge = stripe.Charge.create(
    customer=customer.id,
    amount=suma,
    currency='usd'
    )

    return render_template("thankyou.html", suma=suma/100)

if __name__ == '__main__':
    app.run()
