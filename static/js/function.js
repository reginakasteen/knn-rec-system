console.log("working fine");

$("#commentForm").submit(function(e){
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url: $(this).attr("action"),
        dataType: "json",
        success: function(response){
            console.log("Comment saved");
            //$("#reviews-container").html(response.reviews_html);
            //$("#average-rating").text(response.average_rating);
            window.location.href = "/item/" + response.offer_slug + "/";
        }
    })
})