/*
 * Module containing functions related to result bars.
 */

function animateBars() {
    $(".fill").animate({
      width: '100%',
    }, 500, function () {});

    $(".bar").each(function(i) {
      $(this).animate({
        width: $(this).data('percentNo').toString() + '%',
        }, 500, function() {
        // Animation complete.
        });
    });
}
