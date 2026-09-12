# -*- coding: utf-8 -*-
"""
rebuild_proper.py  –  Restores all 7 BTEC HUB pages with the ORIGINAL design.
Run: python rebuild_proper.py  (from any working directory)
"""

import os

OUT = r"C:\Users\bsoul\Desktop\btec-hub"

# ── shared head ────────────────────────────────────────────────────────────────
def head(title):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="main.css">
  <link rel="stylesheet" href="components.css">
</head>
<body>
<div class="bg-orb bg-orb-1"></div>
<div class="bg-orb bg-orb-2"></div>
'''

# ── shared navbar ──────────────────────────────────────────────────────────────
def navbar(active):
    links = [
        ("index.html",            "fas fa-home",           "الرئيسية"),
        ("services.html",         "fas fa-briefcase",      "الخدمات"),
        ("specializations.html",  "fas fa-graduation-cap", "التخصصات"),
        ("study.html",            "fas fa-book-open",      "الدراسة"),
        ("past-assignments.html", "fas fa-folder-open",    "مهمات سابقة"),
        ("faq.html",              "fas fa-question-circle","الأسئلة"),
        ("contact.html",          "fas fa-envelope",       "تواصل"),
    ]
    li = "\n".join(
        f'      <li><a href="{h}" class="nav-link{"  active" if h==active else ""}"><i class="{i}"></i> {l}</a></li>'
        for h,i,l in links
    )
    mob = "\n".join(
        f'    <li><a href="{h}" class="nav-link{"  active" if h==active else ""}"><i class="{i}"></i> {l}</a></li>'
        for h,i,l in links
    )
    return f'''<nav class="navbar navbar-blur" id="navbar">
  <div class="navbar-inner">
    <a href="index.html" class="navbar-logo">
      <div class="logo-icon">B</div>
      <div class="logo-text"><span>BTEC</span> HUB<span class="logo-sub">Educational Platform</span></div>
    </a>
    <ul class="navbar-nav">
{li}
    </ul>
    <div class="navbar-actions">
      <button class="lang-toggle" id="langToggleBtn">&#127760; <span id="langText">EN</span></button>
      <button class="theme-toggle" id="themeToggleBtn"><i id="themeIcon" class="fas fa-sun"></i></button>
      <button class="cart-nav-btn" id="cartNavBtn"><i class="fas fa-shopping-cart"></i><span class="cart-badge" style="display:none">0</span></button>
      <button class="menu-toggle" id="menuToggle"><i class="fas fa-bars"></i></button>
    </div>
  </div>
</nav>
<div class="mobile-nav" id="mobileNav">
  <ul class="mobile-nav-links">
{mob}
  </ul>
  <div class="mobile-nav-actions">
    <button class="lang-toggle" id="mobileLangBtn">&#127760; <span id="mobileLangText">EN</span></button>
    <button class="theme-toggle" id="mobileThemeBtn"><i id="mobileThemeIcon" class="fas fa-sun"></i></button>
  </div>
</div>
<div class="cart-overlay" id="mobileNavOverlay"></div>
'''

# ── shared footer ──────────────────────────────────────────────────────────────
FOOTER = '''<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="footer-logo">
          <div class="logo-icon">B</div>
          <div class="logo-text"><span>BTEC</span> HUB</div>
        </a>
        <p class="footer-desc">منصة متكاملة لخدمات الدعم الأكاديمي والموارد التعليمية لطلاب BTEC. مدعومة بالذكاء الاصطناعي.</p>
        <div class="footer-social">
          <a href="https://wa.me/962786003597" class="social-btn" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
          <a href="#" class="social-btn" title="Instagram"><i class="fab fa-instagram"></i></a>
          <a href="#" class="social-btn" title="Twitter"><i class="fab fa-twitter"></i></a>
        </div>
      </div>
      <div class="footer-col">
        <h4>الخدمات</h4>
        <ul class="footer-links">
          <li><a href="services.html">تدقيق الواجبات</a></li>
          <li><a href="services.html">إعداد التقارير</a></li>
          <li><a href="services.html">الشرح والتوجيه</a></li>
          <li><a href="services.html">مراجعة المشاريع</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>التخصصات</h4>
        <ul class="footer-links">
          <li><a href="specializations.html#business">Business</a></li>
          <li><a href="specializations.html#it">IT</a></li>
          <li><a href="specializations.html#health">Health &amp; Social Care</a></li>
          <li><a href="specializations.html#engineering">Engineering</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>المنصة</h4>
        <ul class="footer-links">
          <li><a href="study.html">مواد الدراسة</a></li>
          <li><a href="past-assignments.html">مهمات سابقة</a></li>
          <li><a href="faq.html">الأسئلة الشائعة</a></li>
          <li><a href="contact.html">تواصل معنا</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="footer-copy">
        &copy; 2026 BTEC HUB. جميع الحقوق محفوظة.
        <br><span style="font-size:0.85em;opacity:0.85;margin-top:4px;display:inline-block;">
          تم التطوير بواسطة <strong style="color:var(--primary-light);">ورد البصول</strong>
        </span>
      </p>
      <div class="footer-bottom-links">
        <a href="#">سياسة الخصوصية</a>
        <a href="#">شروط الاستخدام</a>
        <a href="#">الدعم الأكاديمي</a>
      </div>
    </div>
  </div>
</footer>
'''

# ── shared widgets (cart, assistant, whatsapp, scroll-top, scripts) ────────────
WIDGETS = '''
<!-- Cart Sidebar -->
<div class="cart-overlay" id="cartOverlay"></div>
<aside class="cart-sidebar" id="cartSidebar">
  <div class="cart-header">
    <div class="cart-title"><i class="fas fa-shopping-cart"></i> <span>السلة</span></div>
    <button class="cart-close" id="cartClose"><i class="fas fa-times"></i></button>
  </div>
  <div class="cart-body" id="cartBody"></div>
  <div class="cart-footer" id="cartFooter" style="display:none;"></div>
</aside>

<!-- BTEC AI Assistant -->
<div class="assistant-fab" id="assistantFab">
  <button class="assistant-fab-btn" title="BTEC Assistant"><i class="fas fa-robot"></i></button>
  <div class="assistant-tooltip">BTEC Assistant</div>
</div>
<div class="assistant-window" id="assistantWindow">
  <div class="assistant-header">
    <div class="assistant-avatar">&#129302;</div>
    <div class="assistant-info">
      <div class="assistant-name">BTEC Assistant</div>
      <div class="assistant-status"><span class="status-dot"></span> متاح الآن</div>
    </div>
    <button class="assistant-minimize" id="assistantMinimize"><i class="fas fa-minus"></i></button>
  </div>
  <div class="assistant-messages" id="assistantMessages"></div>
  <div class="quick-replies" id="quickReplies"></div>
  <div class="assistant-input-area">
    <input type="text" class="assistant-input" id="assistantInput" placeholder="اكتب سؤالك هنا...">
    <button class="assistant-send" id="assistantSend"><i class="fas fa-paper-plane"></i></button>
  </div>
</div>

<!-- WhatsApp FAB -->
<div class="whatsapp-fab">
  <div class="whatsapp-tooltip">تواصل معنا</div>
  <a href="https://wa.me/962786003597" target="_blank" class="whatsapp-fab-btn" title="WhatsApp">
    <i class="fab fa-whatsapp"></i>
  </a>
</div>

<!-- Scroll to top -->
<button class="scroll-top" id="scrollTopBtn" title="للأعلى"><i class="fas fa-chevron-up"></i></button>

