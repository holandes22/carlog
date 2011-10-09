function load_editor_dialog(){
	$.ajax({
		url: $("#editor_form").attr('action'),
		type: 'POST',
		data:  $("#editor_form").serialize(),
		success: function(data, textStatus, jqXHR){
			if(data == 'saved'){
				$('#editor_dialog').dialog('close');
				reactivateCurrentTreeNode();
				return;
			}
			$('#editor_dialog').html(data);	
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
