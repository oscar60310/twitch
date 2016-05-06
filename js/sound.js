function play(src)
{
    var audioElement = document.createElement('audio');
    audioElement.setAttribute('src', 'music/'+ src +'.mp3');
    audioElement.setAttribute('autoplay', 'autoplay');
    audioElement.play();
}