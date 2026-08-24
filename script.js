/* ==========================================================================
   RIYA CHITNIS - ADHD COACHING PLATFORM
   Apple-inspired Interactive Client Experience Logic
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Theme Toggle (Apple Dark / Light)
  initThemeToggle();

  // 2. Mobile Navigation Toggle
  initMobileMenu();

  // 3. Interactive ADHD Clarity Self-Assessment
  initQuiz();

  // 4. Currency Switcher (AED / USD)
  initCurrencyToggle();

  // 5. Interactive Breathing / Focus Pacer
  initBreathingTool();

  // 6. FAQ Accordion Logic
  initFAQ();

  // 7. Booking Modal & Lead Conversion
  initBookingModal();

  // 8. Header scroll backdrop elevation
  initScrollEffects();
});

/* --------------------------------------------------------------------------
   1. THEME TOGGLE
   -------------------------------------------------------------------------- */
function initThemeToggle() {
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  if (!themeToggleBtn) return;

  const currentTheme = localStorage.getItem('rc_theme') || 'dark';
  if (currentTheme === 'light') {
    document.body.classList.add('light-theme');
    updateThemeIcon(true);
  }

  themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('light-theme');
    const isLight = document.body.classList.contains('light-theme');
    localStorage.setItem('rc_theme', isLight ? 'light' : 'dark');
    updateThemeIcon(isLight);
  });
}

