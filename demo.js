let songIndex = 0;
let songs = [
    {songName: "Attention", filePath: "songs/1.mp3",singer:"Charlie Puth" ,coverPath: "block62.png"},
    {songName: "How long", filePath: "songs/2.mp3",singer:"Charlie Puth" , coverPath: "block62.jfif"},
    {songName: "Never Say Never", filePath: "songs/3.mp3",singer:"Justin Bieber" , coverPath: "block65.jpg"},
    {songName: "Sorry", filePath: "songs/4.mp3",singer:"Justin Bieber" , coverPath: "block65.jfif"},
    {songName: "The Way I Am", filePath: "songs/5.mp3",singer:"Charlie Puth" , coverPath: "block66.jfif"},
    {songName: "We Don't talk anymore", filePath: "songs/6.mp3",singer:"Charlie Puth" , coverPath: "block63.jfif"}
]
let volumeBar = document.getElementById("volume_slider");
volumeBar.value = 100;

let progressBar =  document.getElementById("progressbar");
progressBar.value = 0;
// console.log(songs[0].songName);
document.getElementById("info").innerText = songs[songIndex].songName;
document.getElementById("name").innerText =  songs[songIndex].singer;
document.getElementById('song_image').img = songs[songIndex].coverPath;
let audioElement = new Audio(songs[songIndex].filePath);
let playButton = document.getElementById("play");
let nextSong = document.getElementById("skip_next");
let prevSong = document.getElementById("skip_previous");
let forwardSong = document.getElementById("forward");


forwardSong.addEventListener("change", ()=>{
    if((audioElement.currentTime+10)>audioElement.duration)
    {
        audioElement.currentTime = 0;
    }
    else
    {
        audioElement.currentTime = progressBar.value+10;
    }
});


nextSong.addEventListener("click", ()=>{
    //console.log(songIndex+" "+songs.length);
    if(songIndex<songs.length)
    {
        songIndex = songIndex+1;
        audioElement.pause();
        audioElement = new Audio(songs[songIndex].filePath);
        audioElement.play();
        progressBar.value = 0;
    }
    else
    {
        songIndex = 0;
        audioElement.pause();
        audioElement = new Audio(songs[songIndex].filePath);
        audioElement.play();
        progressBar.value = 0;
    }
});

prevSong.addEventListener("click",()=>{
    if(songIndex>0)
    {
        songIndex = songIndex -1;
        audioElement.pause();
        audioElement = new Audio(songs[songIndex].filePath);
        audioElement.play();
        progressBar.value = 0;
    }
    else{
        songIndex = songs.length-1;
        audioElement.pause();
        audioElement = new Audio(songs[songIndex].filePath);
        audioElement.play();
        progressBar.value = 0;
    }
});



playButton.addEventListener("click", ()=>{
    if(audioElement.paused || audioElement.currentTime<=0)
    {
        audioElement.play();
        audioElement.classList.remove("playBut");
        audioElement.classList.add("pauseButton");
    }
    else
    {
        audioElement.pause();
        audioElement.classList.remove("pauseButton");
        audioElement.classList.add("playBut");
    }
});



audioElement.addEventListener("timeupdate",()=>{
    progress = parseInt((audioElement.currentTime/audioElement.duration)*100);
    progressBar.value = progress;
});

progressBar.addEventListener("change",()=>{
    audioElement.currentTime = parseInt((progressBar.value*(audioElement.duration/100)));
});





