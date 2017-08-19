var host = "/gallery/all";


$.post(host,{'csrfmiddlewaretoken':document.getElementsByName('csrfmiddlewaretoken')[0].value},function (data){
media = $("#media")[0].value;
for (j=1;j<=data.data.length/3;j++){		
var a=$("  <div class='row imagetiles' > ");
		for(i=0;i<3;i++){


a.append("<div class='col-lg-3 col-md-3 col-sm-3 col-xs-6'>"+"<img src="+media+data.data[i+j-1].img.img+" class='img-responsive'></div>" )  };	
a.append("</div>");
$('#gal').append(a)  };







	});