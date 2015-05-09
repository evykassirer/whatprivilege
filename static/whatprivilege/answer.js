/*
 * Module for defining the behaviour of our answering flow.
 */

var transitionSpeed = 400; // ms

function showResults() {
    $(".bar").show();
    animateBars();
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
