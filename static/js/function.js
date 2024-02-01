/*$(document).ready(function () {
    $("#commentForm").on('submit', function (event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            dataType: 'json',
            success: function (data) {
                if (data.success) {
                    $("#reviews-container").append(data.review_html);
                    $("#averag-rating").text(data.average_rating);
                } else {
                    console.log("Error");
                }
            }
        });
    });
});*/

$(document).ready(function () {
    $("#commentForm").on('submit', function (event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            url: redirect_url,
            type: 'POST',
            data: formData,
            dataType: 'json',
            success: function (data) {
                if (data.success) {
                    window.location.href = data.redirect_url;
                } else {
                    console.log("Error");
                }
            }
        });
    });
});

