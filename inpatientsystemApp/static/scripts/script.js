// Écouteur d'événement de défilement
window.addEventListener('scroll', function () {
  // Calcul de la position de la barre de défilement
  const scrollPercentage = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;

  // Mise à jour de la position du curseur de la barre de défilement
  document.getElementById('custom-scrollbar-thumb').style.top = `${scrollPercentage}%`;
});

// Écouteur d'événement de clic sur la barre de défilement
document.getElementById('custom-scrollbar-thumb').addEventListener('click', function (event) {
  // Calcul de la nouvelle position de défilement basée sur la position du clic
  const newScrollPosition = (event.clientY / window.innerHeight) * document.documentElement.scrollHeight;

  // Définir la nouvelle position de défilement
  window.scrollTo({ top: newScrollPosition, behavior: 'smooth' });
});
