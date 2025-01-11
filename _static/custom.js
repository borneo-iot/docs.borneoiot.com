window.addEventListener("load", function () {
    var videos = document.querySelectorAll("video");
    videos.forEach(function (video) {
        video.muted = true;
        video.autoplay = true;
        video.controls = true;
        video.loop = true;
    });
});
