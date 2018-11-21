$(document).ready(function () {
    $('.starreview').click(function() {
        var starnum = $(this).data('cd-starnum');

        $('.starreview').each(function(index) {
            if((index + 1) <= starnum) {
                $(this).removeClass('btn-default btn-grey').addClass('btn-warning');
            } else {
                $(this).removeClass('btn-warning').addClass('btn-warning btn-default btn-grey');
            }
        });

        $('#starreviewInput').val(starnum);
    });
})