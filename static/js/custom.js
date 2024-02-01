$(document).ready(function () {
    $("#loadMore").on('click', function (){
        var _currentProducts=$(".product-card").length;
        var _limit=$(this).attr('data-limit');
        var _total=$(this).attr('data-total');

        $.ajax({
            url:'/load-more-data',
            data:{
                limit: _limit,
                offset:_currentProducts
            },
            dataType:'json',
            beforeSend:function (){
                $("#loadMore").attr('disabled', true);
                $(".load-more-icon").addClass('fa-spin');
            },
            success:function (res) {
                $("#loadMore").attr('disabled', false);
                $(".load-more-icon").removeClass('fa-spin');

                var _totalShowing=$(".product-box").length;
                if(_totalShowing==_total){
                    $("#loadMore").remove();
                }
            }
        });

    });
});