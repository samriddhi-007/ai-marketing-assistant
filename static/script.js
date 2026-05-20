async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const userMessage = input.value;

    if (!userMessage) return;

    chatBox.innerHTML += `
        <p><strong>You:</strong> ${userMessage}</p>
    `;

    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userMessage
        })
    });

    const data = await response.json();

    chatBox.innerHTML += `
        <p><strong>Bot:</strong> ${data.reply}</p>
    `;
}