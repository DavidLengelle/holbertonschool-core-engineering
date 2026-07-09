const socket = new WebSocket("ws://localhost:8000/ws");

const form = document.getElementById("chat-form");
const input = document.getElementById("input");
const messages = document.getElementById("messages");
const status = document.getElementById("status");


function addMessage(text, type) {
    const li = document.createElement("li");
    li.textContent = text;
    li.className = type;
    messages.appendChild(li);
}


socket.onopen = () => {
    status.textContent = "Connecte";
};


socket.onclose = () => {
    status.textContent = "Deconnecte";
};


socket.onmessage = (event) => {
    addMessage(event.data, "received");
};


form.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = input.value;
    socket.send(text);
    addMessage(text, "sent");
    input.value = "";
});
