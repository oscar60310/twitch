console.log("js loaded.");
var wsUri = "ws://127.0.0.1:10000/ws";
connect_web();         
function connect_web() 
{
    console.log("try to connect");

    $("#statu").html("Try to connect...");
    websocket = new WebSocket(wsUri);
    websocket.onopen = function(evt) {onOpen(evt)};
    websocket.onclose = function(evt) {onClose(evt)};
    websocket.onmessage = function(evt) {onMessage(evt)};
    websocket.onerror = function(evt) {onError(evt)};
}
function onOpen(evt) 
{
	$("#statu").html("successful connected.");
    doSend("SETTING"); 
}  
function onClose(evt) 
{ 
    
}
var sound,auto,nick;

function onMessage(evt) 
{ 
    var s = evt.data;
    console.log(s);
    if(s == "Update_OK")
    {
    	alert("Successful updated.")
    	location.reload(); 
    }
    else
    {
    	var set = s.split('<setting>')
    
    	auto = load_set(set[0]);
    	nick = load_set(set[1]);
   	 	sound = load_set(set[2]);
   
   	 	$("#cos_name").val(nick.name);
    	$("#Sound").val(sound.name);
    	$("#Reply").val(auto.name);
    	if(sound.name_t.split(',')[2] == 'true')
    		$("#sound_T").prop("checked",true);
    	else
    		$("#sound_F").prop("checked",true);
    	if(auto.name_t.split(',')[2] == 'true')
    		$("#auto_T").prop("checked",true);
    	else
    		$("#auto_F").prop("checked",true);
    	$("#auto_cd").val(auto.name_t.split(',')[3]);
    	$("#sound_cd").val(sound.name_t.split(',')[3]);
    }
    
}  
function onError(evt) 
{ 
	$("#statu").html("Can't connect,will try again in 10 seconds.");
    setTimeout(connect_web,10000);
}  
function doSend(message)
{ 

    websocket.send(message); 
}  
function load_set(raw)
{
	
	var r = $.trim(raw);

	var name_t = r.split('\n')[0];

	var name = "";
	var s =  r.split('\n');
	for(var i=1;i<s.length;i++)
	{
		name += s[i] + "\n";
	}
	return {name_t,name};
}
function update()
{
	var nick_sent = "Twitch ID,name\n" + $("#cos_name").val();
	var auto_sent =  "﻿send,re," + $("#auto_T").prop("checked") + "," + $("#auto_cd").val() + "\n" + $("#Reply").val();
	var sound_sent = "sound,src," + $("#sound_T").prop("checked") + "," + $("#sound_cd").val() + "\n" + $("#Sound").val();

	doSend("Update<setting>" + nick_sent + "<setting>" + sound_sent
	 + "<setting>" + auto_sent);
}