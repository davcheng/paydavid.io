import os
from flask import Flask, render_template, request
import stripe

# stripe_keys = {
#   'secret_key': os.environ['SECRET_KEY'],
#   'publishable_key': os.environ['PUBLISHABLE_KEY']
# }

stripe_keys = {
  'secret_key': "sk_test_bJ7tT1WKB1oFfqOyDAHn6vi3",
  'publishable_key': "pk_test_tejtVd6kHBNBu5H6OHM3aqGU"
}


stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

# data-key="pk_test_tejtVd6kHBNBu5H6OHM3aqGU"
@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = 999

    customer = stripe.Customer.create(
        email='customer@example.com',
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    # app.run('0.0.0.0', debug=True, port=8100, ssl_context='adhoc')
    app.run(debug=True)
