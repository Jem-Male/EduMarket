function checkAnswer() {
    const userInput = document.getElementById('userInput').value.trim();
    const correctAnswer = 'здесь должны появлятся данные с базы данных';

    if (userInput === correctAnswer) {
        document.getElementById('result').innerText = 'Правильно!';
        document.getElementById('result').style.color = 'green';
    } else {
        document.getElementById('result').innerText = 'Неправильно. Попробуйте еще раз.';
        document.getElementById('result').style.color = 'red';
    }
}