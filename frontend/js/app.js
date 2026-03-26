const API_BASE = "http://127.0.0.1:8000";

async function postData(endpoint, payload) {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Erro ao enviar dados.");
        }

        alert("Registro salvo com sucesso.");
        return data;
    } catch (error) {
        alert("Erro: " + error.message);
        console.error(error);
    }
}

async function getData(endpoint) {
    try {
        const response = await fetch(`${API_BASE}${endpoint}`);
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Erro ao buscar dados.");
        }

        return data;
    } catch (error) {
        alert("Erro: " + error.message);
        console.error(error);
        return null;
    }
}

function preencherTabela(tbodyId, linhas, colunas) {
    const tbody = document.getElementById(tbodyId);
    if (!tbody) return;

    tbody.innerHTML = "";

    linhas.forEach(item => {
        const tr = document.createElement("tr");

        colunas.forEach(coluna => {
            const td = document.createElement("td");
            td.textContent = item[coluna] ?? "-";
            tr.appendChild(td);
        });

        tbody.appendChild(tr);
    });
}