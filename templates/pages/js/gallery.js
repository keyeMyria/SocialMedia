
$.post("/gallery/all",{"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value},function (data){
media = $("#media")[0].value;
if (data.data.length%3==0)
	n =(data.data.length/3);
else
	n= (data.data.length/3 )+1;
for (j=0;j<=n;j++){		
var a=$("<div class='row imagetiles' > ");
for(i=0;i<3;i++){
try{	
a.append("<div class='col-lg-3 col-md-3 col-sm-3 col-xs-6'>"+"<img src="+media+data.data[i+j*3].img.img+" class='img-responsive'></div>" );
   }
catch(err){
	console.log(err);
  }
}	
a.append("</div>");
$('#gal').append(a) ;
	 };



	});