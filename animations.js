/* =========================================================
   BTEC HUB – Motion & Polish Layer (JS)
   Loaded after main.js. Everything here is progressive
   enhancement: if this file fails, the site still works.
   ========================================================= */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canHover = window.matchMedia('(hover: hover)').matches;

  // ── 1. Page loader ─────────────────────────────────────
  function hideLoader() {
    var loader = document.querySelector('.page-loader');
    if (!loader) return;
    loader.classList.add('done');
    setTimeout(function () { loader.remove(); }, 700);
  }
  var started = Date.now();
  window.addEventListener('load', function () {
    var wait = Math.max(0, 450 - (Date.now() - started));
    setTimeout(hideLoader, wait);
  });

  // ── 2. Scroll progress bar ─────────────────────────────
  function initScrollProgress() {
    var bar = document.createElement('div');
    bar.className = 'scroll-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);

    var ticking = false;
    function update() {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      var p = h > 0 ? Math.min(1, window.pageYOffset / h) : 0;
      bar.style.transform = 'scaleX(' + p + ')';
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  // ── 3. Hero title: split into words for staggered entrance ─
  function initHeroTitle() {
    var title = document.querySelector('.hero-title');
    if (!title || reduceMotion) return;
    var i = 0;
    var nodes = Array.prototype.slice.call(title.childNodes);
    nodes.forEach(function (node) {
      if (node.nodeType === 3) {                       // text node
        var frag = document.createDocumentFragment();
        node.textContent.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(' ')); return; }
          var w = document.createElement('span');
          w.className = 'word';
          w.style.setProperty('--i', i++);
          w.textContent = part;
          frag.appendChild(w);
        });
        title.replaceChild(frag, node);
      } else if (node.nodeType === 1 && node.tagName !== 'BR') {   // e.g. .glow-text
        node.classList.add('word');
        node.style.setProperty('--i', i++);
      }
    });
  }

  // ── 4. Stagger reveals by position inside their grid ───
  function initRevealStagger() {
    var groups = document.querySelectorAll(
      '.features-grid, .grid-2, .grid-3, .grid-4, .services-grid, .study-grid, .assignments-grid'
    );
    groups.forEach(function (group) {
      var kids = Array.prototype.filter.call(group.children, function (el) {
        return el.classList.contains('reveal');
      });
      kids.forEach(function (el, idx) {
        el.style.setProperty('--reveal-delay', (idx % 6) * 90 + 'ms');
      });
    });
    // Once a card has finished revealing, drop its delay so hover effects feel instant
    document.addEventListener('transitionend', function (e) {
      if (e.propertyName === 'opacity' && e.target.classList &&
          e.target.classList.contains('revealed')) {
        e.target.style.setProperty('--reveal-delay', '0ms');
      }
    });
  }

  // ── 5. Animated counters ───────────────────────────────
  function initCounters() {
    var els = document.querySelectorAll('.stat-number, .hero-stat-num');
    var items = [];
    els.forEach(function (el) {
      var m = el.textContent.trim().match(/^(\d+)(\D*)$/);    // "500+", "98%", "4" – skips "24/7"
      if (!m) return;
      items.push({ el: el, target: parseInt(m[1], 10), suffix: m[2] });
      if (!reduceMotion) el.textContent = '0' + m[2];
    });
    if (!items.length || reduceMotion) return;

    function run(item) {
      var dur = 1600, t0 = null;
      function frame(t) {
        if (t0 === null) t0 = t;
        var p = Math.min(1, (t - t0) / dur);
        var eased = 1 - Math.pow(1 - p, 4);                    // easeOutQuart
        item.el.textContent = Math.round(item.target * eased) + item.suffix;
        if (p < 1) requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var item = items.find(function (it) { return it.el === e.target; });
        if (item) run(item);
        io.unobserve(e.target);
      });
    }, { threshold: 0.4 });
    items.forEach(function (it) { io.observe(it.el); });
  }

  // ── 6. Cursor-follow glow on cards ─────────────────────
  function initCardGlow() {
    if (!canHover || reduceMotion) return;
    var sel = '.feature-card, .spec-card, .service-card, .stat-card, .testimonial-card, ' +
              '.study-card, .assignment-card, .process-track .card';
    document.querySelectorAll(sel).forEach(function (card) {
      card.classList.add('fx-card');
      var glow = document.createElement('span');
      glow.className = 'fx-glow';
      glow.setAttribute('aria-hidden', 'true');
      card.appendChild(glow);
      card.addEventListener('pointermove', function (e) {
        var r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      }, { passive: true });
    });
  }

  // ── 7. Button ripple ───────────────────────────────────
  function initRipple() {
    if (reduceMotion) return;
    document.addEventListener('pointerdown', function (e) {
      var btn = e.target.closest('.btn, .btn-cta-white, .btn-cta-outline');
      if (!btn) return;
      var r = btn.getBoundingClientRect();
      var size = Math.max(r.width, r.height) * 2;
      var dot = document.createElement('span');
      dot.className = 'ripple-dot';
      dot.style.width = dot.style.height = size + 'px';
      dot.style.left = (e.clientX - r.left - size / 2) + 'px';
      dot.style.top = (e.clientY - r.top - size / 2) + 'px';
      btn.appendChild(dot);
      setTimeout(function () { dot.remove(); }, 700);
    });
  }

  // ── 8. Smooth in-page anchors (e.g. specializations.html#it) ─
  function initAnchors() {
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href^="#"]');
      if (!a || a.getAttribute('href') === '#') return;
      var target = document.querySelector(a.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.pageYOffset - 90;
      window.scrollTo({ top: top, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initScrollProgress();
    initHeroTitle();
    initRevealStagger();
    initCounters();
    initCardGlow();
    initRipple();
    initAnchors();
  });
})();
