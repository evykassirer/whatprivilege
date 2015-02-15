$(yes).on('click', function() {
	$(no).prop("disabled",true);
	$(next).show();	
	$(yesno).val("yes");
	$(skip).hide();
	$(bar).show();
});


$(no).on('click', function() {
	$(yes).prop("disabled",true);
	$(next).show();	
	$(yesno).val("no");
	$(skip).hide();
	$(bar).show();
});