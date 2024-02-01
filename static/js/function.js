/*console.log("working fine");

$("#commentForm").submit(function(e){
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url: $(this).attr("action"),
        dataType: "json",
        success: function(response){
            console.log("Comment saved");
            var offerSlug = response.offer_slug;
            //$("#reviews-container").html(response.reviews_html);
            //$("#average-rating").text(response.average_rating);
            window.location.href = "/item/" + offerSlug + "/";
        }
    })
})*/

/*$(document).ready(function () {
    // Обработчик события отправки формы
    $("#commentForm").submit(function(e){
        e.preventDefault(); // Предотвращаем стандартное поведение формы

        // Сериализуем данные формы
        var formData = $(this).serialize();

        // Отправляем Ajax-запрос
        $.ajax({
            type: $(this).attr("method"),
            url: $(this).attr("action"),
            data: formData,
            dataType: "json",
            success: function(response){
                console.log("Comment saved");
                var offerSlug = response.offer_slug;

                // Переходим на страницу с товаром
                window.location.href = "/item/" + offerSlug + "/";
            },
            error: function(xhr, status, error) {
                console.error("Error occurred:", error);
            }
        });
    });
});
*/

/*$(document).ready(function () {
    // Обработчик события отправки формы
    $("#commentForm").submit(function(e){
        // Отменяем стандартное поведение отправки формы
        e.preventDefault();

        // Сериализуем данные формы
        var formData = $(this).serialize();

        // Отправляем Ajax-запрос
        $.ajax({
            type: $(this).attr("method"),
            url: "",  // Пустая строка, означающая текущий URL
            data: formData,
            dataType: "json",
            success: function(response){
                console.log("Comment saved");
                // После успешной отправки формы происходит перенаправление на ту же страницу
                window.location.reload(); // Перезагрузка страницы
            },
            error: function(xhr, status, error) {
                console.error("Error occurred:", error);
            }
        });
    });
});*/

$(document).ready(function () {
    $("#reviewForm").on('submit', function (event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            dataType: 'json',
            success: function (data) {
                if (data.bool) {
                    window.location.href = "/store/item/" + data.context.offer_slug + "/";
                } else {
                    console.log("Error");
                }
            }
        });
    });
});
