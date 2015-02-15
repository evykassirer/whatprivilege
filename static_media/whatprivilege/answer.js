$(yes).on('click', function() {
	$(no).prop("disabled",true);
	$(next).show();	
	$(yesno).val("yes");
});


$(no).on('click', function() {
	$(yes).prop("disabled",true);
	$(next).show();	
	$(yesno).val("no");
});