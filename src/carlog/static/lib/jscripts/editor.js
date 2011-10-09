function load_editor_dialog(){
	
	$.ajax({
		url: $("#editor_form").attr('action'),
		type: 'POST',
		data:  $("#editor_form").serialize(),
		success: function(data, textStatus, jqXHR){
			$('#editor_dialog').html(data).dialog('close').dialog('open');
		},
	})
	
}

$(document).ready(function() {
	$( "#editor_dialog" ).dialog({
		autoOpen: false,
		buttons: {
			Save: load_editor_dialog,
			Cancel: function() {
				$( this ).dialog( "close" );
			},
			
		}
	});
});
