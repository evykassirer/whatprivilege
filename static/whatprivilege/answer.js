$(yes).on('click', function() {
	$(no).prop("disabled",true);
	$(next).show();	
	$(yesno).val("yes");
	$(skip).hide();
});


$(no).on('click', function() {
	$(yes).prop("disabled",true);
	$(next).show();	
	$(yesno).val("no");
	$(skip).hide();
});