<script src="main.js"></script>
<script src="cart.js"></script>
<script src="assistant.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('langToggleBtn')?.addEventListener('click', () => window.BtecMain?.toggleLanguage());
    document.getElementById('themeToggleBtn')?.addEventListener('click', () => window.BtecMain?.toggleTheme());
    document.getElementById('mobileLangBtn')?.addEventListener('click', () => window.BtecMain?.toggleLanguage());
    document.getElementById('mobileThemeBtn')?.addEventListener('click', () => window.BtecMain?.toggleTheme());
  });
</script>
'''

def write(filename, body, extra_script=''):
    content = (
        head({'index.html':'BTEC HUB – الصفحة الرئيسية',
              'services.html':'BTEC HUB – الخدمات',
              'specializations.html':'BTEC HUB – التخصصات',
              'study.html':'BTEC HUB – مواد الدراسة',
              'past-assignments.html':'BTEC HUB – المهمات السابقة',
              'faq.html':'BTEC HUB – الأسئلة الشائعة',
              'contact.html':'BTEC HUB – تواصل معنا'}[filename])
        + navbar(filename)
        + body
        + FOOTER
        + WIDGETS
        + (extra_script if extra_script else '')
        + '\n</body>\n</html>'
    )
    path = os.path.join(OUT, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    open('rebuild_log.txt','a',encoding='utf-8').write(f'OK: ' + filename + chr(10))


# ═══════════════════════════════════════════════════════════════════════════════
# INDEX
# ═══════════════════════════════════════════════════════════════════════════════
index_body = '''
<main>
  <!-- ── HERO ── -->
  <section class="hero">
    <div class="hero-particles" id="particles"></div>
    <div class="container">
      <div class="hero-content">
        <!-- Text -->
        <div class="hero-text reveal">
          <div class="section-badge mb-lg">
            <i class="fas fa-star"></i>&nbsp; منصة رقم 1 لطلاب BTEC
          </div>
          <h1 class="hero-title">
            ارتقِ بمستواك<br>
            الأكاديمي مع<br>
            <span class="glow-text">BTEC HUB</span>
          </h1>
          <p class="hero-desc">
            منصتك المتكاملة لخدمات الدعم الأكاديمي، الموارد التعليمية،
            ومساعد الذكاء الاصطناعي المخصص لطلاب BTEC.
          </p>
          <div class="hero-actions">
            <a href="services.html" class="btn btn-primary btn-lg">
              <i class="fas fa-rocket"></i> استعرض الخدمات
            </a>
            <a href="contact.html" class="btn btn-secondary btn-lg">
              <i class="fab fa-whatsapp"></i> تواصل معنا
            </a>
          </div>
          <div class="hero-stats">
            <div><span class="hero-stat-num">50+</span><span class="hero-stat-label">خدمة متاحة</span></div>
            <div class="sep"></div>
            <div><span class="hero-stat-num">4</span><span class="hero-stat-label">تخصصات</span></div>
            <div class="sep"></div>
            <div><span class="hero-stat-num">24/7</span><span class="hero-stat-label">دعم AI</span></div>
            <div class="sep"></div>
            <div><span class="hero-stat-num">100%</span><span class="hero-stat-label">دعم أكاديمي</span></div>
          </div>
        </div>
        <!-- Visual -->
        <div class="hero-visual reveal">
          <div class="hero-card-main">
            <div class="hero-card-floating hero-card-1">
              <div class="service-icon purple"><i class="fas fa-file-alt"></i></div>
              <div>
                <div style="font-weight:700;font-size:.9rem;">تدقيق الواجبات</div>
                <div style="font-size:.75rem;color:var(--text-muted);">Unit 6 – Business</div>
              </div>
            </div>
            <div class="hero-card-floating hero-card-2">
              <div class="service-icon green"><i class="fas fa-check-circle"></i></div>
              <div>
                <div style="font-weight:700;font-size:.9rem;">مراجعة معتمدة</div>
                <div style="font-size:.75rem;color:var(--text-muted);">وفق معايير BTEC</div>
              </div>
            </div>
            <div class="hero-card-floating hero-card-3">
              <div class="service-icon blue"><i class="fas fa-robot"></i></div>
              <div>
                <div style="font-weight:700;font-size:.9rem;">BTEC Assistant</div>
                <div style="font-size:.75rem;color:var(--text-muted);">متاح 24/7</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── FEATURES ── -->
  <section class="section">
    <div class="container">
      <div class="section-header reveal">
        <div class="section-badge"><i class="fas fa-sparkles"></i> لماذا BTEC HUB؟</div>
        <h2 class="section-title">كل ما تحتاجه في مكان واحد</h2>
        <p class="section-subtitle">نقدم لك تجربة دعم أكاديمي متكاملة تساعدك على التميز في مسيرتك مع BTEC</p>
      </div>
      <div class="features-grid">
        <div class="feature-card reveal">
          <div class="feature-icon-wrap purple"><i class="fas fa-file-signature"></i></div>
          <h3 class="feature-title">تدقيق الواجبات</h3>
          <p class="feature-desc">مراجعة واجباتك وفق معايير BTEC الرسمية مع ملاحظات تفصيلية لتحسين درجاتك.</p>
        </div>
        <div class="feature-card reveal">
          <div class="feature-icon-wrap blue"><i class="fas fa-chart-line"></i></div>
          <h3 class="feature-title">إعداد التقارير</h3>
          <p class="feature-desc">مساعدة متخصصة في بناء وتنسيق تقاريرك الأكاديمية بالشكل الصحيح.</p>
        </div>
        <div class="feature-card reveal">
          <div class="feature-icon-wrap green"><i class="fas fa-chalkboard-teacher"></i></div>
          <h3 class="feature-title">الشرح والتوجيه</h3>
          <p class="feature-desc">جلسات شرح فردية لمساعدتك على فهم أي وحدة تجد صعوبة فيها.</p>
        </div>
        <div class="feature-card reveal">
          <div class="feature-icon-wrap amber"><i class="fas fa-robot"></i></div>
          <h3 class="feature-title">BTEC AI Assistant</h3>
          <p class="feature-desc">مساعد ذكاء اصطناعي متخصص يجيب على أسئلتك ويوجهك على مدار الساعة.</p>
        </div>
        <div class="feature-card reveal">
          <div class="feature-icon-wrap purple"><i class="fas fa-book-open"></i></div>
          <h3 class="feature-title">مواد الدراسة</h3>
          <p class="feature-desc">ملخصات وشروحات شاملة لجميع وحدات تخصصك لتسهيل مراجعتك.</p>
        </div>
        <div class="feature-card reveal">
          <div class="feature-icon-wrap blue"><i class="fas fa-shopping-cart"></i></div>
          <h3 class="feature-title">طلب سريع عبر واتساب</h3>
          <p class="feature-desc">أضف خدماتك للسلة وأرسل طلبك بنقرة واحدة مباشرة عبر واتساب.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── PROCESS ── -->
  <section class="section" style="background:var(--bg-secondary);">
    <div class="container">
      <div class="section-header reveal">
        <div class="section-badge"><i class="fas fa-list-ol"></i> كيف نعمل؟</div>
        <h2 class="section-title">من الطلب إلى التسليم في 4 خطوات</h2>
      </div>
      <div class="grid-4 reveal" style="gap:1.5rem;margin-top:3rem;">
        <div class="card" style="text-align:center;padding:2rem 1.5rem;">
          <div style="width:3rem;height:3rem;background:var(--primary-gradient);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;font-weight:800;font-size:1.25rem;">1</div>
          <h4 style="margin-bottom:.5rem;">اختر خدمتك</h4>
          <p style="font-size:.875rem;color:var(--text-secondary);">تصفح قائمة خدماتنا وأضف ما تحتاجه للسلة</p>
        </div>
        <div class="card" style="text-align:center;padding:2rem 1.5rem;">
          <div style="width:3rem;height:3rem;background:var(--primary-gradient);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;font-weight:800;font-size:1.25rem;">2</div>
          <h4 style="margin-bottom:.5rem;">أرسل طلبك</h4>
          <p style="font-size:.875rem;color:var(--text-secondary);">اضغط "إرسال عبر واتساب" لإرسال تفاصيل طلبك</p>
        </div>
        <div class="card" style="text-align:center;padding:2rem 1.5rem;">
          <div style="width:3rem;height:3rem;background:var(--primary-gradient);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;font-weight:800;font-size:1.25rem;">3</div>
          <h4 style="margin-bottom:.5rem;">تأكيد السعر</h4>
          <p style="font-size:.875rem;color:var(--text-secondary);">يتواصل معك فريقنا لتحديد السعر وتأكيد الطلب</p>
        </div>
        <div class="card" style="text-align:center;padding:2rem 1.5rem;">
          <div style="width:3rem;height:3rem;background:var(--primary-gradient);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 1rem;font-weight:800;font-size:1.25rem;">4</div>
          <h4 style="margin-bottom:.5rem;">التسليم</h4>
          <p style="font-size:.875rem;color:var(--text-secondary);">استلم خدمتك في الموعد بجودة أكاديمية عالية</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── SPECIALIZATIONS PREVIEW ── -->
  <section class="section">
    <div class="container">
      <div class="section-header reveal">
        <div class="section-badge"><i class="fas fa-graduation-cap"></i> تخصصاتنا</div>
        <h2 class="section-title">نغطي جميع تخصصات BTEC</h2>
        <p class="section-subtitle">فريقنا المتخصص جاهز لمساعدتك في أي وحدة من تخصصك</p>
      </div>
      <div class="grid-4" style="gap:1.5rem;margin-top:3rem;">
        <a href="specializations.html#business" class="spec-card reveal">
          <div class="spec-card-cover gradient-purple"><span class="spec-emoji">&#128188;</span></div>
          <div class="spec-card-body">
            <h3 class="spec-name">Business</h3>
            <p class="spec-desc">إدارة الأعمال، التسويق، المحاسبة، الموارد البشرية</p>
            <div class="spec-units">10+ وحدة</div>
          </div>
        </a>
        <a href="specializations.html#it" class="spec-card reveal">
          <div class="spec-card-cover gradient-blue"><span class="spec-emoji">&#128187;</span></div>
          <div class="spec-card-body">
            <h3 class="spec-name">IT</h3>
            <p class="spec-desc">البرمجة، الشبكات، قواعد البيانات، أمن المعلومات</p>
            <div class="spec-units">10+ وحدة</div>
          </div>
        </a>
        <a href="specializations.html#health" class="spec-card reveal">
          <div class="spec-card-cover gradient-green"><span class="spec-emoji">&#127973;</span></div>
          <div class="spec-card-body">
            <h3 class="spec-name">Health &amp; Social Care</h3>
            <p class="spec-desc">الرعاية الصحية، علم النفس، التمريض</p>
            <div class="spec-units">8+ وحدة</div>
          </div>
        </a>
        <a href="specializations.html#engineering" class="spec-card reveal">
          <div class="spec-card-cover gradient-amber"><span class="spec-emoji">&#9881;&#65039;</span></div>
          <div class="spec-card-body">
            <h3 class="spec-name">Engineering</h3>
            <p class="spec-desc">الهندسة الميكانيكية، الكهربائية، الرسم الهندسي</p>
            <div class="spec-units">8+ وحدة</div>
          </div>
        </a>
      </div>
    </div>
  </section>

  <!-- ── STATS ── -->
  <section class="section" style="background:var(--bg-secondary);">
    <div class="container">
      <div class="grid-4 reveal" style="gap:1.5rem;">
        <div class="stat-card"><span class="stat-number">500+</span><span class="stat-label">طالب مستفيد</span></div>
        <div class="stat-card"><span class="stat-number">50+</span><span class="stat-label">خدمة متاحة</span></div>
        <div class="stat-card"><span class="stat-number">4</span><span class="stat-label">تخصصات مغطاة</span></div>
        <div class="stat-card"><span class="stat-number">98%</span><span class="stat-label">نسبة رضا الطلاب</span></div>
      </div>
    </div>
  </section>

  <!-- ── TESTIMONIALS ── -->
  <section class="section">
    <div class="container">
      <div class="section-header reveal">
        <div class="section-badge"><i class="fas fa-star"></i> آراء الطلاب</div>
        <h2 class="section-title">ماذا يقولون عنا؟</h2>
      </div>
      <div class="grid-3" style="gap:1.5rem;margin-top:3rem;">
        <div class="testimonial-card reveal">
          <div class="stars">&#11088;&#11088;&#11088;&#11088;&#11088;</div>
          <p class="testimonial-text">"ساعدني BTEC HUB كثيراً في فهم متطلبات الوحدات وتحسين مستواي الأكاديمي بشكل ملحوظ."</p>
          <div class="testimonial-author">
            <div class="author-avatar">أ</div>
            <div><div class="author-name">أحمد م.</div><div class="author-role">Business – Level 3</div></div>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="stars">&#11088;&#11088;&#11088;&#11088;&#11088;</div>
          <p class="testimonial-text">"المساعد الذكي BTEC Assistant رائع جداً، يجيب على أسئلتي بسرعة ودقة في أي وقت."</p>
          <div class="testimonial-author">
            <div class="author-avatar">س</div>
            <div><div class="author-name">سارة ع.</div><div class="author-role">IT – Level 3</div></div>
          </div>
        </div>
        <div class="testimonial-card reveal">
          <div class="stars">&#11088;&#11088;&#11088;&#11088;&#11088;</div>
          <p class="testimonial-text">"خدمة تدقيق الواجبات ممتازة! الملاحظات كانت واضحة ومفيدة جداً وساعدتني على تحسين درجتي."</p>
          <div class="testimonial-author">
            <div class="author-avatar">م</div>
            <div><div class="author-name">محمد خ.</div><div class="author-role">Health &amp; Social Care – Level 2</div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── CTA ── -->
  <section class="section">
    <div class="container">
      <div class="cta-section reveal">
        <div class="cta-content">
          <h2>جاهز للبدء؟</h2>
          <p>انضم لمئات الطلاب الذين يثقون بـ BTEC HUB لتحقيق أهدافهم الأكاديمية</p>
          <div class="cta-actions">
            <a href="services.html" class="btn-cta-white"><i class="fas fa-rocket"></i> استعرض الخدمات</a>
            <a href="https://wa.me/962786003597" target="_blank" class="btn-cta-outline"><i class="fab fa-whatsapp"></i> تواصل الآن</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
