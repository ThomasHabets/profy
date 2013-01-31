$(document).ready(function(){
	$('#logfile').change(function(){
		$('#logcontents').attr('src', '/log/' + $('#logfile').val());
	});
});
