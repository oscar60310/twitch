function alert_msg (msg,code) 
{
	/* 0 normal 
	   1 success
	   2 user
	   3 follow
	*/

	$("#output").append("<div class='text"+code+"'>"+msg+"</div>");
	$("html, body").animate({ scrollTop: $(document).height() }, "fast");
}
var t = 10;
function connect_web_again()
{
	var info_text = document.createElement("DIV");
	info_text.id = "connect_again_text";
	info_text.innerHTML = "無法連線";
	
	$("#output").append(info_text);
	t = 10;
	setTimeout(connect_again_counter,1000)
}
function connect_again_counter()
{
	if(t <= 0)
	{
		$("#connect_again_text").remove();
		connect_web();
	}
	else
	{
		t = t - 1;
		$("#connect_again_text").html("無法與本機伺服器連線，將在" + t +"秒後重試");
		setTimeout(connect_again_counter,1000);
	}
}