'''
write('index.html', index_body)

# ═══════════════════════════════════════════════════════════════════════════════
# SERVICES
# ═══════════════════════════════════════════════════════════════════════════════

def service_card(cat, icon_cls, icon_color, name, desc, features, cart_id, cart_name, unit, emoji, badge1, badge1_cls, badge2='', badge2_cls=''):
    feats = ''.join(f'<li>{f}</li>' for f in features)
    b2 = f'<span class="badge {badge2_cls}">{badge2}</span>' if badge2 else ''
    return f'''        <div class="service-card reveal" data-category="{cat}">
          <div class="service-card-header">
            <div class="service-icon {icon_color}"><i class="{icon_cls}"></i></div>
            <div class="service-tags">
              <span class="badge {badge1_cls}">{badge1}</span>{b2}
            </div>
          </div>
          <div class="service-card-body">
            <h3 class="service-name">{name}</h3>
            <p class="service-desc">{desc}</p>
            <ul class="service-features">{feats}</ul>
          </div>
          <div class="service-card-footer">
            <div class="service-price">
              <span class="price-contact"><i class="fab fa-whatsapp"></i> تواصل للسعر</span>
              <span class="price-note">يُحدَّد حسب حجم العمل</span>
            </div>
            <div class="service-card-actions">
              <button class="btn btn-sm btn-primary"
                data-add-to-cart="{cart_id}"
                data-name="{cart_name}"
                data-price="contact"
                data-unit="{unit}"
                data-icon="{emoji}">
                <i class="fas fa-cart-plus"></i> أضف للسلة
              </button>
            </div>
          </div>
        </div>
