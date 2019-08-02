$(document).ready(function() {
		
		/*Datatables	
		var table = $('#datatablesNo2').DataTable({
			searching: false,
			paging: false,
			info: false,
      columnDefs: [{
         targets: 0,
         searching: false,
         orderable: false,
         className: 'select-checkbox',
         render: function (data, type, full, meta){
             return '<input type="checkbox" name="id[]" value="' + $('<div/>').text(data).html() + '">';
         }
      }],
      order: [[1, 'asc']],
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

   // Handle click on "Select all" control
   $('#datatablesNo2-select-all').on('click', function(){
      // Get all rows with search applied
      var rows = table.rows({ 'search': 'applied' }).nodes();
      // Check/uncheck checkboxes for all rows in the table
      $('input[type="checkbox"]', rows).prop('checked', this.checked);
   });

   // Handle click on checkbox to set state of "Select all" control
   $('#datatablesNo2 tbody').on('change', 'input[type="checkbox"]', function(){
      // If checkbox is not checked
      if(!this.checked){
         var el = $('#datatablesNo2-select-all').get(0);
         // If "Select all" control is checked and has 'indeterminate' property
         if(el && el.checked && ('indeterminate' in el)){
            // Set visual state of "Select all" control
            // as 'indeterminate'
            el.indeterminate = true;
         }
      }
   });

   // Handle form submission event
  $('#frm-datatablesNo2').on('submit', function(e){
      var form = this;

      // Iterate over all checkboxes in the table
      table.$('input[type="checkbox"]').each(function(){
         // If checkbox doesn't exist in DOM
         if(!$.contains(document, this)){
            // If checkbox is checked
            if(this.checked){
               // Create a hidden element 
               $(form).append(
                  $('<input>')
                     .attr('type', 'hidden')
                     .attr('name', this.name)
                     .val(this.value)
               );
            }
         } 
      });

      // FOR TESTING ONLY
      
      // Output form data to a console
      $('#datatablesNo2-console').text($(form).serialize()); 
      console.log("Form submission", $(form).serialize()); 
       
      // Prevent actual form submission
      e.preventDefault();
   });*/
	
	
	/*Datatable con checbox pra estudiantes*/
	$table = $('#example').DataTable( {
			searching: false,
			paging: false,
			info: false,
			columnDefs: [
				 {
						orderable: false,
						targets: 0,
						checkboxes: {
							 selectRow: true
						}
				 }
			],
			select: {
					style:    'multi'
			},

			order: [[ 1, 'asc' ]],
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
							
					}

	});
	
	
		var csrftoken = $('input[name = csrfmiddlewaretoken]').val();
		function csrfSafeMethod(method) {
				// these HTTP methods do not require CSRF protection
				return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		$.ajaxSetup({
				beforeSend: function(xhr, settings) {
						if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
								xhr.setRequestHeader("X-CSRFToken", csrftoken);
						}
				}
		});
/*
		$("#form" ).on('submit', function( event ){
			
			
			var dato = $( this );
			/*alert( dato['id_foraneaCurso'] );
			*/
			event.preventDefault();
			
			//alert(dato.data('post-url'))
			var selectedRows = $table.rows({ selected: true }).data();
			//alert(selectedRows.length)
			/*$.each(selectedRows, function(index, value){ 
				console.log(value);
			});*
			
			// Datos Envio Ajax 
			
			var URL = dato[0].action;
			//csrfmiddlewaretoken r2b1CMAeRhDqh2HjjMnCBWpNnK6Subz8pwtxn8oFckqImlD8bmSC2eDmknZPnF4k
			//console.log(Token);
			
			var datos = new FormData(this);
			datos.append("tabla", selectedRows);
			$.ajax({
				url: URL,
				type: "POST",
				data:datos,
				processData:false,
				contentType:false,
				success: function(datos){
					
				},
				
			});
			
		/**
		});
	
	
	/**/
	
	
});
