#

2 approaches to Stripe forms: Checkout (quick) and Elements (customizable)

Using checkout:
https://stripe.com/docs/checkout/tutorial
1. drop this form block into your HTML
`<form action="/your-server-side-code" method="POST">
  <script
    src="https://checkout.stripe.com/checkout.js" class="stripe-button"
    data-key="pk_test_BLAHBLAHBLAH"
    data-amount="999"
    data-name="Speech Up Inc."
    data-description="Widget"
    data-zip-code="true" <!-- need to enable "declines on verification failures" in account settings -->
    data-image="https://stripe.com/img/documentation/checkout/marketplace.png"
    data-locale="auto">
  </script>
</form>`

2. set up server side code
(flask implementation)

a. install stripe and flask
`sudo pip install --upgrade stripe
sudo pip install flask`

b. HTTPS so that stripe can work
<!-- Install pyOpenSSL library
`pip install pyOpenSSL`

Update app.py to use ssl
`if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8100, ssl_context='adhoc')` -->