'''

services_body = '''
<main>
  <div class="page-hero">
    <div class="container page-hero-content">
      <div class="section-badge mb-lg"><i class="fas fa-briefcase"></i> خدماتنا</div>
      <h1>خدماتنا الأكاديمية</h1>
      <p>اختر الخدمة المناسبة لاحتياجك وأضفها للسلة لإرسالها مباشرة عبر واتساب</p>
    </div>
  </div>

  <section class="section">
    <div class="container">

      <!-- Filter & Search -->
      <div class="filter-bar reveal" style="justify-content:space-between;flex-wrap:wrap;gap:1rem;">
        <div style="display:flex;gap:.5rem;flex-wrap:wrap;">
          <button class="filter-btn active" data-filter="all">&#128293; الكل</button>
          <button class="filter-btn" data-filter="business">&#128188; Business</button>
          <button class="filter-btn" data-filter="it">&#128187; IT</button>
          <button class="filter-btn" data-filter="health">&#127973; Health</button>
          <button class="filter-btn" data-filter="engineering">&#9881; Engineering</button>
        </div>
        <div class="search-box">
          <i class="fas fa-search search-icon"></i>
          <input type="text" id="serviceSearch" placeholder="ابحث عن خدمة...">
        </div>
      </div>

      <!-- Info Banner -->
      <div class="reveal" style="background:linear-gradient(135deg,rgba(108,63,197,.12),rgba(14,165,233,.08));border:1px solid rgba(108,63,197,.25);border-radius:var(--radius-xl);padding:1.25rem 1.75rem;display:flex;align-items:center;gap:1.25rem;margin-bottom:2rem;backdrop-filter:blur(10px);">
        <span style="font-size:1.75rem;">&#8505;&#65039;</span>
        <p style="font-size:.875rem;color:var(--text-secondary);line-height:1.7;margin:0;">
          <strong style="color:var(--primary-light)">تنبيه:</strong>
          الأسعار النهائية تُحدَّد عبر التواصل المباشر بعد إرسال السلة.
          أضف الخدمات التي تريدها ثم أرسل طلبك عبر واتساب.
        </p>
      </div>

      <!-- Services Grid -->
      <div class="services-grid" id="servicesGrid">
'''
services_body += service_card('business','fas fa-file-alt','purple','تدقيق واجب Unit 6','مراجعة احترافية لواجب Unit 6 مع ملاحظات تفصيلية وفق معايير BTEC الرسمية.',['مراجعة وفق معايير BTEC','ملاحظات واضحة على كل نقطة','نقاط القوة والضعف'],'biz-u6-review','تدقيق واجب Unit 6 – Business','Business – Unit 6','📝','Business','badge-primary','Unit 6','badge-blue')
services_body += service_card('business','fas fa-chart-bar','blue','Business Plan Report','مساعدة في صياغة وتنظيم تقرير خطة العمل لـ Unit 2 وفق المتطلبات الأكاديمية.',['هيكل التقرير الصحيح','مراجعة المحتوى والتحليل','ملاحظات على التنسيق والعرض'],'biz-u2-plan','Business Plan Report – Unit 2','Business – Unit 2','📊','Business','badge-primary','Unit 2','badge-blue')
services_body += service_card('business','fas fa-bullhorn','green','Marketing Campaign Review','مراجعة مشروع حملة التسويق مع تقييم المزيج التسويقي 4Ps.',['تقييم استراتيجية التسويق','مراجعة المزيج التسويقي 4Ps','اقتراحات للتحسين'],'biz-u3-mkt','Marketing Campaign Review – Unit 3','Business – Unit 3','📣','Business','badge-primary','Unit 3','badge-blue')
services_body += service_card('business','fas fa-users','amber','HR Management Assignment','مراجعة واجب إدارة الموارد البشرية لـ Unit 4.',['تقييم تحليل HR','مراجعة السياسات والإجراءات','ملاحظات أكاديمية دقيقة'],'biz-u4-hr','HR Management Assignment – Unit 4','Business – Unit 4','👥','Business','badge-primary','Unit 4','badge-blue')
services_body += service_card('it','fas fa-network-wired','purple','Networking Project Review','مراجعة مشروع الشبكات مع تقييم التصميم والتوثيق.',['تقييم تصميم الشبكة','مراجعة البروتوكولات والأمان','ملاحظات على التوثيق'],'it-u3-net','Networking Project Review – Unit 3','IT – Unit 3','🌐','IT','badge-blue','Unit 3','badge-green')
services_body += service_card('it','fas fa-database','blue','Database Design Review','مراجعة تصميم قواعد البيانات مع تقييم ERD والـ Normalization.',['مراجعة مخطط ERD','تقييم التطبيع Normalization','ملاحظات على استعلامات SQL'],'it-u5-db','Database Design Review – Unit 5','IT – Unit 5','🗃️','IT','badge-blue','Unit 5','badge-green')
services_body += service_card('health','fas fa-heartbeat','green','Health &amp; Social Care – Unit 1','مراجعة واجب Unit 1 مع ملاحظات تفصيلية.',['تقييم تحليل مراحل التطور','مراجعة النظريات المستخدمة','ملاحظات أكاديمية متخصصة'],'health-u1','Health – Unit 1 Review','Health – Unit 1','🏥','Health','badge-green','Unit 1','badge-amber')
services_body += service_card('engineering','fas fa-cogs','amber','Engineering Drawing Review','مراجعة رسومات هندسية مع تقييم متخصص.',['مراجعة المخططات والتصاميم','تقييم الحسابات الهندسية','ملاحظات على التوثيق'],'eng-u2-draw','Engineering Drawing Review – Unit 2','Engineering – Unit 2','⚙️','Engineering','badge-amber','Unit 2','badge-primary')
services_body += service_card('business','fas fa-chalkboard-teacher','purple','جلسة شرح فردية','جلسة شرح فردية لأي وحدة تحتاج فهمها بعمق.',['شرح مخصص لاحتياجك','أمثلة عملية وتطبيقات','إجابة على جميع أسئلتك'],'tutoring','جلسة شرح فردية','خدمة عامة','🎯','عام','badge-primary','متاح','badge-green')
services_body += service_card('business','fas fa-file-signature','blue','مراجعة قبل التسليم','فحص شامل للمشروع قبل التسليم النهائي.',['فحص استيفاء المعايير','مراجعة التنسيق والمراجع','تقرير جاهزية التسليم'],'pre-submit','مراجعة قبل التسليم','خدمة عامة','✅','عام','badge-primary','متاح','badge-green')

services_body += '''      </div><!-- /services-grid -->

      <!-- CTA -->
      <div class="cta-section reveal" style="margin-top:4rem;">
        <div class="cta-content">
          <h2>خدمتك غير موجودة؟</h2>
          <p>تواصل معنا مباشرة وسنساعدك في تحديد الخدمة المناسبة لاحتياجك</p>
          <div class="cta-actions">
            <a href="https://wa.me/962786003597" target="_blank" class="btn-cta-white">
              <i class="fab fa-whatsapp"></i> تواصل عبر واتساب
            </a>
          </div>
        </div>
      </div>

    </div>
  </section>
