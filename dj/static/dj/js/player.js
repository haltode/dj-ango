// Load the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var songYtId = null;
var songStartTime = 0;

function updateCurrentSong(_callback) {
    $.getJSON("/dj/state", function(data) {
        songYtId = data.yt_id;
        songStartTime = data.elapsed;
        // We need to wait for the current function to finish
        _callback();
    });
}

// Create the iframe for the YouTube player
function onYouTubeIframeAPIReady() {
    updateCurrentSong(function() {
        player = new YT.Player('player', {
            height: '600',
            width: '800',
            videoId: songYtId,
            playerVars: {
                start: songStartTime,
            },
            events: {
                'onReady': onPlayerReady,
                'onStateChange': onPlayerStateChange
            }
        });
    });
}

function onPlayerReady(event) {
    event.target.playVideo();
}

function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.ENDED)
        location.reload();
}

function stopVideo() {
    player.stopVideo();
}
