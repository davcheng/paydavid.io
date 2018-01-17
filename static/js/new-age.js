(function($) {
  "use strict"; // Start of use strict


  // // Stripe payment JS
  // // Step 1: Create card element (replace key below with account key)
  // // Create a Stripe client
  // var stripe = Stripe('pk_test_ElBQzyLjVbA3wHv9JDe82TIU');
  // // Create an instance of Elements
  // var elements = stripe.elements();
  //
  // // Step 2: Create an instance of an Element and mount it to the HTML Element container (payment form)
  // // Custom styling can be passed to options when creating an Element.
  // var style = {
  //   base: {
  //     color: '#32325d',
  //     lineHeight: '18px',
  //     fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
  //     fontSmoothing: 'antialiased',
  //     fontSize: '16px',
  //     '::placeholder': {
  //       color: '#aab7c4'
  //     }
  //   },
  //   invalid: {
  //     color: '#fa755a',
  //     iconColor: '#fa755a'
  //   }
  // };
  //
  // // Create an instance of the card Element
  // var card = elements.create('card', {style: style});
  //
  // // Add an instance of the card Element into the `card-element` <div>
  // card.mount('#card-element');
  //
  // // Step 3: Error catching
  // card.addEventListener('change', function(event) {
  // var displayError = document.getElementById('card-errors');
  // if (event.error) {
  //     displayError.textContent = event.error.message;
  //   } else {
  //     displayError.textContent = '';
  //   }
  // });
  //
  // // Step 4: Handle form submission
  // var form = document.getElementById('payment-form');
  // form.addEventListener('submit', function(event) {
  //   event.preventDefault();
  //
  //   stripe.createToken(card).then(function(result) {
  //     if (result.error) {
  //       // Inform the user if there was an error
  //       var errorElement = document.getElementById('card-errors');
  //       errorElement.textContent = result.error.message;
  //     } else {
  //       // Send the token to your server
  //       stripeTokenHandler(result.token);
  //     }
  //   });
  // });
  //
  // //Step 5: Submit the token and form to Server
  // function stripeTokenHandler(token) {
  //   // Insert the token ID into the form so it gets submitted to the server
  //   var form = document.getElementById('payment-form');
  //   var hiddenInput = document.createElement('input');
  //   hiddenInput.setAttribute('type', 'hidden');
  //   hiddenInput.setAttribute('name', 'stripeToken');
  //   hiddenInput.setAttribute('value', token.id);
  //   form.appendChild(hiddenInput);
  //
  //   // Submit the form
  //   conosle.log(form);
  //   form.submit();
  // }


  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 48)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 54
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

})(jQuery); // End of use strict
