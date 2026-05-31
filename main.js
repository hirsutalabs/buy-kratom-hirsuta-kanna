// HirsutaLab - Main JS
document.addEventListener('DOMContentLoaded', () => {

  // ---- LANG SWITCHER (click-based, stable) ----
  const switcher = document.querySelector('.lang-switcher');
  if (switcher) {
    const btn = switcher.querySelector('.lang-active');

    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      switcher.classList.toggle('open');
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!switcher.contains(e.target)) {
        switcher.classList.remove('open');
      }
    });

    // Close on Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') switcher.classList.remove('open');
    });
  }

  // ---- SCROLL FADE-IN ----
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.opacity = '1';
        e.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.why-item, .cta-section').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = '0.5s ease';
    observer.observe(el);
  });

  // ---- NAV SCROLL EFFECT ----
  const nav = document.querySelector('.nav');
  window.addEventListener('scroll', () => {
    nav.style.borderBottomColor = window.scrollY > 80
      ? 'rgba(181, 200, 122, 0.25)'
      : 'rgba(181, 200, 122, 0.15)';
  }, { passive: true });

});
