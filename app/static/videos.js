/* Videos del curso: reproductor grande, lista del curso, anterior y siguiente, y marca de vistos.
   Los vistos se guardan solo en el navegador de cada persona (localStorage). */
(function () {
  var raiz = document.getElementById("videos");
  if (!raiz) return;

  var items = [].slice.call(raiz.querySelectorAll(".video-item"));
  var marco = document.getElementById("video-marco");
  var botonVisto = document.getElementById("video-visto");
  var CLAVE = "ibp-videos-vistos";
  var actual = 0;

  function leer() {
    try { return JSON.parse(localStorage.getItem(CLAVE)) || []; } catch (e) { return []; }
  }
  function guardar(lista) {
    try { localStorage.setItem(CLAVE, JSON.stringify(lista)); } catch (e) { /* sin almacenamiento: no pasa nada */ }
  }
  var vistos = leer();

  function pintarProgreso() {
    items.forEach(function (it) { it.classList.toggle("visto", vistos.indexOf(it.dataset.numero) !== -1); });
    var n = vistos.length, total = items.length;
    document.getElementById("video-progreso-texto").textContent = "Has visto " + n + " de " + total;
    var barra = document.getElementById("video-progreso");
    barra.setAttribute("aria-valuenow", n);
    barra.firstElementChild.style.width = (100 * n / total) + "%";
    var visto = vistos.indexOf(items[actual].dataset.numero) !== -1;
    botonVisto.setAttribute("aria-pressed", visto ? "true" : "false");
    botonVisto.textContent = visto ? "Quitar de vistos" : "Marcar como visto";
  }

  function mostrar(i, reproducir) {
    actual = Math.max(0, Math.min(items.length - 1, i));
    var it = items[actual], d = it.dataset;
    items.forEach(function (x) { x.removeAttribute("aria-current"); });
    it.setAttribute("aria-current", "true");
    document.getElementById("video-modulo").textContent = "Módulo " + d.cursoModulo + " · video " + d.numero + " de " + items.length;
    document.getElementById("video-titulo").textContent = d.titulo;
    document.getElementById("video-texto").textContent = d.texto;
    marco.textContent = "";
    if (d.youtube) {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(d.youtube) + (reproducir ? "?autoplay=1" : "");
      f.title = d.titulo;
      f.allowFullscreen = true;
      f.setAttribute("allow", "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture");
      marco.appendChild(f);
    } else {
      var ph = document.createElement("div");
      ph.className = "ph";
      ph.textContent = "[video " + d.numero + "]";
      marco.appendChild(ph);
    }
    document.getElementById("video-anterior").disabled = actual === 0;
    document.getElementById("video-siguiente").disabled = actual === items.length - 1;
    pintarProgreso();
  }

  items.forEach(function (it, i) { it.addEventListener("click", function () { mostrar(i, true); }); });
  document.getElementById("video-anterior").addEventListener("click", function () { mostrar(actual - 1, true); });
  document.getElementById("video-siguiente").addEventListener("click", function () { mostrar(actual + 1, true); });
  botonVisto.addEventListener("click", function () {
    var n = items[actual].dataset.numero, k = vistos.indexOf(n);
    if (k === -1) vistos.push(n); else vistos.splice(k, 1);
    guardar(vistos);
    pintarProgreso();
  });

  mostrar(0, false);
})();
