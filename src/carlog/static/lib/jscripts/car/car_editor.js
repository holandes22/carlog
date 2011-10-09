function load_editor_dialog(){
	
	$.ajax({
		url: $("#car_editor_form").attr('action'),
		type: 'POST',
		data:  $("#car_editor_form").serialize(),
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
	$('#editor_dialog_button').click(
		function(){
			$('#editor_dialog').load('/entries/car/editor/').dialog('open');	
		}
		
		);
});
