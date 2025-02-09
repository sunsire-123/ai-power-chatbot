require("dotenv").config();
const express = require("express");
const cors = require("cors");
const { Configuration, OpenAIApi } = require("openai");

const app = express();
app.use(cors());
app.use(express.json());

// OpenAI API Configuration
const openai = new OpenAIApi(
    new Configuration({ apiKey: process.env.OPENAI_API_KEY })
);

// Chatbot API Endpoint
app.post("/chat", async (req, res) => {
    try {
        const userMessage = req.body.message;

        // Send user message to OpenAI
        const response = await openai.createChatCompletion({
            model: "gpt-3.5-turbo", // Use "gpt-4" for better results
            messages: [{ role: "system", content: "You are an AI assistant." }, { role: "user", content: userMessage }],
        });

        res.json({ reply: response.data.choices[0].message.content });
    } catch (error) {
        console.error("OpenAI Error:", error);
        res.status(500).json({ reply: "Sorry, I encountered an error." });
    }
});

// Start Server
const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
