(function () {
  'use strict';

  var root = document.documentElement;
  var system = window.matchMedia('(prefers-color-scheme: dark)');
  var preference;
  var button;

  try {
    preference = localStorage.getItem('site-theme');
  } catch (error) { /* Storage may be unavailable in private browsing. */ }
  if (preference !== 'light' && preference !== 'dark') preference = null;

  function apply(theme) {
    root.setAttribute('data-theme', theme);
    if (button) {
      button.setAttribute('aria-pressed', String(theme === 'dark'));
      button.title = 'Switch to ' + (theme === 'dark' ? 'light' : 'dark') + ' mode';
    }
  }

  apply(preference || (system.matches ? 'dark' : 'light'));

  document.addEventListener('DOMContentLoaded', function () {
    button = document.querySelector('.theme-toggle');
    if (!button) return;
    button.hidden = false;
    apply(root.getAttribute('data-theme'));
    button.addEventListener('click', function () {
      preference = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      apply(preference);
      try {
        localStorage.setItem('site-theme', preference);
      } catch (error) { /* Switching still works without persistence. */ }
    });
  });

  function followSystem(event) {
    if (!preference) apply(event.matches ? 'dark' : 'light');
  }
  if (system.addEventListener) system.addEventListener('change', followSystem);
  else system.addListener(followSystem);
}());
