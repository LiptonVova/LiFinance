$(document).ready(function() {
    // Если есть начальные данные, создаем формы для них
    if (initialItems && initialItems.length > 0) {
        initialItems.forEach(item => {
            const newItem = $('#item-template').children().first().clone();
            newItem.find('.item-name').val(item.name);
            newItem.find('.item-quantity').val(item.quantity);
            newItem.find('.item-price').val(item.price);
            $('#items-container').append(newItem);
            newItem.show();
        });
        updateItemsData();
    } 

    // Добавление новой позиции
    $('#add-item-btn').click(function() {
        // Проверяем, все ли предыдущие формы заполнены
        let allValid = true;
        const $forms = $('.item-form');
        
        // Проверяем все формы, кроме последней (новой, которая может быть пустой)
        $forms.slice(0, -1).each(function() {
            const $form = $(this);
            if (!$form.find('.item-name').val() || 
                !$form.find('.item-quantity').val() || 
                !$form.find('.item-price').val()) {
                allValid = false;
                return false; // Выходим из цикла
            }
        });

        if (!allValid) {
            alert('Заполните все поля текущей позиции перед добавлением новой');
            return;
        }

        // Добавляем новую форму
        addNewItemForm();
    });

    // Удаление позиции
    $(document).on('click', '.remove-item-btn', function() {
        $(this).closest('.item-form').remove();
        updateItemsData();
    });

    // Обновление данных при изменении полей
    $(document).on('input', '.item-name, .item-quantity, .item-price', function() {
        updateItemsData();
    });

    // Перед отправкой формы обновляем hidden поле
    $('#transaction-form').submit(function(e) {
        updateItemsData();
        return true;
    });

    // Функция для добавления новой формы
    function addNewItemForm() {
        const newItem = $('#item-template').children().first().clone();
        $('#items-container').append(newItem);
        newItem.show();
        updateItemsData();
    }

    // Функция для обновления скрытого поля с данными
    function updateItemsData() {
        const items = [];
        $('.item-form').each(function() {
            const $form = $(this);
            const name = $form.find('.item-name').val();
            const quantity = $form.find('.item-quantity').val();
            const price = $form.find('.item-price').val();

            // Добавляем в массив только заполненные формы
            if (name && quantity && price) {
                items.push({
                    name: name,
                    quantity: quantity,
                    price: price
                });
            }
        });
        $('#items-data').val(JSON.stringify(items));
    }
});