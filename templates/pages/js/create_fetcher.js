

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}

function run_check(){
url=$("#Url").val();
ide=$("#identifier").val();
ival=$("#id_value").val();
look=$("#look").val();
get=$("#get").val();
rad0=$("#radios-0").attr("checked");

rad="all";
if (rad0)
	rad="one";

$.post("/jobs/ini_job",{"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value,
	"url":url,
	"iden":ide,
	"ival":ival,
	"rad":rad,
	"look":look,
	"get":get},function(data){

		if(data =="sucess"){
			
			$("#sucess").fadeIn("fast",function(){

			$(this).delay(4000).fadeOut("slow");
			});
			

			}
		else{
			$("#fail").fadeIn("fast",function(){

			$(this).delay(4000).fadeOut("slow");
			});
			

			}
		});

	return false;
}