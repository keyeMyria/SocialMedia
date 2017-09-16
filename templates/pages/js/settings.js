function subme(e){
if (e=="pass"){
	if($("#pass").val()!=$("#repass").val()){
		$("#repass").val("")
		return false;
	}
}
data= $("#"+e).val();
q =$("#"+e).attr('name');

query ={"csrfmiddlewaretoken":$('input[name="csrfmiddlewaretoken"]')[0].value};
query[q]=data;
$.post("/settings",query,function (resp){
	if(resp=="200"){
		$("#"+e).val("done");
	}
	else{
		$("#"+e).val("something went wrong!");

	}
});

}