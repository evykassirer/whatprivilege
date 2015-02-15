function showResults() {
    $(bar).show();
    $(fill).animate({
      width: '100%',
    }, 500, function () {});
    $(bar).animate({
      width: '70%',
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
