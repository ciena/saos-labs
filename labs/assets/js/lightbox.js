// Click-to-zoom lightbox for topology/diagram SVGs.
// No dependencies. Enlarges any content SVG to a full-viewport overlay;
// click the overlay or press Escape to dismiss.
(function () {
  "use strict";

  function init() {
    var diagrams = document.querySelectorAll('.rst-content img[src$=".svg"]');
    if (!diagrams.length) {
      return; // pages with no diagrams (e.g. index) — nothing to do
    }

    // Single reusable overlay for the whole page.
    var overlay = document.createElement("div");
    overlay.className = "topo-lightbox";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    var overlayImg = document.createElement("img");
    overlay.appendChild(overlayImg);
    document.body.appendChild(overlay);

    function open(src, alt) {
      overlayImg.setAttribute("src", src);
      overlayImg.setAttribute("alt", alt || "");
      overlay.classList.add("open");
      document.body.classList.add("lightbox-open");
    }

    function close() {
      overlay.classList.remove("open");
      document.body.classList.remove("lightbox-open");
      overlayImg.removeAttribute("src");
    }

    diagrams.forEach(function (img) {
      img.classList.add("zoomable");
      img.addEventListener("click", function () {
        open(img.getAttribute("src"), img.getAttribute("alt"));
      });
    });

    overlay.addEventListener("click", close);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && overlay.classList.contains("open")) {
        close();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
