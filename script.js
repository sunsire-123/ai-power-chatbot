async function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    if (!userInput.trim()) return;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p class='user'><b>You:</b> ${userInput}</p>`;
    document.getElementById("userInput").value = "";

    try {
        let response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput })
        });

        let data = await response.json();
        chatBox.innerHTML += `<p class='bot'><b>Bot:</b> ${data.response}</p>`;
    } catch (error) {
        chatBox.innerHTML += `<p class='bot'><b>Bot:</b> Sorry, something went wrong.</p>`;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

// Allow sending messages using "Enter" key
function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

