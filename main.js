/* =========================================================
   BTEC HUB – Master JavaScript (Optimized 60-120 FPS)
   Nimbus Liquid Glass Navbar, High-Performance 3D Tilt,
   Zero-Lag Wave Text, Smooth Cylindrical Showcase
   ========================================================= */

'use strict';

const WHATSAPP_NUMBER = '962786003597';

document.addEventListener('DOMContentLoaded', () => {
  initNimbusNavbar();
  initMobileNav();
  initWaveBrandSmooth();
  initHeroStageCardsSmooth();
  initCountUpStats();
  init3DTiltCardsSmooth();
  initTiltedCylinderSmooth();
  initAccordion();
  initFilterBars();
  initScrollTop();
  initSearchInputs();
});

// ══════════════════════════════════════════
// 1. HERO STAGE 3D CARDS & FLOATING WIDGETS (RAF THROTTLED)
// ══════════════════════════════════════════
function initHeroStageCardsSmooth() {
  const stage = document.getElementById('heroStage');
  if (!stage) return;

  const cards = stage.querySelectorAll('.stage-card');
  const widgets = stage.querySelectorAll('.floating-widget');
  if (!cards.length) return;

  let currentFront = 0;
  const classes = ['stage-card-1', 'stage-card-2', 'stage-card-3'];

  function updateStack() {
    cards.forEach((card, idx) => {
      classes.forEach(c => card.classList.remove(c));
      const pos = (idx - currentFront + cards.length) % cards.length;
      card.classList.add(classes[pos] || 'stage-card-3');
    });
  }

  // Click on a card to bring it forward
  cards.forEach((card, idx) => {
    card.addEventListener('click', () => {
      currentFront = idx;
      updateStack();
    });
  });

  // Automatic gentle rotation every 5.5s
  let autoTimer = setInterval(() => {
    currentFront = (currentFront + 1) % cards.length;
    updateStack();
  }, 5500);

  stage.addEventListener('mouseenter', () => clearInterval(autoTimer), { passive: true });
  stage.addEventListener('mouseleave', () => {
    autoTimer = setInterval(() => {
      currentFront = (currentFront + 1) % cards.length;
      updateStack();
    }, 5500);
  }, { passive: true });

  // High-Performance RAF-Throttled Parallax
  let rafId = 0;
  let mouseX = 0;
  let mouseY = 0;
  let stageRect = null;

  function onStageMove(e) {
    if (!stageRect) stageRect = stage.getBoundingClientRect();
    mouseX = ((e.clientX - stageRect.left) / stageRect.width - 0.5) * 2;
    mouseY = ((e.clientY - stageRect.top) / stageRect.height - 0.5) * 2;

    if (!rafId) {
      rafId = requestAnimationFrame(renderStageParallax);
    }
  }

  function renderStageParallax() {
    rafId = 0;
    for (let i = 0; i < widgets.length; i++) {
      const depth = (i + 1) * 7;
      const tx = -mouseX * depth;
      const ty = -mouseY * depth;
      widgets[i].style.transform = `translate3d(${tx.toFixed(1)}px, ${ty.toFixed(1)}px, 0) scale(1.04)`;
    }
  }

  stage.addEventListener('mouseenter', () => {
    stageRect = stage.getBoundingClientRect();
  }, { passive: true });

  stage.addEventListener('mousemove', onStageMove, { passive: true });

  stage.addEventListener('mouseleave', () => {
    if (rafId) {
      cancelAnimationFrame(rafId);
      rafId = 0;
    }
    stageRect = null;
    for (let i = 0; i < widgets.length; i++) {
      widgets[i].style.transform = '';
    }
  }, { passive: true });
}

