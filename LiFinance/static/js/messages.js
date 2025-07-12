document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        let messages = document.querySelectorAll('.messages li');
        messages.forEach(function(message) {
            message.style.opacity = '0';
            setTimeout(function() {
                message.style.display = 'none';
            }, 300);
        });
    }, 5000); // Сообщения исчезнут через 5 секунд
});