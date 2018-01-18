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
        email='customer@example.com', # pass in from login?
        source=request.form['stripeToken']
    )
    # print(customer)
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='pay david'
    )

    subscription = stripe.Subscription.create(
      customer=customer.id,
      items=[
        {
          "plan": "basic-monthly",
        },
      ],
    )
    print(subscription)

    return render_template('charge.html', amount=amount)


@app.route('/sub', methods=['POST'])
def sub():
    amount = 1000000
    customer = stripe.Customer.create(
        email='customer@example.com', # pass in from login?
        source=request.form['stripeToken']
    )

    subscription = stripe.Subscription.create(
      customer=customer.id,
      items=[
        {
          "plan": "basic-monthly",
        },
      ],
    )
    print(subscription)

    return render_template('charge.html', amount=amount)

# Subscriptions
# Create plan via:
# curl https://api.stripe.com/v1/plans \
#    -u sk_test_bJ7tT1WKB1oFfqOyDAHn6vi3: \
#    -d name="Basic Plan" \
#    -d id=basic-monthly \
#    -d interval=month \
#    -d currency=usd \
#    -d amount=999

# app.route('/subscribe', methods=['POST'])
# def subscribe(email, stripe_token, plan):
#     print('sup')
#     stripe.api_key = "sk_test_bJ7tT1WKB1oFfqOyDAHn6vi3"
#
#     customer = stripe.Customer.create(
#       email=email,
#       source=stripe_token,
#       plan=plan
#     )
#
#     stripe.Subscription.create(
#       customer="cus_4fdAW5ftNQow1a",
#       items=[
#         {
#           "plan": "basic-monthly",
#         },
#       ],
#     )
#     return render_template('charge.html', amount=amount)

# app.route('/subscribe', methods=['POST'])
def subscribe(email, stripe_token, plan):
    print('sup')
    stripe.api_key = "sk_test_bJ7tT1WKB1oFfqOyDAHn6vi3"

    customer = stripe.Customer.create(
      email=email,
      source=stripe_token,
      plan=plan
    )

    stripe.Subscription.create(
      customer=customer.id,
      items=[
        {
          "plan": "basic-monthly",
        },
      ],
    )
    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    # app.run('0.0.0.0', debug=True, port=8100, ssl_context='adhoc')
    app.run(debug=True)
