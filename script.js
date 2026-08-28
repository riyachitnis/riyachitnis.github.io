document.addEventListener('DOMContentLoaded', () => {
  initMenu();
  initFrictionTool();
  initWhatsAppLinks();
  initBreathingReset();
  initReveals();
  document.getElementById('year').textContent = new Date().getFullYear();
});

function initMenu() {
  const button = document.getElementById('menuButton');
  const nav = document.getElementById('siteNav');
  if (!button || !nav) return;

  const close = () => {
    button.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
    document.body.classList.remove('menu-open');
  };

  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('open', open);
    document.body.classList.toggle('menu-open', open);
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', close));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') close();
  });
}

function initFrictionTool() {
  const tool = document.querySelector('[data-friction-tool]');
  if (!tool) return;
  const tabs = [...tool.querySelectorAll('[role="tab"]')];

  function selectTab(tab, moveFocus = false) {
    tabs.forEach(item => {
      const selected = item === tab;
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
      const panel = document.getElementById(item.getAttribute('aria-controls'));
      if (panel) {
        panel.hidden = !selected;
        panel.classList.toggle('active', selected);
      }
    });
    if (moveFocus) tab.focus();
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => selectTab(tab));
    tab.addEventListener('keydown', event => {
      let nextIndex;
      if (event.key === 'ArrowRight') nextIndex = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') nextIndex = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') nextIndex = 0;
      if (event.key === 'End') nextIndex = tabs.length - 1;
      if (nextIndex !== undefined) {
        event.preventDefault();
        selectTab(tabs[nextIndex], true);
      }
    });
  });
}

function initWhatsAppLinks() {
  const phone = '971502278067';
  const messages = {
    fit: "Hi Riya, I found Clearer Days and I'd like to book a free 20-minute conversation about ADHD coaching.",
    reset: "Hi Riya, I found Clearer Days and I'd like to learn more about the Focus Reset session (AED 500).",
    momentum: "Hi Riya, I found Clearer Days and I'd like to learn more about the four-week Momentum coaching option (AED 1,800).",
    partnership: "Hi Riya, I found Clearer Days and I'd like to learn more about the eight-week Ongoing Partnership (AED 3,200)."
  };

  document.querySelectorAll('[data-whatsapp]').forEach(link => {
    const key = link.dataset.whatsapp;
    link.href = `https://wa.me/${phone}?text=${encodeURIComponent(messages[key] || messages.fit)}`;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  });
}

function initBreathingReset() {
  const button = document.getElementById('breathButton');
  const restart = document.getElementById('breathRestart');
  const ring = document.getElementById('breathRing');
  const count = document.getElementById('breathCount');
  const status = document.getElementById('breathStatus');
  if (!button || !restart || !ring || !count || !status) return;

  let timer = null;
  let phaseTimer = null;
  let remaining = 60;
  let running = false;
  const phases = [
    { label: 'Breathe in slowly', className: 'inhale', duration: 4000 },
    { label: 'Pause gently', className: '', duration: 2000 },
    { label: 'Breathe out slowly', className: 'exhale', duration: 6000 }
  ];
  let phase = 0;

  function showPhase() {
    const current = phases[phase];
    ring.classList.remove('inhale', 'exhale');
    if (current.className) ring.classList.add(current.className);
    status.textContent = current.label;
    phaseTimer = window.setTimeout(() => {
      if (!running) return;
      phase = (phase + 1) % phases.length;
      showPhase();
    }, current.duration);
  }

  function stop(completed = false) {
    running = false;
    window.clearInterval(timer);
    window.clearTimeout(phaseTimer);
    timer = null;
    phaseTimer = null;
    ring.classList.remove('inhale', 'exhale');
    button.textContent = completed ? 'Start again' : 'Resume breathing';
    status.textContent = completed ? 'Reset complete. Take your time.' : 'Paused';
    restart.hidden = completed;
  }

  function start(reset = false) {
    if (reset || remaining <= 0) {
      remaining = 60;
      phase = 0;
      count.textContent = remaining;
    }
    running = true;
    button.textContent = 'Pause';
    restart.hidden = false;
    showPhase();
    timer = window.setInterval(() => {
      remaining -= 1;
      count.textContent = Math.max(remaining, 0);
      if (remaining <= 0) stop(true);
    }, 1000);
  }

  button.addEventListener('click', () => running ? stop(false) : start(remaining <= 0));
  restart.addEventListener('click', () => {
    stop(false);
    remaining = 60;
    phase = 0;
    count.textContent = remaining;
    button.textContent = 'Start breathing';
    status.textContent = 'Ready when you are';
    restart.hidden = true;
  });
}

function initReveals() {
  const items = document.querySelectorAll('.reveal');
  if (!items.length) return;
  if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    items.forEach(item => item.classList.add('visible'));
    return;
  }
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px' });
  items.forEach(item => observer.observe(item));
}
