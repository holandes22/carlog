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


$(document).ready(function() {
	$(window).bind('resize', function() {
		resizeMainWindow();
	});
	resizeMainWindow();
	resizeTreatmentDetailsGridSize();
});

