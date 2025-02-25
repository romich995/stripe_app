const stripe = Stripe('pk_test_51Qw4nPP0myC1Y5PW2vEw6IZ8u2cLjmVy8NPCoACHgABQ2kEb6CTkMHyreJo8ZwjubjajQJ4oq7AOrf2CZOjJUFq300eUl7B5yX');

const item_id = document.querySelector("#item_id").textContent;

console.log(item_id);

document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/buy/"+item_id)
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.session_id})
    })
    .then((res) => {
      console.log(res);
    });
  });