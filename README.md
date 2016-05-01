# twitch 聊天室
這是一個方便Twtich實況主顯示聊天室的工具<br>
利用IRC通訊協定連接聊天室&nbsp;<a href="http://help.twitch.tv/customer/portal/articles/1302780-twitch-irc" target="_blank">Twitch IRC</a><br>
<br>
目前的功能有:<br>
<ol>
<li>顯示聊天文字</li>
<li>客製化暱稱</li>
<li>追蹤者頭像、主播者頭像</li>
</ol>
<br>
<font color='red'>環境設定:</font><br>
<ol>
<li>您必須安裝<a href='https://www.python.org/'>Python2.7</a></li>
<li>安裝<a href='http://www.tornadoweb.org/en/stable/'>Tornado</a></li>
</ol>
#安裝教學
<ol>
<li>Install Python 2.7<br>
(1) go to <a href="https://www.python.org/downloads/" target="_blank">python website</a>, download python2.7.11 for your system and install it.<br>
(2) Add python path to Environment Variables. You can visit <a href="https://docs.python.org/2/using/windows.html">this</a> to get more infomation.<br>
(3) Type "python" in your command window, and you should see the version infomation.<br>
<img src="http://i.imgur.com/pAxx8c0.png"/>

</li>
<li>Install Tornado<br>
(1) Open cmd and cd to "C:\Python27\Scripts". (May be different if you choose custom path to install python)<br>
(2) Enter "pip install Tornado".<br>
<img src="http://i.imgur.com/GMOQDMQ.png"/>

</li>
<li>Setting Project<br>
(1) Download our code at <a href = "https://github.com/oscar60310/twitch">GitHub</a><br>
(2) Click "Download ZIP", download and unzip it.<br>
<img src="http://i.imgur.com/t435iwF.png"/>
(3) Visit <a href="http://twitchapps.com/tmi/">Twitch Chat OAuth Password Generator</a>, generate a password and copy it.<br>
<img src="http://i.imgur.com/OUz1s6j.png"/><br>
(4) Create a file "start.bat" in the folder twitch-master, and paste the code bellow.<br>
<pre><code>python main.py [YourTwitchName] [Password] [ChatRoom]</code></pre>

where YourTwitchName is your TwitchID, and Password is the string startwith "oauth", ChatRoom is the room you want to show.<br>
example: 
<pre><code>python oscar60310 oauth:*** oscar60310</code></pre>
will use ID oscar60310 join myself chatroom.
<br>
(5) Open your OBS or other stream software, create a new CLR Browser.<br>
(6) URL enter "D:\download\twitch-master\1.html" (the position of 1.html), and ckick OK.<br>
(7) Double ckicking the start.bat file you created, and you should see the message below.<br>
<img src="http://i.imgur.com/laRUsJD.png"/><br>
(8) Click "Preview" on OBS, and you will see join message on your OBS window.<br>
<img src="http://i.imgur.com/L3tgxNk.png"/><br><br>
Now, you can get the Chatroom on your stream.<br>
<img src="http://i.imgur.com/0Je1wzT.png"/><br><br>
</li>
<li>Custom nick<br>
(1) Open setting/nick.txt<br>
(2) Add "TwichID,nick" below the text,one line for one user.<br>
<img src="http://i.imgur.com/UoRlFTo.png"/><br>
(3) Restart server or type "nick load" to reload the nick list.
</li>

<li>Custom Icon<br>
(1) Your can replace the file "following.png" and "owner.png" for the icon to follower and owner.
</li>

<li>Command<br>
(1) stop - stop the server.<br>
(2) nick load - reload the nick.txt file.<br>
(3) follow load - update the followers list.<br>
(4) ping - ping the Twitch server.<br>

</li>

</ol>

#使用規定 Notices
您可以使用這些程式在您的實況頁面，可以的話在說明頁面加上我們的連結<br>
https://github.com/oscar60310/twitch<br><br>
You can use this code on your streams, just leave a credit on your page.
