/* =========================================================
   BTEC HUB – Cart JavaScript
   Cart logic, localStorage, WhatsApp integration
   ========================================================= */

'use strict';

// ══════════════════════════════════════════
// CART STATE
// ══════════════════════════════════════════
let cartItems = JSON.parse(localStorage.getItem('btec-cart') || '[]');

// ══════════════════════════════════════════
// INIT
// ══════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  renderCart();
  updateCartBadge();
  initCartSidebar();
  initAddToCartButtons();
});

// ══════════════════════════════════════════
// CART SIDEBAR
// ══════════════════════════════════════════
function initCartSidebar() {
  const overlay = document.getElementById('cartOverlay');
  const sidebar = document.getElementById('cartSidebar');
  const closeBtn = document.getElementById('cartClose');
  const cartNavBtn = document.getElementById('cartNavBtn');

  function openCart() {
    overlay?.classList.add('open');
    sidebar?.classList.add('open');
    document.body.style.overflow = 'hidden';
    renderCart();
  }

  function closeCart() {
    overlay?.classList.remove('open');
    sidebar?.classList.remove('open');
    document.body.style.overflow = '';
  }

  cartNavBtn?.addEventListener('click', openCart);
  closeBtn?.addEventListener('click', closeCart);
  overlay?.addEventListener('click', closeCart);

  // ESC key
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeCart();
  });

  // Expose
  window.openCart = openCart;
  window.closeCart = closeCart;
}

// ══════════════════════════════════════════
// ADD TO CART
// ══════════════════════════════════════════
function initAddToCartButtons() {
  document.querySelectorAll('[data-add-to-cart]').forEach(btn => {
    btn.addEventListener('click', () => {
      const serviceId = btn.getAttribute('data-add-to-cart');
      const serviceName = btn.getAttribute('data-name');
      const servicePrice = btn.getAttribute('data-price') || 'contact';
      const serviceUnit = btn.getAttribute('data-unit') || '';
      const serviceIcon = btn.getAttribute('data-icon') || '📚';

      addToCart({
        id: serviceId,
        name: serviceName,
        price: servicePrice,
        unit: serviceUnit,
        icon: serviceIcon,
      });

      // Button feedback
      const original = btn.innerHTML;
      btn.innerHTML = `<i class="fas fa-check"></i> ${window.BtecMain?.t?.added || 'Added ✓'}`;
      btn.classList.add('added');
      btn.disabled = true;

      setTimeout(() => {
        btn.innerHTML = original;
        btn.classList.remove('added');
        btn.disabled = false;
      }, 2000);
    });
  });
}

// ══════════════════════════════════════════
// CART OPERATIONS
// ══════════════════════════════════════════
function addToCart(item) {
  // Check if already in cart
  const existing = cartItems.find(i => i.id === item.id);
  if (existing) {
    window.BtecMain?.showToast(
      window.BtecMain?.lang === 'ar' ? '⚠️ هذه الخدمة موجودة في السلة بالفعل' : '⚠️ This service is already in the cart',
      'info'
    );
    return;
  }

  cartItems.push(item);
  saveCart();
  updateCartBadge();
  renderCart();

  window.BtecMain?.showToast(
    window.BtecMain?.t?.toastAdded || '✓ Added to cart',
    'success'
  );
}

function removeFromCart(id) {
  cartItems = cartItems.filter(i => i.id !== id);
  saveCart();
  updateCartBadge();
  renderCart();

  window.BtecMain?.showToast(
    window.BtecMain?.t?.toastRemoved || 'Removed from cart',
    'info'
  );
}

function clearCart() {
  cartItems = [];
  saveCart();
  updateCartBadge();
  renderCart();

  window.BtecMain?.showToast(
    window.BtecMain?.t?.toastCleared || 'Cart cleared',
    'info'
  );
}

function saveCart() {
  localStorage.setItem('btec-cart', JSON.stringify(cartItems));
}

