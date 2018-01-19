$(function(){	
	//Date picker
	$('#id_fecha_nacimiento').datepicker({
	  autoclose: true
	});


	$('#filtro').keyup(function(){
		$.ajax({
			url: $("#form-paciente-filter").attr("action"),
			data: $("#form-paciente-filter").serialize(),
			success: function(data){
				var html = $(data).find("#paciente-list").html();
				$("#paciente-list").html(html);
			}
		});
	})
});