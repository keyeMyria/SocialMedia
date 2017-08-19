
	jQuery(function(){
	window.randomColor="red";

	$("*").click(function(event) {
	/*if (self !== top ){*/
		$("*").removeAttr("selected_for_scrp").removeAttr("css","border:2px solid "+randomColor)
	    var text = ($(event.target).attr("selected_for_scrp","active"));

	window.randomColor= "#" + Math.floor(Math.random() * 0xFFFFFF).toString(16);
	$("*[selected_for_scrp]").css("border","2px solid "+randomColor)
	}/*}*/);

	})