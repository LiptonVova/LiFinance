document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const password1 = document.getElementById('id_password1');
    const password2 = document.getElementById('id_password2');
    
    // Анимация появления формы
    form.style.opacity = '0';
    form.style.transform = 'translateY(20px)';
    
    setTimeout(() => {
        form.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        form.style.opacity = '1';
        form.style.transform = 'translateY(0)';
    }, 200);
    
    // Валидация паролей
    function validatePassword() {
        if (password1.value !== password2.value) {
            password2.setCustomValidity('Пароли не совпадают');
            password2.style.borderColor = '#e63946';
        } else {
            password2.setCustomValidity('');
            password2.style.borderColor = '#ddd';
        }
    }
    
    password1.addEventListener('input', validatePassword);
    password2.addEventListener('input', validatePassword);
    
    // Подсветка сложности пароля
    password1.addEventListener('input', function() {
        const strength = calculatePasswordStrength(this.value);
        const hint = this.parentNode.querySelector('.password-hint');
        
        if (this.value.length === 0) {
            hint.textContent = 'Ваш пароль должен содержать как минимум 8 символов.';
            hint.style.color = '#6c757d';
        } else if (strength < 2) {
            hint.textContent = 'Слабый пароль';
            hint.style.color = '#e63946';
        } else if (strength < 4) {
            hint.textContent = 'Средний пароль';
            hint.style.color = '#f4a261';
        } else {
            hint.textContent = 'Сильный пароль';
            hint.style.color = '#2a9d8f';
        }
    });
    
    function calculatePasswordStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength++;
        if (password.match(/[a-z]/)) strength++;
        if (password.match(/[A-Z]/)) strength++;
        if (password.match(/[0-9]/)) strength++;
        if (password.match(/[^a-zA-Z0-9]/)) strength++;
        return strength;
    }
    
    // Валидация перед отправкой
    form.addEventListener('submit', function(e) {
        let isValid = true;
        const inputs = form.querySelectorAll('input[type="text"], input[type="password"]');
        
        inputs.forEach(input => {
            if (!input.value.trim()) {
                input.style.borderColor = '#e63946';
                isValid = false;
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            
            setTimeout(() => {
                inputs.forEach(input => {
                    input.style.borderColor = '#ddd';
                });
            }, 2000);
        }
    });
});