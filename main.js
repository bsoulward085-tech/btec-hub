/* =========================================================
   BTEC HUB – Main JavaScript
   Theme, Language, Navigation, Scroll, Animations
   ========================================================= */

'use strict';

// ══════════════════════════════════════════
// CONSTANTS
// ══════════════════════════════════════════
const WHATSAPP_NUMBER = '962786003597'; // ← رقم واتساب BTEC HUB

const TRANSLATIONS = {
  ar: {
    dir: 'rtl',
    navHome: 'الرئيسية',
    navServices: 'الخدمات',
    navSpecs: 'التخصصات',
    navStudy: 'الدراسة',
    navAssignments: 'مهمات سابقة',
    navAI: 'BTEC AI',
    navFAQ: 'الأسئلة الشائعة',
    navContact: 'تواصل معنا',
    navCart: 'السلة',
    cartEmpty: 'سلتك فارغة',
    cartEmptyDesc: 'أضف خدمات من صفحة الخدمات',
    cartItems: 'عناصر',
    cartTotal: 'الإجمالي',
    cartNote: '* الأسعار النهائية تُحدَّد عبر التواصل المباشر مع الفريق',
    cartSend: 'إرسال عبر واتساب 📲',
    cartClear: 'مسح السلة',
    addToCart: 'أضف للسلة',
    added: 'تمت الإضافة ✓',
    askAssistant: 'اسأل المساعد',
    contactPrice: 'تواصل للسعر',
    assistantName: 'BTEC Assistant',
    assistantStatus: 'متاح الآن',
    assistantPlaceholder: 'اكتب سؤالك هنا...',
    whatsappTooltip: 'تواصل معنا',
    scrollTop: 'للأعلى',
    toastAdded: '✓ تمت إضافة الخدمة للسلة',
    toastRemoved: 'تم حذف الخدمة من السلة',
    toastCleared: 'تم مسح السلة',
    toastCartEmpty: 'السلة فارغة! أضف خدمات أولاً',
    themeLight: 'الوضع الفاتح',
    themeDark: 'الوضع الداكن',
  },
  en: {
    dir: 'ltr',
    navHome: 'Home',
    navServices: 'Services',
    navSpecs: 'Specializations',
    navStudy: 'Study',
    navAssignments: 'Past Assignments',
    navAI: 'BTEC AI',
    navFAQ: 'FAQ',
    navContact: 'Contact',
    navCart: 'Cart',
    cartEmpty: 'Your cart is empty',
    cartEmptyDesc: 'Add services from the Services page',
    cartItems: 'items',
    cartTotal: 'Total',
    cartNote: '* Final prices are confirmed by our team directly',
    cartSend: 'Send via WhatsApp 📲',
    cartClear: 'Clear Cart',
    addToCart: 'Add to Cart',
    added: 'Added ✓',
    askAssistant: 'Ask Assistant',
    contactPrice: 'Contact for Price',
    assistantName: 'BTEC Assistant',
    assistantStatus: 'Online now',
    assistantPlaceholder: 'Type your question...',
    whatsappTooltip: 'Contact us',
    scrollTop: 'Top',
    toastAdded: '✓ Service added to cart',
    toastRemoved: 'Service removed from cart',
    toastCleared: 'Cart cleared',
    toastCartEmpty: 'Cart is empty! Add services first',
    themeLight: 'Light Mode',
    themeDark: 'Dark Mode',
  }
};

// ══════════════════════════════════════════
// STATE
// ══════════════════════════════════════════
let currentLang = localStorage.getItem('btec-lang') || 'ar';
let currentTheme = localStorage.getItem('btec-theme') || 'dark';

// ══════════════════════════════════════════
// INIT
// ══════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  applyTheme(currentTheme);
  applyLanguage(currentLang);
  initNavbar();
  initScrollEffects();
  initRevealAnimations();
  initScrollTop();
  initParticles();
  highlightActiveNav();
});

// ══════════════════════════════════════════
// THEME
// ══════════════════════════════════════════
function applyTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('btec-theme', theme);

  const icon = document.getElementById('themeIcon');
  if (icon) {
    icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
  const mobileIcon = document.getElementById('mobileThemeIcon');
  if (mobileIcon) {
    mobileIcon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
  }
}

function toggleTheme() {
  applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
}

// ══════════════════════════════════════════
// LANGUAGE
// ══════════════════════════════════════════
function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('btec-lang', lang);

  const t = TRANSLATIONS[lang];
  document.documentElement.lang = lang;
  document.documentElement.dir = t.dir;

  // Update all [data-i18n] elements
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (t[key] !== undefined) el.textContent = t[key];
  });

  // Update placeholders
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (t[key] !== undefined) el.placeholder = t[key];
  });

  // Update lang toggle text
  const langToggle = document.getElementById('langText');
  if (langToggle) langToggle.textContent = lang === 'ar' ? 'EN' : 'ع';
  const mobileLangText = document.getElementById('mobileLangText');
  if (mobileLangText) mobileLangText.textContent = lang === 'ar' ? 'EN' : 'ع';
}

function toggleLanguage() {
  applyLanguage(currentLang === 'ar' ? 'en' : 'ar');
}

