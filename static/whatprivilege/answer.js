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
    $(next).show();	
    $(result).fadeIn("slow");
    $(skip).hide();
}

$(yes).on('click', function() {
    showResults();
    $(no).prop("disabled",true);
    $(yesno).val("yes");
});


$(no).on('click', function() {
    showResults();
    $(yes).prop("disabled",true);
    $(yesno).val("no");
});
