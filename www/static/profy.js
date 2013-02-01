$(document).ready(function(){
	$('#cmd').change(function(){
		$('#cmdcontents').attr('src', '/cmd/' + $('#cmd').val());
	});
	$('#logfile').change(function(){
		$('#logcontents').attr('src', '/log/' + $('#logfile').val());
	});
});
