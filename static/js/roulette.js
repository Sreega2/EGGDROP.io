document.addEventListener("DOMContentLoaded", function () {
    const roulette = document.querySelector('.roulette-items');
    const resultDiv = document.getElementById('result');
    const resultSkin = document.getElementById('result-skin');
    
    // Нажатие на кнопку "Открыть кейс"
    document.querySelector('#openCaseForm').addEventListener('submit', function (event) {
        event.preventDefault();  // Предотвращаем стандартную отправку формы

        // Запускаем анимацию вращения
        roulette.style.transform = 'translateX(-5000px)';  // Повернем влево на 5000px
        resultDiv.style.display = 'none';  // Скрываем результаты, пока рулетка крутится

        // Через 5 секунд (после остановки анимации) показываем результат
        setTimeout(function () {
            const allItems = document.querySelectorAll('.roulette-item');
            const randomIndex = Math.floor(Math.random() * allItems.length);  // Случайный индекс скина
            const selectedSkin = allItems[randomIndex];

            // Показываем результат (сделаем скин большим)
            resultSkin.innerHTML = `<img src="${selectedSkin.querySelector('img').src}" alt="${selectedSkin.querySelector('p').innerText}"><br>${selectedSkin.querySelector('p').innerText}`;

            // Показываем блок с результатом
            resultDiv.style.display = 'block';
        }, 5000);  // Через 5 секунд
    });
});
