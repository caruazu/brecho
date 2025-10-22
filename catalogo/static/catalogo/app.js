// util: pegar CSRF do cookie (Django padrão)
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return decodeURIComponent(parts.pop().split(";").shift());
  return "";
}
const csrftoken = getCookie("csrftoken");

// toast helper
function showToast(message, variant = "primary") {
  const toastEl = document.getElementById("liveToast");
  if (!toastEl) return alert(message);
  toastEl.className = `toast align-items-center text-bg-${variant} border-0`;
  toastEl.querySelector(".toast-body").textContent = message;
  const t = bootstrap.Toast.getOrCreateInstance(toastEl);
  t.show();
}

// delegação de eventos para os botões "Alternar"
document.addEventListener("click", async (e) => {
  const btn = e.target.closest(".btn-toggle");
  if (!btn) return;

  const id = btn.getAttribute("data-item-id");
  if (!id) return;

  btn.disabled = true;
  const row = btn.closest("tr");

  try {
    const resp = await fetch(`/api/items/${id}/toggle/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrftoken,
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
      },
      body: "{}",
    });

    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();

    // Atualiza o badge na linha
    const badge = row.querySelector(".badge");
    if (badge) {
      const disponivel = Boolean(data.disponivel);
      badge.textContent = disponivel ? "Disponível" : "Indisponível";
      badge.classList.toggle("text-bg-success", disponivel);
      badge.classList.toggle("text-bg-secondary", !disponivel);
    }

    showToast("Status atualizado!", "success");
  } catch (err) {
    console.error(err);
    showToast("Falha ao atualizar. Tente novamente.", "danger");
  } finally {
    btn.disabled = false;
  }
});
