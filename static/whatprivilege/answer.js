var transitionSpeed = 400; // ms

function showResults() {
    $(".bar").show();
    $(".fill").animate({
      width: '100%',
    }, 500, function () {});

    $(".bar").each(function(i) {
      $(this).animate({
        width: $(this).data('percentYes').toString() + '%',
      //borderWidth: 30,
      //marginLeft: '33%',
        }, 500, function() {
        // Animation complete.
        });});
    $(qform).show();
    $(next).show();
    $(step2).show();
    $(".result").fadeIn("slow");
    $(step1).removeClass('highlight');
    $(skip).hide();
}

$(yes).on('click', function() {
    showResults();
    $(no).hide(transitionSpeed);
    $(no).prop("disabled",true);
    $(yesno).val("yes");
});


$(no).on('click', function() {
    showResults();
    $(yes).hide(transitionSpeed);
    $(yes).prop("disabled",true);
    $(yesno).val("no");
});
