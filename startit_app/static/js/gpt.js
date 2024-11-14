
document.getElementById('chat-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const userInput = document.getElementById('user-input').value;
    const responseDiv = document.getElementById('response');
    const taskId = 1; // Замените на реальный идентификатор задания

    try {
        // Получаем дополнительные данные из API
        const additionalDataResponse = await fetch(`http://localhost:8000/api/get_additional_data/${taskId}/`);
        const additionalData = await additionalDataResponse.json();

        const modifiedMessage = additionalData.additional_data + userInput;

        const apiKey = 'sk-proj-QJeak1M5jus2lC9d2Ungf-pHWntV7p2a13lY4006ClvN4bMBFmOIknbsYZSKlnLZtrus06-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'; // Замените на ваш API ключ

        const response = await fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                prompt: modifiedMessage,
                max_tokens: 150
            })
        });

        const data = await response.json();
        if (data.choices && data.choices.length > 0) {
            responseDiv.innerText = data.choices[0].text;
        } else {
            console.error('Unexpected response format:', data);
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
});