// ══════════════════════════════════════════
// NAVBAR
// ══════════════════════════════════════════
function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const menuToggle = document.getElementById('menuToggle');
  const mobileNav = document.getElementById('mobileNav');
  const overlay = document.getElementById('mobileNavOverlay');

  // Scroll effect
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 20) {
      navbar.classList.add('navbar-blur');
      navbar.style.height = currentScroll > lastScroll && currentScroll > 300
        ? '0' : '';
    } else {
      navbar.classList.remove('navbar-blur');
    }

    lastScroll = currentScroll;
  }, { passive: true });

  // Mobile menu
  if (menuToggle) {
    menuToggle.addEventListener('click', () => {
      const isOpen = mobileNav.classList.toggle('open');
      menuToggle.innerHTML = isOpen
        ? '<i class="fas fa-times"></i>'
        : '<i class="fas fa-bars"></i>';
      if (overlay) overlay.classList.toggle('open', isOpen);
    });
  }

  if (overlay) {
    overlay.addEventListener('click', closeMobileNav);
  }

  // Close on link click
  document.querySelectorAll('.mobile-nav-links .nav-link').forEach(link => {
    link.addEventListener('click', closeMobileNav);
  });

  function closeMobileNav() {
    mobileNav?.classList.remove('open');
    if (menuToggle) menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
    overlay?.classList.remove('open');
  }
}

function highlightActiveNav() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link[data-page]').forEach(link => {
    const page = link.getAttribute('data-page');
    if (page === currentPage || (currentPage === '' && page === 'index.html')) {
      link.classList.add('active');
    }
  });
}

// ══════════════════════════════════════════
// SCROLL EFFECTS
// ══════════════════════════════════════════
function initScrollEffects() {
  window.addEventListener('scroll', () => {
    updateScrollTop();
  }, { passive: true });
}

// ══════════════════════════════════════════
// SCROLL TOP
// ══════════════════════════════════════════
function initScrollTop() {
  const btn = document.getElementById('scrollTopBtn');
  if (!btn) return;

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

function updateScrollTop() {
  const btn = document.getElementById('scrollTopBtn');
  if (!btn) return;
  btn.classList.toggle('visible', window.pageYOffset > 400);
}

// ══════════════════════════════════════════
// REVEAL ANIMATIONS (Intersection Observer)
// ══════════════════════════════════════════
function initRevealAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('revealed');
        }, i * 80);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

// ══════════════════════════════════════════
// PARTICLES
// ══════════════════════════════════════════
function initParticles() {
  const container = document.querySelector('.hero-particles');
  if (!container) return;

  const count = window.matchMedia('(max-width: 768px)').matches ? 8 : 15;

  for (let i = 0; i < count; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    const size = Math.random() * 6 + 3;
    const duration = Math.random() * 15 + 10;
    const delay = Math.random() * 10;
    const left = Math.random() * 100;

    p.style.cssText = `
      width: ${size}px;
      height: ${size}px;
      left: ${left}%;
      animation-duration: ${duration}s;
      animation-delay: ${delay}s;
    `;
    container.appendChild(p);
  }
}

// ══════════════════════════════════════════
// ACCORDION
// ══════════════════════════════════════════
function initAccordion() {
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const isOpen = item.classList.contains('open');

      // Close all
      document.querySelectorAll('.accordion-item.open').forEach(i => {
        i.classList.remove('open');
      });

      // Open clicked
      if (!isOpen) item.classList.add('open');
    });
  });
}

// ══════════════════════════════════════════
// FILTERS
// ══════════════════════════════════════════
function initFilters(containerSelector, cardSelector) {
  const filterBtns = document.querySelectorAll('.filter-btn');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');
      const cards = document.querySelectorAll(cardSelector);

      cards.forEach(card => {
        if (filter === 'all' || card.getAttribute('data-category') === filter) {
          card.style.display = '';
          setTimeout(() => card.classList.add('revealed'), 10);
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

// ══════════════════════════════════════════
// SEARCH
// ══════════════════════════════════════════
function initSearch(inputId, cardSelector, searchFields) {
  const input = document.getElementById(inputId);
  if (!input) return;

  input.addEventListener('input', debounce(() => {
    const query = input.value.toLowerCase().trim();
    const cards = document.querySelectorAll(cardSelector);

    cards.forEach(card => {
      const text = searchFields.map(f => {
        const el = card.querySelector(f);
        return el ? el.textContent.toLowerCase() : '';
      }).join(' ');

      card.style.display = !query || text.includes(query) ? '' : 'none';
    });
  }, 300));
}

// ══════════════════════════════════════════
// TOAST NOTIFICATIONS
// ══════════════════════════════════════════
function showToast(message, type = 'info', duration = 3000) {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const icons = { success: 'fa-check-circle', error: 'fa-times-circle', info: 'fa-info-circle' };

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <i class="fas ${icons[type] || icons.info} toast-icon"></i>
    <span>${message}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add('removing');
    setTimeout(() => toast.remove(), 300);
  }, duration);
}

// ══════════════════════════════════════════
// UTILITIES
// ══════════════════════════════════════════
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

function formatWhatsAppMessage(items) {
  const t = TRANSLATIONS[currentLang];
  const lines = items.map(item =>
    `• ${item.name}${item.price && item.price !== 'contact' ? ` — ${item.price}` : ' — سعر يُحدَّد'}`
  );

  return encodeURIComponent(
    `🎓 *BTEC HUB – طلب خدمة*\n\n${lines.join('\n')}\n\n---\n📌 أرجو تأكيد السعر والتفاصيل\nشكراً!`
  );
}

function getWhatsAppLink(message) {
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${message}`;
}

// Expose globally
window.BtecMain = {
  toggleTheme,
  toggleLanguage,
  showToast,
  getWhatsAppLink,
  formatWhatsAppMessage,
  WHATSAPP_NUMBER,
  get lang() { return currentLang; },
  get t() { return TRANSLATIONS[currentLang]; },
  initAccordion,
  initFilters,
  initSearch,
};
