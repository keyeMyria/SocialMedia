
$("#pic").ready($.post( "/inner/pic_im1",{"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value},function( data ) {
        $("#pic").attr("src",data)
        $(".po").attr("src",data)
        $(".po").attr("width","80")  
        $(".po").attr("height","100")  

    }));


	$("#op").click(function(){
			if ($("#pt").val()!=""){
		$.post( "/inner/post/poste",{"pp":$("#pt").val(),"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value}, function( data ) {	
			if (data=="200"){
				alert("you should connect first");
			}
			else if(data=="100"){
				$.post( "/inner/pic_im1",{"id":$("#id_user").val()},function( da ) {

          a=$("<div id='t'  class='po' style='padding-top:400px' id='container'></div>");          
          c=$("<div></div>").append("<img src="+da+" width='80' height='80'>");
          d=$("<div></div>").append("<h3>"+$("#id_user").attr("name")+"</h3>"+"<p>"+$("#pt").val()+"</p>");
          $("#t").attr("style","");


          a.append(c,d);
					$("#wall").prepend(a);
					$("#pt").val("");
					$("#t").attr("style","padding-top:400px");
				})
			}
			else{
				alert(data);			}
		return false;
		});}});

	$("#new").click(function(e){
        $("#myModal2").attr("style","display:block");
	});




      


// If an event gets to the body


// Prevent events from getting pass .popup
$("#tb").click(function(e){
  e.stopPropagation();
});

//close button
$('#close').click(function(e){
  $("#myModal2").css("display","None");

});
	$("#iframe_a").click(function(e){
	$("#iframe_a").attr("href",$("#url_fetch").val());
	});

$("#url-send").click(function(){
		$("#loads").css("display","block");
	$.post("/inner/post/load_site",{"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value,"url":$("#url").val()},function(data){
		$("#loads").css("display","none");
		if (data.slice(0,2)=="100"){
			$("#result_site").text("something went wrong try again");
		}
		else{
			$("#result_site").text("choose your element");
			//$("#printer").append();
		}
		$(function() {
	var $frame = $('<iframe style="width:100%; height0px;">');
	$('#printer').html( $frame );
	setTimeout( function() {
		var jq  ='<scr' + 'ipt src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></scr' + 'ipt>';
		var d   =jq+"<script>$(document).ready(function(){$(this).click(function(e){console.log($(e.toElement).attr('style','border:5px solid #ff0500'))});})</script>	";
		var doc = $frame[0].contentWindow.document;
		var $body = $('body',doc);
		var $head = $('head',doc);
		$body.html(data.slice(3,data.length-1));
		$head.html(d+$head.html);

	}, 1 );
});


	});
	});

/**
$("#inputs").onsubmit(
	$("#inputs").value

	);**/