</main>
'''

services_script = '''
<script>
document.addEventListener('DOMContentLoaded', () => {
  // Filter
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.getAttribute('data-filter');
      document.querySelectorAll('.service-card').forEach(card => {
        card.style.display = (f === 'all' || card.getAttribute('data-category') === f) ? '' : 'none';
      });
    });
  });
  // Search
  document.getElementById('serviceSearch')?.addEventListener('input', function() {
    const q = this.value.toLowerCase();
    document.querySelectorAll('.service-card').forEach(card => {
      card.style.display = card.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
  });
});
</script>
'''
write('services.html', services_body, services_script)


# ═══════════════════════════════════════════════════════════════════════════════
# SPECIALIZATIONS
# ═══════════════════════════════════════════════════════════════════════════════

def spec_section(anchor, emoji, grad, name, desc, units, btn_color):
    unit_chips = ''.join(
        f'<span style="display:inline-flex;align-items:center;gap:.4rem;padding:.4rem .8rem;background:var(--bg-tertiary);border:1px solid var(--border-color);border-radius:var(--radius-md);font-size:.78rem;font-weight:600;color:var(--text-secondary);margin:.25rem;">'
        f'<i class="fas fa-circle" style="font-size:.5rem;opacity:.5;"></i>{u}</span>'
        for u in units
    )
    return f'''
      <div id="{anchor}" class="card reveal" style="overflow:hidden;margin-bottom:2rem;padding:0;">
        <div style="height:200px;background:{grad};display:flex;align-items:center;justify-content:center;font-size:5rem;position:relative;">
          <span style="filter:drop-shadow(0 8px 20px rgba(0,0,0,.4));position:relative;z-index:1;">{emoji}</span>
        </div>
        <div style="padding:2rem;">
          <h2 style="font-size:1.5rem;font-weight:800;margin-bottom:.5rem;">{name}</h2>
          <p style="color:var(--text-secondary);line-height:1.7;margin-bottom:1.5rem;">{desc}</p>
          <div style="margin-bottom:1.5rem;">{unit_chips}</div>
          <div style="display:flex;gap:1rem;flex-wrap:wrap;align-items:center;">
            <a href="services.html" class="btn btn-primary" style="background:{btn_color};">
              <i class="fas fa-briefcase"></i> عرض خدمات هذا التخصص
            </a>
            <a href="study.html" class="btn btn-secondary"><i class="fas fa-book-open"></i> مواد الدراسة</a>
          </div>
        </div>
      </div>
'''

spec_body = '''
<main>
  <div class="page-hero">
    <div class="container page-hero-content">
      <div class="section-badge mb-lg"><i class="fas fa-graduation-cap"></i> التخصصات</div>
      <h1>تخصصات BTEC</h1>
      <p>نغطي جميع التخصصات الرئيسية لبرامج BTEC بخدمات متخصصة لكل وحدة</p>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="grid-4 reveal" style="margin-bottom:3rem;gap:1.5rem;">
        <div class="stat-card"><span class="stat-number">4</span><span class="stat-label">تخصصات</span></div>
        <div class="stat-card"><span class="stat-number">30+</span><span class="stat-label">وحدة مغطاة</span></div>
        <div class="stat-card"><span class="stat-number">3</span><span class="stat-label">مستويات</span></div>
        <div class="stat-card"><span class="stat-number">50+</span><span class="stat-label">خدمة متاحة</span></div>
      </div>
'''
spec_body += spec_section(
    'business','💼','linear-gradient(135deg,#4C1D95,#1E40AF)',
    'Business – إدارة الأعمال',
    'تخصص شامل يغطي مجالات إدارة الأعمال والتسويق والتمويل وإدارة الموارد البشرية. من أكثر التخصصات طلباً في سوق العمل.',
    ['Unit 1 – Business Environment','Unit 2 – Business Resources','Unit 3 – Introduction to Marketing',
     'Unit 4 – Business Communication','Unit 5 – Business Accounting','Unit 6 – Business Decision Making',
     'Unit 7 – Business Strategy','Unit 8 – Human Resources','Unit 9 – Management Accounting','Unit 10 – Business Law'],
    'var(--primary-gradient)'
)
spec_body += spec_section(
    'it','💻','linear-gradient(135deg,#0369A1,#065F46)',
    'Information Technology – تقنية المعلومات',
    'تخصص يشمل البرمجة، الشبكات، أمن المعلومات، قواعد البيانات، وتطوير الأنظمة. مثالي للراغبين في دخول قطاع التقنية.',
    ['Unit 1 – IT Systems','Unit 2 – Technology Systems','Unit 3 – Computer Networks',
     'Unit 4 – Web Design','Unit 5 – Database Design','Unit 6 – Software Design',
     'Unit 7 – IT Systems Security','Unit 8 – Mobile Apps','Unit 9 – Cloud Computing','Unit 10 – Programming'],
    'linear-gradient(135deg,#0EA5E9,#10B981)'
)
spec_body += spec_section(
    'health','🏥','linear-gradient(135deg,#065F46,#92400E)',
    'Health &amp; Social Care – الصحة والرعاية الاجتماعية',
    'تخصص يغطي مجالات الرعاية الصحية، التمريض، الخدمات الاجتماعية، وعلم النفس.',
    ['Unit 1 – Human Lifespan Development','Unit 2 – Values in Health Care','Unit 3 – Health &amp; Safety',
     'Unit 4 – Social Influences','Unit 5 – Anatomy &amp; Physiology','Unit 6 – Public Health',
     'Unit 7 – Sociological Perspectives','Unit 8 – Psychological Perspectives'],
    'linear-gradient(135deg,#10B981,#F59E0B)'
)
spec_body += spec_section(
    'engineering','⚙️','linear-gradient(135deg,#92400E,#7C3AED)',
    'Engineering – الهندسة',
    'تخصص يشمل الهندسة الميكانيكية، الكهربائية، المدنية، وإدارة المشاريع الهندسية.',
    ['Unit 1 – Engineering Principles','Unit 2 – Engineering Drawing','Unit 3 – Mathematics',
     'Unit 4 – Materials &amp; Processes','Unit 5 – Electrical/Electronic','Unit 6 – Mechanical Principles',
     'Unit 7 – Project Management','Unit 8 – Quality Control'],
    'linear-gradient(135deg,#F59E0B,#EF4444)'
)
spec_body += '''
    </div>
  </section>
