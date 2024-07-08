document.addEventListener('DOMContentLoaded', () => {
    const popup = document.getElementById('popup');
    const openPopupBtn = document.getElementById('openPopupBtn');
    const closeBtn = document.querySelector('.close');
    const yesBtn = document.getElementById('yesBtn');
    const noBtn = document.getElementById('noBtn');

    openPopupBtn.onclick = function() {
        popup.style.display = 'block';
    }

    closeBtn.onclick = function() {
        popup.style.display = 'none';
    }

    yesBtn.onclick = function() {
        window.location.href = 'Templates/faz.html'; // Caminho relativo para a página local
    }

    noBtn.onclick = function() {
        popup.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    }
});