document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const inputs = form.querySelectorAll('input[type="text"], input[type="password"]');
    
    // Анимация появления формы
    form.style.opacity = '0';
    form.style.transform = 'translateY(20px)';
    
    setTimeout(() => {
        form.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        form.style.opacity = '1';
        form.style.transform = 'translateY(0)';
    }, 200);
    
    // Подсветка активного поля ввода
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentNode.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentNode.classList.remove('focused');
        });
    });
    
    // Валидация перед отправкой
    form.addEventListener('submit', function(e) {
        let isValid = true;
        
        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.style.borderColor = '#e63946';
                isValid = false;
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            
            // Сброс подсветки через 2 секунды
            setTimeout(() => {
                inputs.forEach(input => {
                    input.style.borderColor = '#ddd';
                });
            }, 2000);
        }
    });
});