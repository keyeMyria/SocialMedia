/*global $, alert,console*/


$(function () {
	'use strict';
	$('.im').attr("width",$(window).width());
	$('.im').attr("height",$(window).height());
	$(window).resize(function (){
	$('.im').attr("width",$(window).width());
	$('.im').attr("height",$(window).height());
	});
	});


$("#2").offset({ top:$(window).scrollTop() +	$(".im").height()});

$( window ).scroll(function() {
$("#2").offset({ top:$(window).scrollTop() + $(".im").height()});
  })
   
$('#look').keyup(function (e){
  

  if (e.keyCode == 13) {
       $.post( "/inner/look",{"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value,"name":$("#look")[0].value}, function( data ) {
        $("#myModal").css("display","block")
        $('#fake').remove();
        var table = $("<table id='fake'></table>");
        for(i=0; i<data.length ; i++){
        
          var a= $("<a ></a>").addClass('bar').attr("href","profile?id="+data[i].id).text( data[i].f+"\n "+data[i].email);
        var row = $('<tr></tr>');
  
       table.append(row.append(a.append($("<img>").attr('src',data[i].img).attr('width',"150").attr('height',"150"))));
}

$('#tb').append(table);
  return false;

});
   }
})

// out of pop up

// If an event gets to the body
$("body").click(function(){
  $("#myModal").css("display","None");
  
});

// Prevent events from getting pass .popup
$("#tb").click(function(e){
  e.stopPropagation();
});

//close button
$('#close').click(function(e){
  $("#myModal").css("display","None");

})
//remove old data
$('#act').click(function(e){
  $('#fake').remove();

});