</main>
'''
write('specializations.html', spec_body)


# ═══════════════════════════════════════════════════════════════════════════════
# STUDY
# ═══════════════════════════════════════════════════════════════════════════════

def study_card(cat, icon_cls, icon_color, title, desc, tag, unit):
    return f'''        <div class="study-card reveal" data-category="{cat}">
          <div class="study-card-icon {icon_color}"><i class="{icon_cls}"></i></div>
          <div class="study-card-content">
            <h3 class="study-card-title">{title}</h3>
            <p class="study-card-desc">{desc}</p>
            <div class="study-card-meta">
              <span class="study-meta-item"><i class="fas fa-tag"></i> {tag}</span>
              <span class="study-meta-item"><i class="fas fa-book"></i> {unit}</span>
            </div>
          </div>
          <div class="study-card-action">
            <button class="btn btn-ghost" onclick="window.BtecMain?.showToast('سيتم توفير المادة قريباً...','info')">
              <i class="fas fa-eye"></i> عرض المادة
            </button>
          </div>
        </div>\n'''

study_body = '''
<main>
  <div class="page-hero">
    <div class="container page-hero-content">
      <div class="section-badge mb-lg"><i class="fas fa-book-open"></i> مواد الدراسة</div>
      <h1>مواد الدراسة والشروحات</h1>
      <p>شروحات مفصلة، ملخصات، وموارد تعليمية لمختلف تخصصات BTEC</p>
    </div>
  </div>
  <section class="section">
    <div class="container">

      <div class="reveal" style="background:rgba(14,165,233,.1);border:1px solid rgba(14,165,233,.3);border-radius:var(--radius-xl);padding:1.25rem 1.75rem;display:flex;align-items:center;gap:1.25rem;margin-bottom:2rem;">
        <span style="font-size:1.75rem;">&#8505;&#65039;</span>
        <p style="font-size:.875rem;color:var(--text-secondary);line-height:1.7;margin:0;">
          <strong style="color:#0EA5E9">ملاحظة:</strong>
          هذه المواد مقدمة لأغراض مرجعية وتعليمية لمساعدتك على فهم متطلبات وحدات BTEC بشكل أفضل.
        </p>
      </div>

      <div class="filter-bar reveal" style="justify-content:space-between;flex-wrap:wrap;gap:1rem;">
        <div style="display:flex;gap:.5rem;flex-wrap:wrap;">
          <button class="filter-btn active" data-filter="all">الكل</button>
          <button class="filter-btn" data-filter="business">Business</button>
          <button class="filter-btn" data-filter="it">IT</button>
          <button class="filter-btn" data-filter="health">Health</button>
          <button class="filter-btn" data-filter="engineering">Engineering</button>
        </div>
        <div class="search-box">
          <i class="fas fa-search search-icon"></i>
          <input type="text" id="studySearch" placeholder="ابحث عن درس...">
        </div>
      </div>

      <div class="grid-2" id="studyGrid">
'''
study_body += study_card('business','fas fa-chart-pie','purple','مقدمة في التسويق (Marketing)','شرح مفصل لعناصر المزيج التسويقي وكيفية إعداد خطة تسويقية مبدئية.','Business','Unit 3')
study_body += study_card('business','fas fa-users','purple','إدارة الموارد البشرية','ملخص لعمليات التوظيف، التدريب، وتقييم الأداء في المؤسسات.','Business','Unit 8')
study_body += study_card('business','fas fa-coins','amber','المحاسبة المالية الأساسية','شرح القوائم المالية والنسب المحاسبية الأساسية المستخدمة في تقييم الأداء.','Business','Unit 5')
study_body += study_card('it','fas fa-network-wired','blue','أساسيات شبكات الحاسب','شرح لبروتوكولات الشبكات، طبقات OSI، ومكونات الشبكة الأساسية.','IT','Unit 3')
study_body += study_card('it','fas fa-database','blue','تصميم قواعد البيانات','شرح عملي لمفاهيم ERD، Normalization، واستعلامات SQL.','IT','Unit 5')
study_body += study_card('it','fas fa-shield-alt','green','أساسيات أمن المعلومات','مقدمة في أنواع التهديدات الإلكترونية وطرق الحماية والتشفير.','IT','Unit 7')
study_body += study_card('health','fas fa-child','green','مراحل نمو الإنسان','ملخص لمراحل التطور الجسدي، العقلي، والاجتماعي للإنسان.','Health','Unit 1')
study_body += study_card('health','fas fa-shield-alt','green','الصحة والسلامة المهنية','إرشادات الصحة والسلامة في بيئات الرعاية الصحية والاجتماعية.','Health','Unit 3')
study_body += study_card('engineering','fas fa-drafting-compass','amber','الرسم الهندسي الأساسي','شرح لأساسيات قراءة وكتابة الرسومات الهندسية والأبعاد.','Engineering','Unit 2')
study_body += study_card('engineering','fas fa-cogs','amber','مبادئ الميكانيكا','مقدمة في القوى، العزوم، وقوانين الحركة وتطبيقاتها الهندسية.','Engineering','Unit 6')

study_body += '''      </div>
    </div>
  </section>
</main>
'''

study_script = '''
<script>
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.getAttribute('data-filter');
      document.querySelectorAll('.study-card').forEach(card => {
        card.style.display = (f==='all' || card.getAttribute('data-category')===f) ? '' : 'none';
      });
    });
  });
  document.getElementById('studySearch')?.addEventListener('input', function() {
    const q = this.value.toLowerCase();
    document.querySelectorAll('.study-card').forEach(card => {
      card.style.display = card.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
  });
});
</script>
'''
write('study.html', study_body, study_script)


# ═══════════════════════════════════════════════════════════════════════════════
# PAST ASSIGNMENTS
# ═══════════════════════════════════════════════════════════════════════════════

def assign_card(cat, title, year, badges, desc):
    bs = ''.join(f'<span class="badge {c}">{t}</span>' for t,c in badges)
    return f'''        <div class="assignment-card reveal" data-category="{cat}">
          <div class="assignment-card-header">
            <h3 class="assignment-title">{title}</h3>
            <span class="badge badge-primary">{year}</span>
          </div>
          <div class="assignment-tags">{bs}</div>
          <p class="assignment-desc">{desc}</p>
          <div class="assignment-warning">
            <i class="fas fa-exclamation-triangle warning-icon"></i>
            <span>للاطلاع والمراجعة فقط – يمنع النسخ</span>
          </div>
          <button class="btn btn-secondary btn-sm" onclick="window.BtecMain?.showToast('جاري التحميل...','info')">
            <i class="fas fa-eye"></i> عرض المهمة
          </button>
        </div>\n'''

pa_body = '''
<main>
  <div class="page-hero">
    <div class="container page-hero-content">
      <div class="section-badge mb-lg"><i class="fas fa-folder-open"></i> المهمات السابقة</div>
      <h1>مهمات نموذجية سابقة</h1>
      <p>اطلع على طرق الحل والتنسيق المعتمدة لتطوير مستواك الأكاديمي</p>
    </div>
  </div>
  <section class="section">
    <div class="container">

      <div class="reveal" style="background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.3);border-radius:var(--radius-xl);padding:1.25rem 1.75rem;display:flex;align-items:center;gap:1.25rem;margin-bottom:2rem;">
        <span style="font-size:1.75rem;">&#9888;&#65039;</span>
        <p style="font-size:.875rem;color:var(--text-secondary);line-height:1.7;margin:0;">
          <strong style="color:#F59E0B">تحذير أكاديمي:</strong>
          هذه المهمات مخصصة للاطلاع والمراجعة وفهم طرق الحل فقط.
          استخدامها كعمل شخصي يعتبر غشاً أكاديمياً (Plagiarism) ويعرضك للحرمان.
        </p>
      </div>

      <div class="filter-bar reveal" style="gap:.5rem;flex-wrap:wrap;">
        <button class="filter-btn active" data-filter="all">الكل</button>
        <button class="filter-btn" data-filter="business">Business</button>
        <button class="filter-btn" data-filter="it">IT</button>
        <button class="filter-btn" data-filter="health">Health</button>
        <button class="filter-btn" data-filter="engineering">Engineering</button>
      </div>

      <div class="grid-2" id="assignGrid">
