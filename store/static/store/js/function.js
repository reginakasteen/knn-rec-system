$(document).ready(function () {
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
                    console.log("OK");
                    window.location.href = data.redirect_url;
                } else {
                    console.log("Error");
                }
            }
        });
    });
});

