var transitionSpeed = 400; // ms

function showResults() {
    $(".bar").show();
    $(".fill").animate({
      width: '100%',
    }, 500, function () {});

    $(".bar").each(function(i) {
      $(this).animate({
        width: $(this).data('percentYes').toString() + '%',
        }, 500, function() {
        // Animation complete.
        });});
    $(step2).show();
    $(".result").fadeIn("slow");
    $(step1).removeClass('highlight');
    $(skip).hide();
}

$(yes).on('click', function( event ) {
    showResults();
    $(no).hide(transitionSpeed);
    $(no).prop("disabled",true);
    $(yesno).val("yes");
    event.preventDefault()
});


$(no).on('click', function( event ) {
    showResults();
    $(yes).hide(transitionSpeed);
    $(yes).prop("disabled",true);
    $(yesno).val("no");
    event.preventDefault()
});
