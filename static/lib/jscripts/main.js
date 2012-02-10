function resizeMainWindow() {
	var h = $(window).height() - 36;
	$('.limit_height').css({
		'height' : h + 'px',
		'max-height' : h + 'px'
	});
}

function resizeTreatmentDetailsGridSize(){
	var ww = $(window).width();
  	var wh = $(window).height();
	$("#treatment_details_grid").setGridWidth($(window).width() - 450, true);
	$("#treatment_details_grid").setGridHeight($(window).height() - 200, true);  	  	
}

function genericLoadDialog(form_selector, dialog_selector, onSuccessHandler, matchString){
	$.ajax({
		url: $(form_selector).attr('action'),
		type: 'POST',
		data:  $(form_selector).serialize(),
		success: function(data, textStatus, jqXHR){
			if(data.match(matchString)){
				$(dialog_selector).dialog('close');
				if(onSuccessHandler && typeof onSuccessHandler == 'function'){
					onSuccessHandler();
				}
				return;
			}
			//We got errors
			$(dialog_selector).html(data);
			$('.field_error').effect("highlight", { times: 3 }, 1200);
		},
	})
	
}

$(document).ready(function() {
	$(window).bind('resize', function() {
		resizeMainWindow();
	});
	resizeMainWindow();
	resizeTreatmentDetailsGridSize();
	
	$( "#editor_dialog" ).dialog({
		autoOpen: false,
		width: 'auto',
		resizable: false,
		buttons: {
			Save: function() {
				genericLoadDialog("#editor_form", this, reactivateCurrentTreeNode, "saved");	
			},
			Cancel: function() {
				$( this ).dialog( "close" );
			},
			
		}
	});
	
	
});

