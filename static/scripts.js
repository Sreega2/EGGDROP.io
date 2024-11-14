document.addEventListener("DOMContentLoaded", function() {
    const rouletteInner = document.querySelector(".roulette-inner");
    
    setTimeout(function() {
        rouletteInner.style.transform = "translateX(-200%)";  // Начать движение рулетки
    }, 100);

    setTimeout(function() {
        rouletteInner.style.transform = "translateX(0%)";  // Остановить рулетку на случайном скине
    }, 3000);  // Пауза в 3 секунды перед остановкой
});
