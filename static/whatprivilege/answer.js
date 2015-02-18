var transitionSpeed = 400; // ms

function showResults() {
    var percentYes = $(result).data('percentYes');
    $(bar).show();
    $(fill).animate({
      width: '100%',
    }, 500, function () {});
    $(bar).animate({
      width: percentYes.toString() + '%',
      //borderWidth: 30,
      //marginLeft: '33%',
      }, 500, function() {
        // Animation complete.
      });
    $(qform).show();
    $(next).show();
    $(step2).show();
    $(result).fadeIn("slow");
    $(step1).removeClass('highlight');
    $(skip).hide();
    workshopResults();
}

function workshopResults() {
    if ($("#bar2").length == 0) return;
    var percentYes = $(result2).data('percentYes');
    $(bar2).show();
    $(fill2).animate({
      width: '100%',
    }, 500, function () {});
    $(bar2).animate({
      width: percentYes.toString() + '%',
      //borderWidth: 30,
      //marginLeft: '33%',
      }, 500, function() {
        // Animation complete.
      });
    $(result2).fadeIn("slow");
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
