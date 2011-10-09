function reload_editor_dialog () {
  	$.ajax({
		url: '/entries/car/editor/',
		success: function(data, textStatus, jqXHR){
			$('#editor_dialog').load('/entries/car/editor/');
			$( "#editor_dialog" ).open();
		},
		error: function(jqXHR, textStatus, errorThrown){
			$( "#editor_dialog" ).open();
		},
	});
}

$(document).ready(function(){
	$( "#editor_dialog" ).dialog(
		{
			autoOpen: false,
			show: "blind",
			hide: "explode"
		}
	);
	
	$("#add_car_button").click(reload_editor_dialog);
})