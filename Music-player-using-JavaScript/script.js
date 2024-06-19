// script.js

const audioPlayer = document.getElementById('audio-player');
const musicTitle = document.getElementById('music-title');
const musicArtist = document.getElementById('music-artist');

function playPause() {
    if (audioPlayer.paused) {
        audioPlayer.play();
    } else {
        audioPlayer.pause();
    }
}

function stopAudio() {
    audioPlayer.pause();
    audioPlayer.currentTime = 0;
}

// Example: Change music title and artist dynamically
audioPlayer.addEventListener('loadedmetadata', function() {
    musicTitle.textContent = 'Sample Song';
    musicArtist.textContent = 'Unknown Artist';
});
