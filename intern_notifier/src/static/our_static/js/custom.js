$(document).ready(function(){

	$("#id_profileimage").addClass("btn btn-default");
//img-image-profile


	$("input:checkbox.checkbox").change(function(){
		var val = $(this).val();
		var total=$('form input[type=checkbox]:checked').size();
		if(total == 0){
			$(this).prop('checked', true);
			$("#alert").append("<b>Atleast one domain is required</b>");
		}else{
			$.ajax({
				type: 'POST',
				url :'/',
				data: {
					value: val,
					csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
				},
				success: function(){
					window.location = window.location.href;
				}
			});
		}
	});
});