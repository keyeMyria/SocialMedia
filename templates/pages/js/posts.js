function loadit(a){
	if ($("#end_p").length ==0)
	if (($(window).scrollTop() == ($(document).height() - $(window).height()) )|| a)  {
	
$("#loads_post").attr("style","margin-left: 30%;display:block;border:0px;");
$.post("http://"+host+":80/inner/post/load_posts",{"ic":$("#wall").attr("ic"),"pid":$("#menu").attr("id2")||-1},function(posts){
	if (posts != ""){
	
			$.post( "http://"+host+":80/inner/pic_im1",{"id":posts.userid},function( data ) {
					for (i=0;i<=posts.length-1;i++){

          a=$("<div class='po' id='container'></div>");          
          c=$("<div></div>").append("<img class='post_finder'  src="+data+" width='80' height='80'>");
          d=$("<div></div>").append("<h3>"+posts[i].author+"</h3>"+"<p>"+posts[i].post+"</p>");

          a.append(c,d);
					$("#wall").append(a);
         	$("#loads_post").attr("style","margin-left: 30%;display:none;border:0px;")
         	p=$("#loads_post")[0];
         	$("#loads_post").remove();
         	$("#wall").append(p);
         	$("#wall").attr("ic",$(".post_finder").length)
		


    }})
	}
	else {
         	$("#loads_post").attr("style","margin-left: 30%;display:none;border:0px;")

        if ($("#end_p").length ==0){
        
		$("#wall").append("<label id='end_p' style='margin-left: 39%;margin-top: 6%'>end of posts</label>");
	}}

})}};






$(document).ready(function(){loadit(1)});

$(window).scroll(function(){loadit()});