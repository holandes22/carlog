function loadEditorDialog(){
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
			//We got errors
			$('#editor_dialog').html(data);
			$('.field_error').effect("highlight", { times: 3 }, 1200);
		},
	})
	
}

$(document).ready(function() {
	$( "#editor_dialog" ).dialog({
		autoOpen: false,
		width: 'auto',
		buttons: {
			Save: loadEditorDialog,
			Cancel: function() {
				$( this ).dialog( "close" );
			},
			
		}
	});
});