'''
pa_body += assign_card('business','Business Plan – Marketing Unit 2','2024',
    [('Business','badge-primary'),('Level 3','badge-blue'),('Unit 2','badge-blue')],
    'نموذج لخطة تسويق كاملة تتضمن تحليل SWOT وPESTLE والمزيج التسويقي.')
pa_body += assign_card('business','Financial Analysis Report','2023',
    [('Business','badge-primary'),('Level 3','badge-blue'),('Unit 5','badge-blue')],
    'تحليل مالي لشركتين منافستين بناءً على القوائم المالية وحساب النسب المالية.')
pa_body += assign_card('it','Network Design Proposal','2024',
    [('IT','badge-blue'),('Level 3','badge-green'),('Unit 3','badge-green')],
    'مقترح تصميم شبكة محلية LAN مع مخطط الشبكة وتبرير اختيار المكونات.')
pa_body += assign_card('it','Database Implementation SQL','2023',
    [('IT','badge-blue'),('Level 3','badge-green'),('Unit 5','badge-green')],
    'تصميم قاعدة بيانات لمكتبة يتضمن ERD، Normalization، واستعلامات SQL.')
pa_body += assign_card('health','Lifespan Development Case Study','2024',
    [('Health','badge-green'),('Level 2','badge-amber'),('Unit 1','badge-amber')],
    'دراسة حالة عن تأثير العوامل البيئية والوراثية على النمو في مرحلة الطفولة.')
pa_body += assign_card('health','Health &amp; Safety Report','2023',
    [('Health','badge-green'),('Level 3','badge-amber'),('Unit 3','badge-amber')],
    'تقرير شامل عن معايير الصحة والسلامة في بيئات الرعاية الصحية.')
pa_body += assign_card('engineering','CAD Engineering Drawing','2023',
    [('Engineering','badge-amber'),('Level 3','badge-primary'),('Unit 2','badge-primary')],
    'نموذج لرسومات هندسية ثنائية وثلاثية الأبعاد باستخدام برامج CAD.')
pa_body += assign_card('engineering','Mechanical Principles Report','2024',
    [('Engineering','badge-amber'),('Level 3','badge-primary'),('Unit 6','badge-primary')],
    'تقرير تحليلي يتضمن حسابات القوى والعزوم وتطبيقاتها الهندسية.')

pa_body += '''      </div>
    </div>
  </section>
</main>
'''
pa_script = '''
<script>
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.getAttribute('data-filter');
      document.querySelectorAll('.assignment-card').forEach(card => {
        card.style.display = (f==='all' || card.getAttribute('data-category')===f) ? '' : 'none';
      });
    });
  });
});
</script>
'''
write('past-assignments.html', pa_body, pa_script)


# ═══════════════════════════════════════════════════════════════════════════════
# FAQ
# ═══════════════════════════════════════════════════════════════════════════════

def faq_item(q, a, cat=''):
    cat_attr = f' data-category="{cat}"' if cat else ''
    return f'''        <div class="accordion-item reveal"{cat_attr}>
          <div class="accordion-header">
            <div class="accordion-question">{q}</div>
            <div class="accordion-icon"><i class="fas fa-chevron-down"></i></div>
          </div>
          <div class="accordion-body"><p>{a}</p></div>
        </div>\n'''

faq_body = '''
<main>
  <div class="page-hero">
    <div class="container page-hero-content">
      <div class="section-badge mb-lg"><i class="fas fa-question-circle"></i> الأسئلة الشائعة</div>
      <h1>كيف يمكننا مساعدتك؟</h1>
      <p>تجد هنا إجابات على أكثر الأسئلة شيوعاً حول خدماتنا وكيفية الطلب</p>
    </div>
  </div>
  <section class="section">
    <div class="container">

      <div class="filter-bar reveal" style="justify-content:center;gap:1rem;margin-bottom:3rem;flex-wrap:wrap;">
        <button class="filter-btn active" data-filter="all">الكل</button>
        <button class="filter-btn" data-filter="services">عن الخدمات</button>
        <button class="filter-btn" data-filter="pricing">الأسعار والدفع</button>
        <button class="filter-btn" data-filter="cart">الطلب والسلة</button>
        <button class="filter-btn" data-filter="ai">المساعد الذكي</button>
      </div>

      <div class="accordion-list" style="max-width:800px;margin:0 auto;">
