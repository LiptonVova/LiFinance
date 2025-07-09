document.addEventListener('DOMContentLoaded', function() {

    const form = document.getElementById('myForm');

    const inputContainer = document.getElementById('inputContainer');

    const addButton = document.getElementById('addInput');

    addButton.addEventListener('click', function() {

    const newInput = document.createElement('input');

        newInput.type = 'text';

        inputContainer.appendChild(newInput);

    });

    form.addEventListener('submit', function(event) {

        event.preventDefault(); // Предотвращаем отправку

        // Здесь можно обработать отправку данных

    });

});