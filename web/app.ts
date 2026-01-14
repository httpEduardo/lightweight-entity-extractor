const results = document.getElementById("results") as HTMLDivElement;
const extractButton = document.getElementById("extractButton") as HTMLButtonElement;

function renderEntities(entities: Record<string, string[]>): void {
  results.innerHTML = "";
  Object.entries(entities).forEach(([key, values]) => {
    const card = document.createElement("div");
    card.className = "result-card";
    const list = values.length ? values.join(", ") : "None";
    card.textContent = `${key}: ${list}`;
    results.appendChild(card);
  });
}

extractButton.addEventListener("click", () => {
  const text = (document.getElementById("textInput") as HTMLTextAreaElement).value;
  fetch("/api/extract", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  })
    .then((res) => res.json())
    .then((data) => renderEntities(data.entities || {}));
});
