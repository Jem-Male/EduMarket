const express = require('express');
const axios = require('axios');
const app = express();

app.use(express.json());

app.post('/send', async (req, res) => {
    const userMessage = req.body.message;
    const additionalData = "Задание: ";
    const modifiedMessage = additionalData + userMessage;

    try {
        const response = await sendToAnotherSite(modifiedMessage);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Ошибка при отправке сообщения' });
    }
});

async function sendToAnotherSite(message) {
    const url = 'https://example.com/api';
    const data = { message: message };
    return await axios.post(url, data);
}

app.listen(3000, () => {
    console.log('Сервер запущен на порту 3000');
});
