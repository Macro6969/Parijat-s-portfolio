/* ==========================================================================
   Parijat Majumdar — Portfolio scripts (vanilla JavaScript)
   1. Mobile navigation   2. Header shadow   3. Active link on scroll
   4. Reveal on scroll    5. Simulated telemetry   6. Reduced-motion handling
   ========================================================================== */

(function () {
  "use strict";

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* 1. MOBILE NAVIGATION ------------------------------------------------- */
  var header = document.querySelector(".site-header");
  var toggle = document.getElementById("nav-toggle");
  var nav = document.getElementById("site-nav");

  function setMenu(open) {
    if (!toggle || !nav) return;
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    nav.classList.toggle("is-open", open);
    if (header) header.classList.toggle("is-open", open);
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      setMenu(toggle.getAttribute("aria-expanded") !== "true");
    });

    // Close after choosing a link
    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) setMenu(false);
    });

    // Close with the Escape key and return focus to the button
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setMenu(false);
        toggle.focus();
      }
    });

    // Reset when the window grows to desktop size
    window.addEventListener("resize", function () {
      if (window.innerWidth > 760) setMenu(false);
    });
  }

  /* 2. HEADER BORDER AFTER SCROLLING ------------------------------------- */
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* 3. HIGHLIGHT THE NAV LINK OF THE SECTION IN VIEW ---------------------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".site-nav a[data-section]"));

  // The page order is projects -> pipeline -> skills -> about -> contact
  function sectionFor(id) {
    return id === "pipeline" ? "projects" : id;
  }

  if ("IntersectionObserver" in window && navLinks.length) {
    var sectionEls = ["projects", "pipeline", "skills", "about", "contact"]
      .map(function (id) { return document.getElementById(id); })
      .filter(Boolean);

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var current = sectionFor(entry.target.id);
        navLinks.forEach(function (link) {
          link.classList.toggle("is-active", link.dataset.section === current);
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });

    sectionEls.forEach(function (el) { spy.observe(el); });

    // Home is active while the hero is in view
    var hero = document.querySelector(".hero");
    if (hero) {
      new IntersectionObserver(function (entries) {
        if (entries[0].isIntersecting) {
          navLinks.forEach(function (link) {
            link.classList.toggle("is-active", link.dataset.section === "top");
          });
        }
      }, { rootMargin: "-45% 0px -50% 0px" }).observe(hero);
    }
  }

  /* 4. REVEAL ELEMENTS AS THEY SCROLL INTO VIEW ---------------------------- */
  var revealEls = document.querySelectorAll("[data-reveal]");

  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var revealer = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target); // animate only once
        }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) { revealer.observe(el); });
  }

  /* 5. SIMULATED TELEMETRY (clearly labelled as simulated in the UI) ------- */
  function sign(n) { return (n >= 0 ? "+" : "−") + Math.abs(n).toFixed(2); }

  function startTelemetry(frame) {
    var x = 0, y = 0, z = 0.12, h = 18;
    var fields = {
      x: frame.querySelector('[data-tele="x"]'),
      y: frame.querySelector('[data-tele="y"]'),
      z: frame.querySelector('[data-tele="z"]'),
      h: frame.querySelector('[data-tele="h"]')
    };
    if (!fields.x) return;

    function tick() {
      x += 0.04 + Math.random() * 0.05;
      y += 0.08 + Math.random() * 0.06;
      z = 0.12 + Math.sin(y) * 0.04;
      h = (h + (Math.random() * 3 - 1)) % 360;
      if (y > 9) { x = 0; y = 0; }
      fields.x.textContent = sign(x);
      fields.y.textContent = sign(y);
      fields.z.textContent = z.toFixed(2);
      fields.h.textContent = String(Math.round(Math.abs(h))).padStart(3, "0") + "°";
    }
    tick();
    if (!prefersReducedMotion) setInterval(tick, 900);
  }

  document.querySelectorAll(".vis").forEach(startTelemetry);

  /* 6. REDUCED MOTION: remove the looping SVG "rover" dot ------------------ */
  if (prefersReducedMotion) {
    document.querySelectorAll(".vis__rover").forEach(function (el) { el.remove(); });
  }
})();
