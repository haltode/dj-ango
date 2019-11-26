// Load the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// Create the iframe for the YouTube player
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '600',
        width: '800',
        videoId: 'fJIKatjB00U',
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerReady(event) {
    event.target.playVideo();
}

function onPlayerStateChange(event) {
}

function stopVideo() {
    player.stopVideo();
}
