document.addEventListener('DOMContentLoaded', function() {
    // Подсветка активной ссылки в навигации
    const navLinks = document.querySelectorAll('.nav-link');
    const currentUrl = window.location.pathname;
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });
    
    // Анимация при загрузке страницы
    const nav = document.querySelector('nav');
    nav.style.opacity = '0';
    nav.style.transform = 'translateY(-20px)';
    
    setTimeout(() => {
        nav.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        nav.style.opacity = '1';
        nav.style.transform = 'translateY(0)';
    }, 100);
});