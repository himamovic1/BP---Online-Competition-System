$(function() {
	$("#competition-search-query").on("keyup", function(e) {
		if(e.which == 13)
			$("#competition-search").trigger("click");
	});

	$("#competition-search").on("click", function() {
		let search_query = $("#competition-search-query").val();

		if(search_query.length === 0)
			return;

		let page_base = window.location.protocol + "//" + window.location.host + "/";

		$.get(page_base + "api/search/competition/" + search_query, function(data) {
			let results_table = $("#datatable-buttons > tbody");
			results_table.empty();

			$.each(data, function(i, e) {
				let extra_opts = '<div class="btn-group"><button type="button" class="btn btn-danger">Opcije</button><button type="button" class="btn btn-danger dropdown-toggle" data-toggle="dropdown" aria-expanded="false"><span class="caret"></span><span class="sr-only">Toggle Dropdown</span></button><ul class="dropdown-menu" role="menu"><li><a href="/competition/delete/'+ e.name + '/' + e.date + '">Obriši</a></li><li><a href="/competition/delete/' + e.name + '/' + e.date + '">Promijeni</a></li></ul></div>';
				results_table.append("<tr><td>" + e.name + "</td><td>" + e.field + "</td><td>" + e.date + "</td><td>" + extra_opts + "</td></tr>");
			});
		});
	});
});