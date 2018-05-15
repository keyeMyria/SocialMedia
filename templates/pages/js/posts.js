
var socket = new WebSocket('ws:' + window.location.host + '/ws/check_user');

console.log(socket);

  
socket.onopen = function open() {
};



socket.onmessage = function message(event) {
  var data = JSON.parse(event.data);
  i=0;
   $('[id^=user_]').each(function(e){
    d=$(this).attr('id').match(/user_[0-9]+/)[0].split("user_")[1];  
    if (d==$("#id_user").val()){
      $(this).remove();
    }
    if (data[i]==true && $(this).attr("done")!='true' ){
      $(this).val("friends");
      $(this).css("display","block !important");
      $(this).onclick("");
    }
    else{
      $(this).attr("done","true");
    }
    i++;
    })

};


function update(){

  a= {};
  i=0;
  $('[id^=user_]').each(function() {
  d=$(this).attr('id').match(/user_[0-9]+/)[0].split("user_")[1];  
  if (d!=$("#id_user").val && $(this).attr("done")!='true'){
  a[i]=d;
    i++;
}
  });

a["job"]="check";
if (a.length > 1)
 socket.send(JSON.stringify(a));


}	





function add_user(user){
  var socket = new WebSocket('ws:' + window.location.host + '/ws/check_user');

  a["to"]=user; 
  
  socket.onopen = function open() {
  	a["job"]="add";
	socket.send(JSON.stringify(a));
};

socket.onmessage = function message(event) {
  var data = JSON.parse(event.data);
  // add sucess msg or fail
 


};

}


function loadit(a){
	if ($("#end_p").length ==0)
	if (($(window).scrollTop() == ($(document).height() - $(window).height()) )|| a)  {
	
$("#loads_post").attr("style","margin-left: 30%;display:block;border:0px;");
$.post("/inner/post/load_posts",{"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value,"ic":$("#wall").attr("ic"),"pid":$("#menu").attr("id2")||-1},function(posts){
	if (posts != ""){
	
			$.post("/inner/pic_im1",{"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value,"id":posts.userid},function( data ) {
					for (i=0;i<=posts.length-1;i++){

          a=$("<div class='po' id='container'></div>");          
          c=$("<div></div>").append("<img class='post_finder' style='margin-right: 40px;' src="+data+" width='80' height='80'>"+"<a href=/profile?id="+posts[i].userid+" style='margin-right:10px;color:#ee5706;font-size:20px;'>"+posts[i].author+"</a><input  value='add' id=user_"+posts[i].userid+" type='submit' done='false' class='btn' style='border-color:#ee5706;background-color: white !important;color:#ee5706  !important;display:none;' onclick='check(this.name);'> ");
          d=$("<div></div>").append("<p>"+posts[i].post+"</p>");

          a.append(c,d);
					$("#wall").append(a);
         	$("#loads_post").attr("style","margin-left: 30%;display:none;border:0px;")
         	p=$("#loads_post")[0];
         	$("#loads_post").remove();
         	$("#wall").append(p);
         	$("#wall").attr("ic",$(".post_finder").length)
		


    }
update();
})
	}
	else {
         	$("#loads_post").attr("style","margin-left: 30%;display:none;border:0px;")

        if ($("#end_p").length ==0){
        
		$("#wall").append("<label id='end_p' style='margin-left: 39%;margin-top: 6%'>end of posts</label>");
	}}

})

}


};





$(document).ready(function(){loadit(1);});

$(window).scroll(function(){loadit()});


