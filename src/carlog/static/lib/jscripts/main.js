function resizeMainWindow() {
	var h = $(window).height() - 36;
	$('.limit_height').css({
		'height' : h + 'px',
		'max-height' : h + 'px'
	});
}


$(document).ready(function() {
	$(window).bind('resize', function() {
		resizeMainWindow();
	});
	resizeMainWindow();
});

