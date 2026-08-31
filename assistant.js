/* =========================================================
   BTEC HUB – BTEC Assistant JavaScript
   AI Chatbot Simulation (rule-based responses)
   ========================================================= */

'use strict';

// ══════════════════════════════════════════
// KNOWLEDGE BASE
// ══════════════════════════════════════════
const KB = {
  ar: {
    greetings: ['مرحبا', 'هلا', 'السلام', 'أهلا', 'hi', 'hello'],
    services: {
      keywords: ['خدمات', 'service', 'ماذا تقدمون', 'ما هي الخدمات'],
      response: `نقدم في BTEC HUB خدمات متعددة للطلاب:\n\n📝 **تدقيق الواجبات** – مراجعة وتقديم ملاحظات احترافية\n📊 **إعداد التقارير** – مساعدة في صياغة التقارير\n🎯 **الشرح والتوجيه** – جلسات فردية لفهم المادة\n📁 **مراجعة المشاريع** – تقييم المشاريع قبل التسليم\n\nهل تريد معرفة المزيد عن خدمة معينة؟`
    },
    price: {
      keywords: ['سعر', 'كم', 'تكلفة', 'price', 'cost'],
      response: `أسعارنا تختلف حسب نوع الخدمة والوحدة. لمعرفة السعر الدقيق:\n\n1️⃣ اختر الخدمة من صفحة الخدمات\n2️⃣ أضفها للسلة\n3️⃣ أرسل طلبك عبر واتساب\n\nسيرد فريقنا بالسعر النهائي خلال وقت قصير ⚡`
    },
    cart: {
      keywords: ['سلة', 'cart', 'كيف أضيف', 'كيف أرسل'],
      response: `للاستخدام السلة:\n\n🛒 **الإضافة**: اضغط "أضف للسلة" على أي خدمة\n👁️ **المراجعة**: اضغط أيقونة السلة في الشريط العلوي\n📲 **الإرسال**: اضغط "إرسال عبر واتساب" وستفتح محادثة جاهزة مع طلبك`
    },
    units: {
      keywords: ['unit', 'وحدة', 'مادة'],
      response: `نغطي وحدات BTEC متعددة حسب التخصص:\n\n💼 **Business**: Unit 1, 2, 3, 4, 6...\n💻 **IT**: Unit 1, 3, 5, 7...\n🏥 **Health & Social Care**: Unit 1, 2, 3...\n⚙️ **Engineering**: Unit 1, 2, 4...\n\nأخبرني بتخصصك والوحدة وسأوجهك للخدمة المناسبة!`
    },
    how: {
      keywords: ['كيف', 'how', 'خطوات', 'طريقة'],
      response: `عملية الطلب بسيطة جداً:\n\n1️⃣ استعرض الخدمات من قائمة "الخدمات"\n2️⃣ اختر ما يناسبك وأضفه للسلة\n3️⃣ أرسل طلبك عبر واتساب\n4️⃣ نرد بالسعر والتفاصيل\n5️⃣ بعد التأكيد والدفع نبدأ التنفيذ\n6️⃣ نسلم لك الخدمة في الوقت المحدد ✅`
    },
    homework: {
      keywords: ['حل واجب', 'اكتب', 'افعل واجب', 'أنجز', 'do assignment', 'write for me'],
      response: `❌ عذراً، لا أقدر على حل الواجبات أو كتابتها نيابةً عنك.\n\n✅ ما أستطيع فعله:\n• توجيهك لفهم المتطلبات\n• شرح المعايير الأكاديمية\n• مساعدتك في اختيار خدمة **تدقيق الواجبات** التي يراجع فيها فريقنا عملك ويقدم لك ملاحظات بنّاءة\n\nهل تريد معرفة المزيد عن خدمة التدقيق؟`
    },
    contact: {
      keywords: ['تواصل', 'contact', 'واتساب', 'whatsapp', 'رقم'],
      response: `للتواصل المباشر:\n\n📱 **واتساب**: الزر الأخضر في الزاوية السفلية\n📧 يمكنك أيضاً زيارة صفحة **تواصل معنا** من القائمة\n\nفريقنا جاهز للرد على أسئلتك! 💬`
    },
    study: {
      keywords: ['دراسة', 'شرح', 'مواد', 'study', 'material', 'resources'],
      response: `في قسم **الدراسة** ستجد:\n\n📖 شروحات تفصيلية للمواد\n📝 ملخصات الوحدات\n🎯 نقاط مهمة للمراجعة\n📌 إرشادات للتطبيق العملي\n\nادخل قسم "الدراسة" من القائمة لاستعراض المحتوى المتاح!`
    },
    default: `أنا **BTEC Assistant** وأنا هنا لمساعدتك! 🤖\n\nيمكنني:\n• شرح الخدمات المتاحة\n• توجيهك لاختيار الخدمة المناسبة\n• الإجابة عن أسئلة الاستخدام\n\nجرب أن تسألني: "ما هي خدماتكم؟" أو "كيف أرسل طلبي؟"`
  },
  en: {
    greetings: ['hello', 'hi', 'hey', 'مرحبا', 'السلام'],
    services: {
      keywords: ['services', 'what do you offer', 'what can you do'],
      response: `BTEC HUB offers multiple services for students:\n\n📝 **Assignment Review** – Professional feedback & corrections\n📊 **Report Writing Help** – Guidance in structuring reports\n🎯 **Tutoring Sessions** – One-on-one subject understanding\n📁 **Project Review** – Assessment before submission\n\nWant to know more about a specific service?`
    },
    price: {
      keywords: ['price', 'cost', 'how much', 'fee'],
      response: `Prices vary by service type and unit. To get an exact price:\n\n1️⃣ Choose the service from the Services page\n2️⃣ Add it to your cart\n3️⃣ Send your request via WhatsApp\n\nOur team will reply with the final price quickly ⚡`
    },
    cart: {
      keywords: ['cart', 'how to add', 'how to send', 'shopping'],
      response: `Using the cart:\n\n🛒 **Add**: Click "Add to Cart" on any service\n👁️ **Review**: Click the cart icon in the top navbar\n📲 **Send**: Click "Send via WhatsApp" and a ready-made message will open`
    },
    units: {
      keywords: ['unit', 'subject', 'module'],
      response: `We cover multiple BTEC units per specialization:\n\n💼 **Business**: Unit 1, 2, 3, 4, 6...\n💻 **IT**: Unit 1, 3, 5, 7...\n🏥 **Health & Social Care**: Unit 1, 2, 3...\n⚙️ **Engineering**: Unit 1, 2, 4...\n\nTell me your specialization and unit and I'll guide you!`
    },
    how: {
      keywords: ['how', 'steps', 'process', 'order'],
      response: `The ordering process is simple:\n\n1️⃣ Browse services from the "Services" menu\n2️⃣ Choose what you need and add to cart\n3️⃣ Send your request via WhatsApp\n4️⃣ We reply with price and details\n5️⃣ After confirmation and payment, we start\n6️⃣ Service delivered on time ✅`
    },
    homework: {
      keywords: ['do my homework', 'write for me', 'do assignment', 'complete my work'],
      response: `❌ Sorry, I cannot complete or write assignments on your behalf.\n\n✅ What I can help with:\n• Guide you to understand requirements\n• Explain academic standards\n• Help you choose our **Assignment Review** service where our team reviews your work and provides constructive feedback\n\nWould you like to know more about the review service?`
    },
    contact: {
      keywords: ['contact', 'whatsapp', 'number', 'reach'],
      response: `To contact us directly:\n\n📱 **WhatsApp**: Green button in the bottom corner\n📧 Visit the **Contact Us** page from the menu\n\nOur team is ready to answer your questions! 💬`
    },
    study: {
      keywords: ['study', 'material', 'resources', 'notes', 'explanation'],
      response: `In the **Study** section you'll find:\n\n📖 Detailed subject explanations\n📝 Unit summaries\n🎯 Key revision points\n📌 Practical application guidelines\n\nVisit "Study" from the menu to explore available content!`
    },
    default: `I'm **BTEC Assistant** here to help! 🤖\n\nI can:\n• Explain available services\n• Guide you in choosing the right service\n• Answer usage questions\n\nTry asking: "What services do you offer?" or "How do I send my request?"`
  }
};