// ══════════════════════════════════════════
// RENDER CART
// ══════════════════════════════════════════
function renderCart() {
  const cartBody = document.getElementById('cartBody');
  const cartFooter = document.getElementById('cartFooter');
  if (!cartBody) return;

  const t = window.BtecMain?.t || {};

  if (cartItems.length === 0) {
    cartBody.innerHTML = `
      <div class="cart-empty">
        <div class="cart-empty-icon">🛒</div>
        <h3>${t.cartEmpty || 'Your cart is empty'}</h3>
        <p class="text-secondary">${t.cartEmptyDesc || 'Add services from the Services page'}</p>
        <a href="services.html" class="btn btn-primary btn-sm mt-lg" onclick="window.closeCart?.()">
          <i class="fas fa-plus"></i>
          ${window.BtecMain?.lang === 'ar' ? 'استعرض الخدمات' : 'Browse Services'}
        </a>
      </div>
    `;
    if (cartFooter) cartFooter.style.display = 'none';
    return;
  }

  if (cartFooter) cartFooter.style.display = '';

  // Render items
  const itemsHtml = cartItems.map(item => `
    <div class="cart-item" data-id="${item.id}">
      <div class="cart-item-icon">${item.icon}</div>
      <div class="cart-item-info">
        <div class="cart-item-name">${item.name}</div>
        <div class="cart-item-unit">${item.unit}</div>
      </div>
      <div class="cart-item-price">
        ${item.price === 'contact'
          ? `<span style="font-size:0.7rem;color:var(--accent)">${window.BtecMain?.lang === 'ar' ? 'سعر يُحدَّد' : 'TBD'}</span>`
          : item.price
        }
      </div>
      <button class="cart-item-remove" onclick="removeFromCart('${item.id}')" title="Remove">
        <i class="fas fa-times"></i>
      </button>
    </div>
  `).join('');

  cartBody.innerHTML = `<div class="cart-items">${itemsHtml}</div>`;

  // Count numeric prices
  const numericPrices = cartItems
    .map(i => parseFloat(i.price))
    .filter(p => !isNaN(p));

  const hasAllPrices = numericPrices.length === cartItems.length;
  const total = numericPrices.reduce((a, b) => a + b, 0);

  // Render footer
  if (cartFooter) {
    const currency = window.BtecMain?.lang === 'ar' ? 'ر.س' : 'SAR';
    cartFooter.innerHTML = `
      <div class="cart-summary">
        <div class="cart-summary-row">
          <span>${window.BtecMain?.lang === 'ar' ? 'عدد الخدمات' : 'Services count'}</span>
          <span>${cartItems.length} ${t.cartItems || 'items'}</span>
        </div>
        ${hasAllPrices ? `
        <div class="cart-summary-row total">
          <span>${t.cartTotal || 'Total'}</span>
          <span class="amount">${total} ${currency}</span>
        </div>
        ` : `
        <div class="cart-summary-row total">
          <span>${t.cartTotal || 'Total'}</span>
          <span style="font-size:0.85rem;color:var(--accent);-webkit-text-fill-color:var(--accent)">${window.BtecMain?.lang === 'ar' ? 'يُحدَّد عند التواصل' : 'To be confirmed'}</span>
        </div>
        `}
      </div>

      <div class="cart-actions">
        <button class="btn btn-whatsapp" onclick="sendCartViaWhatsApp()" style="width:100%;justify-content:center;">
          <i class="fab fa-whatsapp"></i>
          ${t.cartSend || 'Send via WhatsApp'}
        </button>
        <button class="btn-clear-cart" onclick="clearCart()">
          <i class="fas fa-trash-alt"></i>
          ${t.cartClear || 'Clear Cart'}
        </button>
      </div>

      <p class="cart-note">${t.cartNote || '* Final prices confirmed by our team'}</p>
    `;
  }
}

// ══════════════════════════════════════════
// SEND VIA WHATSAPP
// ══════════════════════════════════════════
function sendCartViaWhatsApp() {
  if (cartItems.length === 0) {
    window.BtecMain?.showToast(
      window.BtecMain?.t?.toastCartEmpty || 'Cart is empty!',
      'error'
    );
    return;
  }

  const message = window.BtecMain?.formatWhatsAppMessage(cartItems) || '';
  const link = window.BtecMain?.getWhatsAppLink(message) || '';
  window.open(link, '_blank');
}

// ══════════════════════════════════════════
// CART BADGE
// ══════════════════════════════════════════
function updateCartBadge() {
  const badges = document.querySelectorAll('.cart-badge');
  const count = cartItems.length;
  badges.forEach(badge => {
    badge.textContent = count;
    badge.style.display = count === 0 ? 'none' : 'flex';
  });
}

// ══════════════════════════════════════════
// EXPOSE GLOBALLY
// ══════════════════════════════════════════
window.addToCart = addToCart;
window.removeFromCart = removeFromCart;
window.clearCart = clearCart;
window.sendCartViaWhatsApp = sendCartViaWhatsApp;
window.getCartCount = () => cartItems.length;
window.getCartItems = () => cartItems;
