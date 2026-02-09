// static/js/cart.js
function updateCartUI() {
    const cartCount = document.getElementById('cart-count');
    const cartData = JSON.parse(localStorage.getItem('cart')) || [];
    
    if (cartCount) {
        cartCount.innerText = cartData.length;
        // Add a small animation effect
        cartCount.classList.add('bump');
        setTimeout(() => cartCount.classList.remove('bump'), 300);
    }
}

// Call this on page load
document.addEventListener('DOMContentLoaded', updateCartUI);