const QUICK_REPLIES = {
  ar: [
    { text: '📋 ما هي الخدمات؟', query: 'ما هي خدماتكم' },
    { text: '💰 السعر', query: 'كم يكلف' },
    { text: '🛒 كيف أطلب؟', query: 'كيف أرسل طلبي' },
    { text: '📚 الوحدات المتاحة', query: 'ما هي الوحدات' },
    { text: '📞 تواصل', query: 'كيف أتواصل معكم' },
  ],
  en: [
    { text: '📋 Our Services', query: 'what services do you offer' },
    { text: '💰 Pricing', query: 'how much does it cost' },
    { text: '🛒 How to Order', query: 'how do I send my request' },
    { text: '📚 Available Units', query: 'what units do you cover' },
    { text: '📞 Contact', query: 'how to contact you' },
  ]
};

// ══════════════════════════════════════════
// INIT
// ══════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  initAssistant();
});

// ══════════════════════════════════════════
// ASSISTANT LOGIC
// ══════════════════════════════════════════
function initAssistant() {
  const fab = document.getElementById('assistantFab');
  const window_ = document.getElementById('assistantWindow');
  const minimizeBtn = document.getElementById('assistantMinimize');
  const input = document.getElementById('assistantInput');
  const sendBtn = document.getElementById('assistantSend');
  const messagesEl = document.getElementById('assistantMessages');
  const quickRepliesEl = document.getElementById('quickReplies');

  if (!fab) return;

  let isOpen = false;
  let hasGreeted = false;

  // Toggle window
  fab.addEventListener('click', () => {
    isOpen = !isOpen;
    window_.classList.toggle('open', isOpen);
    fab.querySelector('i').className = isOpen ? 'fas fa-times' : 'fas fa-robot';

    if (isOpen && !hasGreeted) {
      hasGreeted = true;
      setTimeout(() => {
        const lang = window.BtecMain?.lang || 'ar';
        const greeting = lang === 'ar'
          ? `مرحباً بك في BTEC HUB! 👋\n\nأنا **BTEC Assistant**، مساعدك الذكي. يمكنني توجيهك لاختيار الخدمة المناسبة، شرح كيفية الطلب، والإجابة عن أسئلتك.\n\nكيف يمكنني مساعدتك اليوم؟`
          : `Welcome to BTEC HUB! 👋\n\nI'm **BTEC Assistant**, your smart guide. I can help you choose the right service, explain the ordering process, and answer your questions.\n\nHow can I help you today?`;

        addMessage(greeting, 'bot');
        renderQuickReplies();
      }, 400);
    }
  });

  // Minimize
  minimizeBtn?.addEventListener('click', () => {
    isOpen = false;
    window_.classList.remove('open');
    fab.querySelector('i').className = 'fas fa-robot';
  });

  // Send message
  function handleSend() {
    const text = input?.value?.trim();
    if (!text) return;

    addMessage(text, 'user');
    input.value = '';

    // Show typing
    showTyping();

    setTimeout(() => {
      hideTyping();
      const response = generateResponse(text);
      addMessage(response, 'bot');
      renderQuickReplies();
    }, 800 + Math.random() * 600);
  }

  sendBtn?.addEventListener('click', handleSend);
  input?.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  });

  // Quick replies
  quickRepliesEl?.addEventListener('click', e => {
    const btn = e.target.closest('.quick-reply');
    if (!btn) return;
    const query = btn.getAttribute('data-query');
    if (input) input.value = query;
    handleSend();
  });

  function addMessage(text, role) {
    const msg = document.createElement('div');
    msg.className = `message ${role}`;

    const avatar = document.createElement('div');
    avatar.className = 'message-avatar';
    avatar.innerHTML = role === 'bot' ? '🤖' : '👤';

    const content = document.createElement('div');
    content.className = 'message-content';

    // Convert markdown-like **bold** and \n
    content.innerHTML = text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\n/g, '<br>');

    msg.appendChild(avatar);
    msg.appendChild(content);
    messagesEl?.appendChild(msg);
    messagesEl?.scrollTo({ top: messagesEl.scrollHeight, behavior: 'smooth' });
  }

  function showTyping() {
    const typing = document.createElement('div');
    typing.className = 'message bot';
    typing.id = 'typingIndicator';
    typing.innerHTML = `
      <div class="message-avatar">🤖</div>
      <div class="message-content">
        <div class="typing-indicator">
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
        </div>
      </div>
    `;
    messagesEl?.appendChild(typing);
    messagesEl?.scrollTo({ top: messagesEl.scrollHeight, behavior: 'smooth' });
  }

  function hideTyping() {
    document.getElementById('typingIndicator')?.remove();
  }

  function renderQuickReplies() {
    if (!quickRepliesEl) return;
    const lang = window.BtecMain?.lang || 'ar';
    const replies = QUICK_REPLIES[lang] || QUICK_REPLIES.ar;
    quickRepliesEl.innerHTML = replies.map(r =>
      `<button class="quick-reply" data-query="${r.query}">${r.text}</button>`
    ).join('');
  }
}

// ══════════════════════════════════════════
// RESPONSE GENERATOR
// ══════════════════════════════════════════
function generateResponse(input) {
  const lang = window.BtecMain?.lang || 'ar';
  const kb = KB[lang] || KB.ar;
  const text = input.toLowerCase().trim();

  // Greetings
  if (kb.greetings.some(g => text.includes(g))) {
    const greets = lang === 'ar'
      ? ['أهلاً وسهلاً! 👋 كيف يمكنني مساعدتك؟', 'مرحباً! أنا BTEC Assistant 🤖 كيف أخدمك؟', 'هلا والله! 😊 ماذا تحتاج؟']
      : ['Hello! 👋 How can I help you?', 'Hi there! I\'m BTEC Assistant 🤖 What do you need?', 'Hey! 😊 How can I assist you?'];
    return greets[Math.floor(Math.random() * greets.length)];
  }

  // Check each KB category
  const categories = ['homework', 'cart', 'price', 'services', 'units', 'how', 'contact', 'study'];
  for (const cat of categories) {
    const entry = kb[cat];
    if (entry && entry.keywords.some(k => text.includes(k))) {
      return entry.response;
    }
  }

  // Default
  return kb.default;
}
