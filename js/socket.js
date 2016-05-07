var wsUri = "ws://127.0.0.1:10000/ws";
var output;
function init()
{
    alert_msg("正在載入...",0);
    output = document.getElementById("output");
    alert_msg("正在連接伺服器",0);
    connect_web();

}
            
function connect_web() 
{
    console.log("try to connect");
    websocket = new WebSocket(wsUri);
    websocket.onopen = function(evt) {onOpen(evt)};
    websocket.onclose = function(evt) {onClose(evt)};
    websocket.onmessage = function(evt) {onMessage(evt)};
    websocket.onerror = function(evt) {onError(evt)};
}
function onOpen(evt) 
{
    alert_msg("與本機連線成功",1);
    doSend("PING"); 
}  
function onClose(evt) 
{ 
    
}  
function onMessage(evt) 
{ 
    var s = evt.data;
    
    if (s == "PONG")
        return;
    else if (s[0] == 'p')
    {
        var text = "";
        for (var i = 1 ; i<s.length;i++)
            text += s[i]
        play(text)
        return;
    }
    var text = "";
    for (var i = 1 ; i<s.length;i++)
        text += s[i]
    alert_msg(text,s[0]);

   // websocket.close(); 
}  
function onError(evt) 
{ 
    connect_web_again();
}  
function doSend(message)
{ 
    //writeToScreen("SENT: " + message);
    websocket.send(message); 
}  
function writeToScreen(message) 
{ 
    var pre = document.createElement("p"); 
    pre.style.wordWrap = "break-word";
    pre.innerHTML = message; 
    output.appendChild(pre); 
}  
window.addEventListener("load", init, false);  