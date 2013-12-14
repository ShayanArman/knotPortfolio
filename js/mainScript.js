$(document).ready(function() {
	var pathname = window.location.pathname;
	var pathArray = pathname.split("/")
	pathname = pathArray[1]

	$("#"+pathname).css("color","#4099FF"); // thanks ruoping.
});