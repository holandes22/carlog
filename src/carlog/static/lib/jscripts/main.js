function resize_main_window() {
	var h = $(window).height() - 32;
	$('.limit_height').css({
		'height' : h + 'px',
		'max-height' : h + 'px'
	});
}

$(document).ready(function() {
	$(window).bind('resize', function() {
		resize_main_window();
	});
	resize_main_window();
});