function updateThemeIcon(isLight) {
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  if (!themeToggleBtn) return;
  themeToggleBtn.innerHTML = isLight
    ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`
    : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;
}

/* --------------------------------------------------------------------------
   2. MOBILE NAVIGATION
   -------------------------------------------------------------------------- */
function initMobileMenu() {
  const mobileBtn = document.getElementById('mobileMenuBtn');
  const navLinks = document.getElementById('navLinks');
  if (!mobileBtn || !navLinks) return;

  mobileBtn.addEventListener('click', () => {
    navLinks.classList.toggle('mobile-open');
  });

  // Close when clicking nav links
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('mobile-open');
    });
  });
}

/* --------------------------------------------------------------------------
   3. INTERACTIVE ADHD CLARITY QUIZ
   -------------------------------------------------------------------------- */
function initQuiz() {
  const steps = document.querySelectorAll('.quiz-step');
  const progressFill = document.getElementById('quizProgressFill');
  const scoreAnswers = [];

  window.selectQuizOption = function(stepIndex, points, text) {
    scoreAnswers[stepIndex - 1] = { points, text };
    
    // highlight selected button in step
    const currentStepEl = document.getElementById(`quizStep${stepIndex}`);
    if (currentStepEl) {
      currentStepEl.querySelectorAll('.quiz-option-btn').forEach(btn => btn.classList.remove('selected'));
      event.currentTarget.classList.add('selected');
    }

    // Auto advance after slight delay for smooth feel
    setTimeout(() => {
      goToQuizStep(stepIndex + 1);
    }, 280);
  };

  window.goToQuizStep = function(stepNum) {
    steps.forEach(step => step.classList.remove('active'));
    
    const targetStep = document.getElementById(`quizStep${stepNum}`);
    if (targetStep) {
      targetStep.classList.add('active');
      if (progressFill) {
        const percent = Math.min(100, (stepNum / 4) * 100);
        progressFill.style.width = `${percent}%`;
      }
    } else if (stepNum > 4) {
      // Show results
      showQuizResults();
    }
  };

  function showQuizResults() {
    steps.forEach(step => step.classList.remove('active'));
    const resultStep = document.getElementById('quizStepResult');
    if (resultStep) {
      resultStep.classList.add('active');
      if (progressFill) progressFill.style.width = '100%';
    }

    // Calculate total score
    let totalScore = 0;
    scoreAnswers.forEach(ans => {
      if (ans && ans.points) totalScore += ans.points;
    });

    const resultBadge = document.getElementById('resultBadge');
    const resultTitle = document.getElementById('resultTitle');
    const resultDesc = document.getElementById('resultDesc');
    const matchScore = document.getElementById('matchScore');

    if (totalScore >= 10) {
      if (resultBadge) resultBadge.textContent = "High Match • Exceptional Potential for Coaching";
      if (resultTitle) resultTitle.textContent = "You are ready for transformative ADHD Architecture.";
      if (resultDesc) resultDesc.textContent = "Your responses reveal classic high-potential ADHD patterns: brilliant ideas hampered by executive function friction, dopamine fatigue, or overwhelming context-switching. 1-on-1 coaching with Riya will help you build custom external systems rather than relying on exhausting brute willpower.";
      if (matchScore) matchScore.textContent = "96% Fit";
    } else {
      if (resultBadge) resultBadge.textContent = "Strong Match • Targeted System Upgrade";
      if (resultTitle) resultTitle.textContent = "ADHD Clarity & Flow Optimization";
      if (resultDesc) resultDesc.textContent = "You have solid foundational strengths, but specific friction points like time estimation or task paralysis are draining your daily energy. Targeted ADHD coaching will streamline your workflows and create effortless momentum.";
      if (matchScore) matchScore.textContent = "88% Fit";
    }
  }

  window.restartQuiz = function() {
    scoreAnswers.length = 0;
    document.querySelectorAll('.quiz-option-btn').forEach(btn => btn.classList.remove('selected'));
    goToQuizStep(1);
  };
}

/* --------------------------------------------------------------------------
   4. CURRENCY SWITCHER (AED / USD)
   -------------------------------------------------------------------------- */
function initCurrencyToggle() {
  const btnAED = document.getElementById('btnAED');
  const btnUSD = document.getElementById('btnUSD');
  const prices = document.querySelectorAll('.price-amount');

  if (!btnAED || !btnUSD) return;

  const priceData = {
    AED: {
      single: "AED 950",
      twelve: "AED 9,800",
      exec: "AED 16,500"
    },
    USD: {
      single: "$260",
      twelve: "$2,670",
      exec: "$4,490"
    }
  };

  function updatePrices(currency) {
    const p1 = document.getElementById('priceSingle');
    const p2 = document.getElementById('priceTwelve');
    const p3 = document.getElementById('priceExec');

    if (p1) p1.textContent = priceData[currency].single;
    if (p2) p2.textContent = priceData[currency].twelve;
    if (p3) p3.textContent = priceData[currency].exec;
  }

  btnAED.addEventListener('click', () => {
    btnAED.classList.add('active');
    btnUSD.classList.remove('active');
    updatePrices('AED');
  });

  btnUSD.addEventListener('click', () => {
    btnUSD.classList.add('active');
    btnAED.classList.remove('active');
    updatePrices('USD');
  });
}

/* --------------------------------------------------------------------------
   5. INTERACTIVE BREATHING / FOCUS RESET TOOL
   -------------------------------------------------------------------------- */
function initBreathingTool() {
  const statusText = document.getElementById('breathingStatus');
  const actionBtn = document.getElementById('breathingToggleBtn');
  const circle = document.querySelector('.breathing-circle-pulse');
  if (!statusText || !actionBtn || !circle) return;

  let isRunning = true;
  let cycleTimer = null;

  const cycleTexts = ["Inhale deeply...", "Hold focus...", "Exhale gently...", "Rest & Reset..."];
  let textIndex = 0;

  function runCycle() {
    statusText.textContent = cycleTexts[textIndex];
    textIndex = (textIndex + 1) % cycleTexts.length;
  }

  cycleTimer = setInterval(runCycle, 2000);

  actionBtn.addEventListener('click', () => {
    if (isRunning) {
      clearInterval(cycleTimer);
      circle.style.animationPlayState = 'paused';
      statusText.textContent = 'Paused';
      actionBtn.textContent = 'Resume Reset';
      isRunning = false;
    } else {
      circle.style.animationPlayState = 'running';
      cycleTimer = setInterval(runCycle, 2000);
      statusText.textContent = 'Inhale deeply...';
      actionBtn.textContent = 'Pause Reset';
      isRunning = true;
    }
  });
}

/* --------------------------------------------------------------------------
   6. FAQ ACCORDION
   -------------------------------------------------------------------------- */
function initFAQ() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      // Close all
      faqItems.forEach(i => i.classList.remove('active'));
      // Toggle clicked
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });
}

/* --------------------------------------------------------------------------
   7. BOOKING MODAL & CONSULTATION
   -------------------------------------------------------------------------- */
function initBookingModal() {
  const modal = document.getElementById('bookingModal');
  const closeBtn = document.getElementById('modalCloseBtn');
  const bookingForm = document.getElementById('bookingForm');
  const toast = document.getElementById('toastMsg');
  const openButtons = document.querySelectorAll('[data-open-modal="booking"]');

  if (!modal) return;

  window.openBookingModal = function(packagePreset = '') {
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    if (packagePreset) {
      const select = document.getElementById('modalProgramSelect');
      if (select) select.value = packagePreset;
    }
  };

  window.closeBookingModal = function() {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  };

  openButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const preset = btn.getAttribute('data-package') || '';
      openBookingModal(preset);
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeBookingModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeBookingModal();
    }
  });

  // Handle escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      closeBookingModal();
    }
  });

  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('bookingName').value;
      const email = document.getElementById('bookingEmail').value;
      const location = document.getElementById('bookingLocation').value;
      const program = document.getElementById('modalProgramSelect').value;
      const notes = document.getElementById('bookingNotes').value;

      closeBookingModal();
      showToast(`Thank you, ${name}! Your consultation request is received. Riya will be in touch shortly.`);

      // Optional: Prepare quick WhatsApp message link or redirect
      const cleanPhone = "+971500000000"; // Example UAE WhatsApp contact
      const waMsg = encodeURIComponent(`Hi Riya! My name is ${name}. I am in ${location} and interested in ${program} ADHD coaching. Notes: ${notes}`);
      console.log(`Booking request logged: ${name} (${email}) - ${program}`);
    });
  }
}

function showToast(message) {
  const toast = document.getElementById('toastMsg');
  const toastText = document.getElementById('toastText');
  if (!toast) return;

  if (toastText) toastText.textContent = message;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, 4500);
}

/* --------------------------------------------------------------------------
   8. HEADER SCROLL BACKDROP ELEVATION
   -------------------------------------------------------------------------- */
function initScrollEffects() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 20) {
      header.style.boxShadow = '0 8px 24px rgba(0, 0, 0, 0.3)';
    } else {
      header.style.boxShadow = 'none';
    }
  });
}
