(function () {
  'use strict';

  /* ---------- Menú móvil ---------- */
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      toggle.setAttribute('aria-label', isOpen ? 'Cerrar menú' : 'Abrir menú');
    });

    // Cierra el menú al pulsar un enlace
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ---------- Header: sombra al hacer scroll ---------- */
  var header = document.getElementById('site-header');
  var toTopBtn = document.getElementById('to-top');

  function onScroll() {
    var scrolled = window.scrollY > 12;
    if (header) header.style.boxShadow = scrolled ? '0 6px 20px rgba(26,26,26,0.06)' : 'none';
    if (toTopBtn) toTopBtn.classList.toggle('visible', window.scrollY > 500);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (toTopBtn) {
    toTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ---------- Animación al hacer scroll (reveal) ---------- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---------- Formulario de contacto (demo, sin backend) ---------- */
  var form = document.getElementById('contact-form');
  var note = document.getElementById('form-note');

  if (form && note) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      if (!form.checkValidity()) {
        note.textContent = 'Por favor, completa los campos obligatorios.';
        note.classList.remove('success');
        return;
      }

      // NOTA: este formulario es una demo de interfaz. Para recibir los
      // mensajes de verdad, conéctalo a tu backend, a un servicio de
      // formularios (p. ej. Fluent Forms) o a un webhook propio.
      note.textContent = '¡Gracias! Hemos recibido tu mensaje y te contactaremos en breve.';
      note.classList.add('success');
      form.reset();
    });
  }
})();