'''
faq_body += faq_item('هل تقومون بكتابة الواجبات نيابة عن الطلاب؟',
    'لا، نحن لا نكتب الواجبات نيابة عن الطلاب. نقدم خدمات تدقيق وتوجيه ودعم أكاديمي لمساعدتك على فهم المعايير وتحسين أدائك بنفسك، وذلك للحفاظ على النزاهة الأكاديمية.',
    'services')
faq_body += faq_item('ماذا تشمل خدمة تدقيق الواجبات؟',
    'تشمل مراجعة المحتوى بناءً على معايير BTEC، تحديد نقاط القوة والضعف، وتقديم ملاحظات تفصيلية حول كيفية تحسين التنسيق والتحليل والمراجع الأكاديمية.',
    'services')
faq_body += faq_item('هل يمكنني طلب جلسة شرح فردية أونلاين؟',
    'نعم، نقدم جلسات شرح فردية وتوجيه أونلاين عبر Zoom أو Google Meet حسب رغبتك لمساعدتك في أي وحدة تواجه صعوبة فيها.',
    'services')
faq_body += faq_item('ما هي التخصصات التي تغطونها؟',
    'نغطي حالياً أربع تخصصات رئيسية: Business, Information Technology, Health & Social Care, Engineering بكافة مستوياتها ووحداتها.',
    'services')
faq_body += faq_item('لماذا لا يوجد سعر ثابت لبعض الخدمات؟',
    'بعض الخدمات تختلف تكلفتها حسب حجم العمل، مستوى الصعوبة، والموعد النهائي للتسليم. لذلك يتم تقييم السعر بدقة بعد رؤية تفاصيل طلبك.',
    'pricing')
faq_body += faq_item('كيف يتم الدفع مقابل الخدمات؟',
    'يتم الدفع عن طريق الحوالات البنكية أو الدفع الإلكتروني عبر روابط آمنة تُرسل لك عبر واتساب بعد الاتفاق على السعر.',
    'pricing')
faq_body += faq_item('هل يمكنني استرداد المبلغ إذا لم أستفد؟',
    'نضمن جودة العمل. في حال وجود تقصير من طرفنا، نقوم بإجراء التعديلات المطلوبة مجاناً، أو يمكن استرجاع المبلغ وفق سياسة الاسترجاع.',
    'pricing')
faq_body += faq_item('كيف أتمم الطلب من خلال السلة؟',
    'أضف الخدمات التي تحتاجها إلى السلة، افتح السلة، واضغط "إرسال عبر واتساب". سيقوم النظام بتوليد رسالة جاهزة بكل خدماتك ترسلها بنقرة واحدة.',
    'cart')
faq_body += faq_item('كم يستغرق الرد بعد إرسال الطلب؟',
    'عادةً نرد خلال ساعتين في أوقات العمل (9 ص - 10 م). الطلبات المُرسلة في وقت متأخر يُرد عليها صباح اليوم التالي.',
    'cart')
faq_body += faq_item('هل إضافة الخدمة للسلة تسجيل نهائي للطلب؟',
    'لا، السلة مجرد وسيلة لتنظيم طلبك. الطلب لا يُؤكد إلا بعد التواصل عبر واتساب وتحديد السعر وإتمام الدفع.',
    'cart')
faq_body += faq_item('ما هو BTEC Assistant وهل يمكنه حل الواجبات؟',
    'BTEC Assistant أداة لمساعدتك في تصفح الموقع وفهم الخدمات. هو مُبرمج خصيصاً لرفض حل الواجبات للحفاظ على النزاهة الأكاديمية، لكنه يساعدك في الفهم والتوجيه.',
    'ai')
faq_body += faq_item('هل المساعد الذكي يدعم اللغتين العربية والإنجليزية؟',
    'نعم، يمكنك التحدث مع المساعد بالعربية أو الإنجليزية وسيرد بناءً على لغة واجهة الموقع المختارة.',
    'ai')

faq_body += '''      </div>

      <!-- CTA -->
      <div class="cta-section reveal" style="margin-top:4rem;">
        <div class="cta-content">
          <h2>لم تجد إجابتك؟</h2>
          <p>تواصل معنا مباشرة وسنرد عليك في أسرع وقت ممكن</p>
          <div class="cta-actions">
            <a href="https://wa.me/962786003597" target="_blank" class="btn-cta-white">
              <i class="fab fa-whatsapp"></i> تواصل عبر واتساب
            </a>
            <a href="contact.html" class="btn-cta-outline">
              <i class="fas fa-envelope"></i> راسلنا
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
'''
faq_script = '''
<script>
document.addEventListener('DOMContentLoaded', () => {
  window.BtecMain?.initAccordion();
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.getAttribute('data-filter');
      document.querySelectorAll('.accordion-item').forEach(item => {
        item.style.display = (f==='all' || item.getAttribute('data-category')===f) ? '' : 'none';
      });
    });
  });
});
</script>
'''
write('faq.html', faq_body, faq_script)


# ═══════════════════════════════════════════════════════════════════════════════
# CONTACT
# ═══════════════════════════════════════════════════════════════════════════════

contact_body = '''
<main>
  <div class="page-hero">
    <div class="container page-hero-content">
      <div class="section-badge mb-lg"><i class="fas fa-envelope"></i> اتصل بنا</div>
      <h1>تواصل معنا</h1>
      <p>فريقنا جاهز للرد على استفساراتك وتقديم الدعم الأكاديمي</p>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="contact-grid">

        <!-- Info Card -->
        <div class="contact-info-card reveal">
          <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:1.5rem;">معلومات التواصل</h3>

          <a href="https://wa.me/962786003597" target="_blank" class="contact-method">
            <div class="contact-method-icon" style="background:rgba(37,211,102,.15);color:#25D366;">
              <i class="fab fa-whatsapp"></i>
            </div>
            <div>
              <span class="contact-method-label">واتساب الدعم الفني</span>
              <span class="contact-method-value">+962 78 600 3597</span>
            </div>
          </a>

          <div class="contact-method" style="cursor:default;">
            <div class="contact-method-icon" style="background:rgba(108,63,197,.15);color:var(--primary-light);">
              <i class="fas fa-clock"></i>
            </div>
            <div>
              <span class="contact-method-label">ساعات العمل</span>
              <span class="contact-method-value">9:00 ص – 10:00 م (يومياً)</span>
            </div>
          </div>

          <div class="contact-method" style="cursor:default;">
            <div class="contact-method-icon" style="background:rgba(14,165,233,.15);color:#0EA5E9;">
              <i class="fas fa-bolt"></i>
            </div>
            <div>
              <span class="contact-method-label">متوسط وقت الرد</span>
              <span class="contact-method-value">أقل من ساعتين</span>
            </div>
          </div>

          <div style="margin-top:2rem;padding:1.25rem;background:rgba(108,63,197,.08);border:1px solid rgba(108,63,197,.2);border-radius:var(--radius-lg);">
            <p style="font-size:.875rem;color:var(--text-secondary);line-height:1.7;margin:0;">
              &#128161; <strong style="color:var(--primary-light)">نصيحة:</strong>
              يمكنك إضافة الخدمات التي تحتاجها إلى السلة أولاً من صفحة
              <a href="services.html" style="color:var(--primary-light);">الخدمات</a>،
              ثم إرسالها دفعة واحدة عبر واتساب!
            </p>
          </div>
        </div>

        <!-- Form Card -->
        <div class="contact-form-card reveal">
          <h3 style="font-size:1.25rem;font-weight:700;margin-bottom:1.5rem;">أرسل استفسارك</h3>
          <form id="contactForm" onsubmit="event.preventDefault();submitContactForm();">
            <div class="grid-2" style="gap:1rem;">
              <div class="form-group">
                <label class="form-label">الاسم</label>
                <input type="text" id="cName" class="form-control" placeholder="اسمك الكريم" required>
              </div>
              <div class="form-group">
                <label class="form-label">التخصص</label>
                <select id="cSpec" class="form-control" required>
                  <option value="" disabled selected>اختر التخصص...</option>
                  <option>Business</option>
                  <option>IT</option>
                  <option>Health &amp; Social Care</option>
                  <option>Engineering</option>
                  <option>تخصص آخر</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <label class="form-label">نوع الخدمة / الاستفسار</label>
              <select id="cService" class="form-control" required>
                <option value="" disabled selected>اختر الخدمة...</option>
                <option>تدقيق واجبات</option>
                <option>إعداد تقارير</option>
                <option>جلسة شرح</option>
                <option>استفسار عام</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">الرسالة</label>
              <textarea id="cMsg" class="form-control" rows="5"
                placeholder="اكتب تفاصيل طلبك أو استفسارك هنا..." required></textarea>
            </div>
            <button type="submit" class="btn btn-whatsapp" style="width:100%;justify-content:center;">
              <i class="fab fa-whatsapp"></i> إرسال عبر واتساب
            </button>
          </form>
        </div>

      </div>
    </div>
  </section>
</main>
'''
contact_script = '''
<script>
function submitContactForm() {
  const name    = document.getElementById('cName').value;
  const spec    = document.getElementById('cSpec').value;
  const service = document.getElementById('cService').value;
  const msg     = document.getElementById('cMsg').value;
  const text = encodeURIComponent(
    'مرحباً فريق BTEC HUB 👋\\n\\n' +
    '📌 *استفسار جديد*\\n\\n' +
    '👤 *الاسم:* ' + name + '\\n' +
    '🎓 *التخصص:* ' + spec + '\\n' +
    '🛠️ *الخدمة:* ' + service + '\\n\\n' +
    '💬 *الرسالة:*\\n' + msg
  );
  window.open('https://wa.me/962786003597?text=' + text, '_blank');
}
</script>
'''
write('contact.html', contact_body, contact_script)

print('\n🎉  All 7 files rebuilt successfully with correct Arabic encoding + original design!')

