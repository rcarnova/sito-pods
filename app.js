(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  function setMenu(open) {
    if (!btn || !nav) return;
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    nav.classList.toggle('open', open);
  }
  if (btn && nav) {
    btn.addEventListener('click', function () { setMenu(btn.getAttribute('aria-expanded') !== 'true'); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 1100) setMenu(false); });
  }

  /* "Leggi di più" (attivo solo su mobile via CSS). Sulle card: tocco sulla scheda, chevron leggero */
  var mq = window.matchMedia ? window.matchMedia('(max-width: 860px)') : { matches: false };
  document.querySelectorAll('[data-more]').forEach(function (el, i) {
    var w = document.createElement('div');
    w.className = 'rm';
    el.parentNode.insertBefore(w, el);
    w.appendChild(el);
    if (!el.id) el.id = 'more-' + i;
    var card = el.closest('.card');
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'rm-btn' + (card ? ' lite' : '');
    b.setAttribute('aria-expanded', 'false');
    b.setAttribute('aria-controls', el.id);
    function label(o) {
      var t = o ? 'Mostra meno' : 'Leggi di più';
      if (card) b.setAttribute('aria-label', t); else b.textContent = t;
    }
    label(false);
    w.appendChild(b);
    function toggle() {
      var o = el.classList.toggle('open');
      b.setAttribute('aria-expanded', o ? 'true' : 'false');
      label(o);
      if (!o && w.getBoundingClientRect().top < 80) w.scrollIntoView({ block: 'start' });
    }
    b.addEventListener('click', toggle);
    if (card) {
      card.addEventListener('click', function (e) {
        if (!mq.matches || e.target.closest('a, button')) return;
        toggle();
      });
    }
  });

  /* rivelazione allo scroll */
  var items = document.querySelectorAll('[data-rv], .prov, .vbars');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!('IntersectionObserver' in window) || reduce) {
    items.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  /* voce di menu attiva */
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav a[href^="#"]'));
  var map = {};
  links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
  if ('IntersectionObserver' in window) {
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var a = map[en.target.id];
        if (a && !a.classList.contains('nav-cta')) a.classList.toggle('on', en.isIntersecting);
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    Object.keys(map).forEach(function (id) { var s = document.getElementById(id); if (s) so.observe(s); });
  }
})();
