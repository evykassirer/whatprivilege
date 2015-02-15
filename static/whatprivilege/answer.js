function showResults() {
    $(bar).show();
    $(bar).animate({
      width: 75,
      borderWidth: 225,
      }, 500, function() {
        // Animation complete.
      });
    $(next).show();	
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
