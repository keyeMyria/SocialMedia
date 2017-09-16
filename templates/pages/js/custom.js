//resize the container
$(document).ready(function (){
var size = "1000px";
$.each($('.carousel')[0].childNodes,function(a,b){
	var a='#'+b.id+''; 
	if(a != "#undefined"){
		$(a).css("width",size);
	}
		});
$($(".slider-product")[0]).css("width",size);
$('.caroufredsel_wrapper,#product,.slider-product ,.carousel').css("width",size);


$('.caroufredsel_wrapper')[1].style['width'] = size;
$('.caroufredsel_wrapper')[3].style['width'] = size;
$('.list_prod')[0].style['display'] = "None";


$('#list_prod_rect').click(function(){
if ($(".glyphicon-collapse-down").length >=1 ){
$('.glyphicon').removeClass('glyphicon-collapse-down');
$('.glyphicon').addClass('glyphicon-collapse-up');
$('.list_prod')[0].style['display'] = "block";
}
else
 {
$('.glyphicon').removeClass('glyphicon-collapse-up');
$('.glyphicon').addClass('glyphicon-collapse-down');
$('.list_prod')[0].style['display'] = "None";

}

});

});//end tag


//**/