// ══════════════════════════════════════════
// 2. ANIMATED COUNTUP STATS
// ══════════════════════════════════════════
function initCountUpStats() {
  const stats = document.querySelectorAll('.hero-stat-num');
  if (!stats.length) return;

  let animated = false;
  function trigger() {
    if (animated) return;
    animated = true;

    stats.forEach(el => {
      const raw = el.getAttribute('data-target') || el.textContent.trim();
      if (raw.includes('98.5')) {
        counter(el, 0, 98.5, 1400, '%', 1);
      } else if (raw.includes('1,400') || raw.includes('1400')) {
        counter(el, 0, 1400, 1600, '+', 0, true);
      } else if (raw.includes('100')) {
        counter(el, 0, 100, 1300, '%', 0);
      }
    });
  }

  function counter(el, start, end, duration, affix, decimals, isPrefix = false) {
    const startTime = performance.now();
    function tick(now) {
      const progress = Math.min(1, (now - startTime) / duration);
      const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      const current = start + (end - start) * ease;
      const numStr = decimals > 0 ? current.toFixed(decimals) : Math.floor(current).toLocaleString();
      el.textContent = isPrefix ? (affix + numStr) : (numStr + affix);
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  setTimeout(trigger, 150);
}

// ══════════════════════════════════════════
// 3. NIMBUS LIQUID GLASS NAVBAR (Spring Physics)
// ══════════════════════════════════════════
function initNimbusNavbar() {
  const nav = document.getElementById('nimbusNav');
  const drop = document.getElementById('nimbusDrop');
  if (!nav || !drop) return;

  const items = nav.querySelectorAll('.nimbus-item');
  let activeItem = nav.querySelector('.nimbus-item.active') || items[0];

  function positionDrop(target) {
    if (!target) {
      drop.style.opacity = '0';
      return;
    }
    const navRect = nav.getBoundingClientRect();
    const itemRect = target.getBoundingClientRect();
    const left = itemRect.left - navRect.left;
    const width = itemRect.width;

    drop.style.left = `${left}px`;
    drop.style.width = `${width}px`;
    drop.style.opacity = '1';
  }

  // Initial positioning with slight delay
  setTimeout(() => {
    positionDrop(activeItem);
  }, 60);

  window.addEventListener('resize', () => {
    positionDrop(activeItem);
  }, { passive: true });

  items.forEach(item => {
    item.addEventListener('mouseenter', () => {
      positionDrop(item);

      // Trigger icon micro-animation
      const ico = item.querySelector('.nv-ico');
      if (ico) {
        const fx = ico.getAttribute('data-fx');
        if (fx) {
          ico.style.animation = 'none';
          void ico.offsetWidth; // trigger reflow
          ico.style.animation = '';
        }
      }
    });
  });

  nav.addEventListener('mouseleave', () => {
    positionDrop(activeItem);
  });
}

// ══════════════════════════════════════════
// 4. MOBILE NAVIGATION DRAWER
// ══════════════════════════════════════════
function initMobileNav() {
  const toggle = document.getElementById('menuToggle');
  const drawer = document.getElementById('mobileNav');
  const close = document.getElementById('mobileNavClose');
  const overlay = document.getElementById('mobileNavOverlay');

  if (!toggle || !drawer) return;

  function openNav() {
    drawer.classList.add('open');
    if (overlay) overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeNav() {
    drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  toggle.addEventListener('click', openNav);
  if (close) close.addEventListener('click', closeNav);
  if (overlay) overlay.addEventListener('click', closeNav);
}

// ══════════════════════════════════════════
// 5. ZERO-LAG WAVE BRAND LOGO WITH CACHED GEOMETRY
// ══════════════════════════════════════════
function initWaveBrandSmooth() {
  const brands = document.querySelectorAll('.wave-brand');
  brands.forEach(brand => {
    const chars = Array.from(brand.querySelectorAll('.wave-char'));
    if (!chars.length) return;

    let brandRect = null;
    let charCenters = [];
    let rafId = 0;
    let clientX = -1000;
    let clientY = -1000;

    function cachePositions() {
      brandRect = brand.getBoundingClientRect();
      charCenters = chars.map(c => {
        const r = c.getBoundingClientRect();
        return {
          x: r.left + r.width / 2,
          y: r.top + r.height / 2
        };
      });
    }

    brand.addEventListener('mouseenter', () => {
      cachePositions();
    }, { passive: true });

    brand.addEventListener('mousemove', (e) => {
      clientX = e.clientX;
      clientY = e.clientY;
      if (!rafId) {
        rafId = requestAnimationFrame(updateWave);
      }
    }, { passive: true });

    function updateWave() {
      rafId = 0;
      if (!brandRect || !charCenters.length) return;

      const px = ((clientX - brandRect.left) / brandRect.width) * 100;
      const py = ((clientY - brandRect.top) / brandRect.height) * 100;

      for (let i = 0; i < chars.length; i++) {
        const center = charCenters[i];
        const dist = Math.hypot(clientX - center.x, clientY - center.y);

        if (dist < 60) {
          const force = (1 - dist / 60) * -8;
          chars[i].style.transform = `translate3d(0, ${force.toFixed(1)}px, 0) scale(1.12)`;
        } else {
          chars[i].style.transform = '';
        }
        chars[i].style.setProperty('--mouse-x', `${px.toFixed(1)}%`);
        chars[i].style.setProperty('--mouse-y', `${py.toFixed(1)}%`);
      }
    }

    brand.addEventListener('mouseleave', () => {
      if (rafId) {
        cancelAnimationFrame(rafId);
        rafId = 0;
      }
      chars.forEach(c => {
        c.style.transform = '';
      });
      brandRect = null;
    }, { passive: true });
  });
}

// ══════════════════════════════════════════
// 6. HIGH-PERFORMANCE 3D CARD TILT (RAF THROTTLED)
// ══════════════════════════════════════════
function init3DTiltCardsSmooth() {
  // Supports all card types including the new Gradient Cards (.gc-card)
  const cards = document.querySelectorAll(
    '.service-card, .spec-card, .study-card, .assignment-card, .contact-card, .ib-card, .stage-card, .gc-card'
  );

  cards.forEach(card => {
    card.classList.add('tilt-card-3d');

    if (!card.querySelector('.tilt-glare')) {
      const glare = document.createElement('div');
      glare.className = 'tilt-glare';
      card.appendChild(glare);
    }

    let rect = null;
    let rafId = 0;
    let localX = 0;
    let localY = 0;

    card.addEventListener('mouseenter', () => {
      rect = card.getBoundingClientRect();
    }, { passive: true });

    card.addEventListener('mousemove', (e) => {
      if (!rect) rect = card.getBoundingClientRect();
      localX = e.clientX - rect.left;
      localY = e.clientY - rect.top;

      if (!rafId) {
        rafId = requestAnimationFrame(updateCardTilt);
      }
    }, { passive: true });

    function updateCardTilt() {
      rafId = 0;
      if (!rect) return;

      const centerX = rect.width / 2;
      const centerY = rect.height / 2;

      // Subtle, buttery-smooth luxury tilt (max 5 deg)
      const rotateX = ((localY - centerY) / centerY) * -5;
      const rotateY = ((localX - centerX) / centerX) * 5;

      const glareX = (localX / rect.width) * 100;
      const glareY = (localY / rect.height) * 100;

      card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translate3d(0, -4px, 0)`;
      card.style.setProperty('--glare-x', `${glareX.toFixed(1)}%`);
      card.style.setProperty('--glare-y', `${glareY.toFixed(1)}%`);
    }

    card.addEventListener('mouseleave', () => {
      if (rafId) {
        cancelAnimationFrame(rafId);
        rafId = 0;
      }
      rect = null;
      card.style.transform = '';
      card.style.removeProperty('--glare-x');
      card.style.removeProperty('--glare-y');
    }, { passive: true });
  });
}

// ══════════════════════════════════════════
// 7. SMOOTH TILTED GRID 3D CYLINDER (RAF THROTTLED)
// ══════════════════════════════════════════
function initTiltedCylinderSmooth() {
  const track = document.getElementById('tghTrack');
  if (!track) return;

  let currentAngle = 0;
  let targetAngle = 0;
  let isDragging = false;
  let lastX = 0;
  let rafId = 0;

  function renderTrack() {
    currentAngle += (targetAngle - currentAngle) * 0.25;
    track.style.transform = `rotateY(${currentAngle.toFixed(2)}deg)`;

    if (Math.abs(targetAngle - currentAngle) > 0.05 || isDragging) {
      rafId = requestAnimationFrame(renderTrack);
    } else {
      rafId = 0;
    }
  }

  function startDrag(clientX) {
    isDragging = true;
    lastX = clientX;
    track.style.animationPlayState = 'paused';
    if (!rafId) rafId = requestAnimationFrame(renderTrack);
  }

  function moveDrag(clientX) {
    if (!isDragging) return;
    const deltaX = clientX - lastX;
    lastX = clientX;
    targetAngle += deltaX * 0.45;
  }

  function endDrag() {
    if (isDragging) {
      isDragging = false;
      setTimeout(() => {
        if (!isDragging) track.style.animationPlayState = '';
      }, 1200);
    }
  }

  track.parentElement.addEventListener('mousedown', (e) => startDrag(e.clientX));
  window.addEventListener('mousemove', (e) => moveDrag(e.clientX), { passive: true });
  window.addEventListener('mouseup', endDrag);

  track.parentElement.addEventListener('touchstart', (e) => startDrag(e.touches[0].clientX), { passive: true });
  window.addEventListener('touchmove', (e) => moveDrag(e.touches[0].clientX), { passive: true });
  window.addEventListener('touchend', endDrag);
}

// ══════════════════════════════════════════
// 8. ACCORDION (FAQ)
// ══════════════════════════════════════════
function initAccordion() {
  const items = document.querySelectorAll('.faq-item');
  items.forEach(item => {
    const q = item.querySelector('.faq-question');
    if (!q) return;

    q.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      items.forEach(i => i.classList.remove('open'));
      if (!isOpen) {
        item.classList.add('open');
      }
    });
  });
}

// ══════════════════════════════════════════
// 9. FILTER BARS
// ══════════════════════════════════════════
function initFilterBars() {
  const filterBars = document.querySelectorAll('.filter-bar');
  filterBars.forEach(bar => {
    const buttons = bar.querySelectorAll('.filter-btn');
    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const filter = btn.getAttribute('data-filter');
        const grid = document.querySelector('.services-grid, .study-grid, .assignment-grid, .faq-list');
        if (!grid) return;

        const cards = grid.children;
        Array.from(cards).forEach(card => {
          const cat = card.getAttribute('data-category');
          if (filter === 'all' || !cat || cat === filter) {
            card.style.display = '';
            card.style.opacity = '1';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  });
}

// ══════════════════════════════════════════
// 10. SEARCH INPUTS
// ══════════════════════════════════════════
function initSearchInputs() {
  const inputs = document.querySelectorAll('.search-input');
  inputs.forEach(input => {
    input.addEventListener('input', (e) => {
      const term = e.target.value.trim().toLowerCase();
      const grid = document.querySelector('.study-grid, .assignment-grid, .services-grid');
      if (!grid) return;

      const cards = grid.children;
      Array.from(cards).forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(term)) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

// ══════════════════════════════════════════
// 11. SCROLL TOP
// ══════════════════════════════════════════
function initScrollTop() {
  const btn = document.getElementById('scrollTopBtn');
  if (!btn) return;

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        if (window.scrollY > 400) {
          btn.style.opacity = '1';
          btn.style.visibility = 'visible';
        } else {
          btn.style.opacity = '0';
          btn.style.visibility = 'hidden';
        }
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}
