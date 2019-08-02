



$(document).ready(function() {
		
		// Initialización

		// SideNav Initialization
		$(".button-collapse").sideNav();

		// Material Select Initialization
		$('.mdb-select').material_select();
		

		// Data Picker Initialization
		$('.datepicker').pickadate();

		// Tooltip Initialization
		$('[data-toggle="tooltip"]').tooltip()
		
		var container = document.querySelector('.custom-scrollbar');
		Ps.initialize(container, {
				wheelSpeed: 2,
				wheelPropagation: true,
				minScrollbarLength: 20
		});

	
		/*Datatables*/
		var $table =  $('#datatables');
		$table.DataTable( {
			
        language: {
							"sProcessing":     "Procesando...",
							"sLengthMenu":     "Mostrar _MENU_ registros",
							"sZeroRecords":    "No se encontraron resultados",
							"sEmptyTable":     "Ningún dato disponible en esta tabla",
							"sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
							"sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
							"sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
							"sInfoPostFix":    "",
							"sSearch":         "Buscar:",
							"sUrl":            "",
							"sInfoThousands":  ",",
							"sLoadingRecords": "Cargando...",
							"oPaginate": {
									"sFirst":    "Primero",
									"sLast":     "Último",
									"sNext":     "Siguiente",
									"sPrevious": "Anterior"
							},
							"oAria": {
									"sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
									"sSortDescending": ": Activar para ordenar la columna de manera descendente"
							}
					}
    });
	

	
		// Material Select Initialization
		$('select[name="datatables_length"]').material_select();
		
		$('#datatables_length > label > div.form-control').removeClass("form-control");
	
		// TinyMCE Initialization
		tinymce.init({ 
			selector:'#id_descripcionTarea', 
			menubar: false, 
			height : "200",
			language: 'es',
			themes: "modern",
			setup: function (editor) {
        editor.on('change', function (e) {
            editor.save();
        });
				editor.getElement().removeAttribute('required');
    	}
		});
		
		//Inicializacón Calendario
		$('#datetimepicker1').datetimepicker({
			langage:'es',
			minDate:moment(),
			icons: {
				time: 'fa fa-clock-o indigo-text',
				date: 'fa fa-calendar indigo-text',
				up: 'fa fa-arrow-up indigo-text',
				down: 'fa fa-arrow-down indigo-text',
				previous: 'fa fa-chevron-left indigo-text',
				next: 'fa fa-chevron-right indigo-text',
				today: 'fa fa-calendar-check-o indigo-text',
				clear: 'fa fa-trash indigo-text ',
				close: 'fa fa-times indigo-text'
			}
		});

});
