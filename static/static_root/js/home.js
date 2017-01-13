$("#pic").ready($.post( "http://127.0.0.1:8000/inner/pic_im1",function( data ) {
        $("#pic").attr("src",data)
        $(".po").attr("src",data)
        $(".po").attr("width","80")  
        $(".po").attr("height","100")  

    }));


	$("#op").click(function(){
		$.post( "http://127.0.0.1:8000/inner/post/poste",{"pp":$("#pt").val()}, function( data ) {	
			if (data=="200"){
				alert("you should connect first");
			}
			else if(data=="100"){

          a=$("<div id='container'></div>");          
          c=$("<div></div>").append("<img class='po' width='80' height='80'>");
          d=$("<div></div>").append("<h3>"+$("#id_user").attr("value")+"</h3>"+"<p>"+$("#pt").val()+"</p>");

          a.append(c,d);
					$("#wall").prepend(a);
					$("#pt").val("");
			}
			else{
				alert("something went wrong");			}
		return false;
		});});

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
	$.post("http://127.0.0.1:8000/inner/post/load_site",{"url":$("#url").val()},function(data){
		$("#loads").css("display","none");
		if (data.slice(0,2)=="100"){
			$("#result_site").text("something went wrong try again");
		}
		else{
			$("#result_site").text("choose your element");
			//$("#printer").append();
		}
		$(function() {
	var $frame = $('<iframe style="width:100%; height:800px;">');
	$('#printer').html( $frame );
	setTimeout( function() {
		var doc = $frame[0].contentWindow.document;
		var $body = $('body',doc);
		$body.html(data.slice(3,data.length-1));
	}, 1 );
});


	});
	});


// get posts
//$(document).ready(
//$.post("http://127.0.0.1:8000/inner/post/load_site",{"pos":$("#pos_st").attr("pos"),function(posts){

//}});	);