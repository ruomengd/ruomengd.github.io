(function () {
  'use strict';

  var map = document.querySelector('.visitor-map');
  if (!map) return;

  var desktop = window.matchMedia('(min-width: 768px)');
  var widget = map.querySelector('.visitor-map-widget');
  var status = map.querySelector('.visitor-map-status');
  var retry = map.querySelector('.visitor-map-retry');
  var loading = false;
  var queueIndex;
  var renderTimeout;
  var observer = new MutationObserver(function () {
    if (widget.querySelector('img')) {
      clearTimeout(renderTimeout);
      loading = false;
      status.hidden = true;
    }
  });
  observer.observe(widget, { childList: true, subtree: true });

  function placeMap() {
    var target = document.querySelector(desktop.matches
      ? '.visitor-map--desktop' : '.visitor-map--mobile');
    // Pages without a sidebar still have the mobile placement available.
    if (!target) target = document.querySelector('.visitor-map--mobile');
    if (target && map.parentNode !== target) target.appendChild(map);
    if (target) target.style.display = 'block';
    document.querySelectorAll('.visitor-map-wrapper').forEach(function (wrapper) {
      if (wrapper !== target) wrapper.style.display = 'none';
    });
  }

  function loadMap() {
    if (loading || widget.querySelector('img')) return;
    loading = true;
    status.hidden = true;
    renderTimeout = setTimeout(function () {
      loading = false;
      status.hidden = false;
    }, 15000);

    // Keep one queue entry and one map when switching layouts or retrying.
    if (queueIndex === undefined) {
      var marker = document.createElement('script');
      marker.id = '_wauvisitor';
      widget.appendChild(marker);
      window._wau = window._wau || [];
      queueIndex = window._wau.length;
      window._wau.push(['map', map.getAttribute('data-visitor-map-id'),
        'visitor', '200', '100', 'classic', 'default-blue']);
    }

    if (typeof window.WAU_map === 'function') {
      window.WAU_map(map.getAttribute('data-visitor-map-id'),
        '200', '100', 'classic', 'default-blue', queueIndex);
      return;
    }

    if (widget.querySelector('#visitor-map-loader')) return;

    var script = document.createElement('script');
    script.id = 'visitor-map-loader';
    script.async = true;
    script.src = 'https://waust.at/m.js';
    script.onerror = function () {
      clearTimeout(renderTimeout);
      loading = false;
      script.remove();
      status.hidden = false;
    };
    widget.appendChild(script);
  }

  placeMap();
  if (desktop.addEventListener) desktop.addEventListener('change', placeMap);
  else desktop.addListener(placeMap);
  retry.addEventListener('click', loadMap);
  loadMap();
}());
