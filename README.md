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
(4) Create a file "start.bat" in the folder twitch-master, and paste the code bellow.
</li>

```bat
@echo off
python main.py [YourTwitchName] [Password] [ChatRoom]
PAUSE
```


</ol>
