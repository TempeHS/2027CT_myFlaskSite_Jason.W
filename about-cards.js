document.addEventListener("DOMContentLoaded", () => {
  const cards = Array.from(document.querySelectorAll(".card-stage .fall-card"));
  if (!cards.length) return;

  let order = cards.map((_, i) => i); // bottom -> top

  const render = () => {
    order.forEach((cardIndex, layer) => {
      cards[cardIndex].style.zIndex = String(10 + layer);
    });
  };

  const next = () => {
    const top = order.pop();
    order.unshift(top);
    render();
  };

  const prev = () => {
    const bottom = order.shift();
    order.push(bottom);
    render();
  };

  const shuffle = () => {
    for (let i = order.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [order[i], order[j]] = [order[j], order[i]];
    }
    render();
  };

  document.getElementById("nextCard")?.addEventListener("click", next);
  document.getElementById("prevCard")?.addEventListener("click", prev);
  document.getElementById("shuffleCards")?.addEventListener("click", shuffle);

  render();
});
