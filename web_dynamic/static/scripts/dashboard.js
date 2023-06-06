$(document).ready(function() {
    $('#create-customer-link').click(function(e) {
        e.preventDefault();
	$('#customer-form-overlay').show();
    });

    $('#cancel-customer').click(function() {
        $('#customer-form-overlay').hide();
    });
});
