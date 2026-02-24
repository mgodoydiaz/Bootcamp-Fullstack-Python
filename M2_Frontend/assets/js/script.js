/* global bootstrap */

$(function () {
  const $body = $("body");

  // Smooth scroll
  $("a.nav-link").on("click", function (e) {
    const href = $(this).attr("href");
    if (!href || !href.startsWith("#")) return;

    e.preventDefault();
    const $target = $(href);
    if ($target.length === 0) return;

    const navH = $("#topNav").outerHeight() || 0;
    const top = $target.offset().top - navH + 2;

    $("html, body").animate({ scrollTop: top }, 450);

    // Collapse navbar on mobile
    const nav = document.getElementById("navLinks");
    if (nav && nav.classList.contains("show")) {
      bootstrap.Collapse.getOrCreateInstance(nav).hide();
    }
  });

  // Active link highlighting on scroll
  const sectionIds = ["#about", "#experience", "#projects", "#skills", "#education", "#contact"];
  const $links = $("a.nav-link");

  function updateActiveNav() {
    const scrollPos = $(window).scrollTop() || 0;
    const navH = $("#topNav").outerHeight() || 0;

    let current = "#about";
    for (const id of sectionIds) {
      const $sec = $(id);
      if ($sec.length === 0) continue;
      const top = $sec.offset().top - navH - 10;
      if (scrollPos >= top) current = id;
    }

    $links.removeClass("active");
    $links.filter(`[href="${current}"]`).addClass("active");
  }

  $(window).on("scroll", updateActiveNav);
  updateActiveNav();

  // Theme toggle (event 1)
  const savedTheme = localStorage.getItem("cv_theme");
  if (savedTheme === "light") $body.addClass("light");

  $("#themeToggle").on("click", function () {
    $body.toggleClass("light");
    localStorage.setItem("cv_theme", $body.hasClass("light") ? "light" : "dark");
    toast($body.hasClass("light") ? "Light theme enabled" : "Dark theme enabled");
  });

  // Accent shuffle (event 2) changes colors in sections
  const accents = [
    "#4f8cff",
    "#f97316",
    "#a855f7",
    "#22c55e",
    "#06b6d4",
    "#e11d48",
  ];

  $("#accentShuffle").on("click", function () {
    const next = accents[Math.floor(Math.random() * accents.length)];
    document.documentElement.style.setProperty("--accent", next);
    toast("Accent updated");
  });

  // Footer year
  $("#year").text(new Date().getFullYear());

  // Contact form validation (event 3)
  function validEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  $("#contactForm").on("submit", function (e) {
    e.preventDefault();

    const $name = $("#name");
    const $email = $("#email");
    const $msg = $("#message");

    const nameOk = ($name.val() || "").trim().length >= 2;
    const emailOk = validEmail(($email.val() || "").trim());
    const msgOk = ($msg.val() || "").trim().length >= 10;

    setValidity($name, nameOk);
    setValidity($email, emailOk);
    setValidity($msg, msgOk);

    if (nameOk && emailOk && msgOk) {
      toast("Looks good. Message validated locally.");
    } else {
      toast("Please fix the highlighted fields.");
    }
  });

  $("#clearForm").on("click", function () {
    $("#contactForm")[0].reset();
    $(".is-invalid, .is-valid").removeClass("is-invalid is-valid");
  });

  function setValidity($el, ok) {
    $el.toggleClass("is-valid", ok);
    $el.toggleClass("is-invalid", !ok);
  }

  // Toast helper
  function toast(message) {
    $("#toastMsg").text(message);
    const el = document.getElementById("liveToast");
    bootstrap.Toast.getOrCreateInstance(el, { delay: 2200 }).show();
  }
});
