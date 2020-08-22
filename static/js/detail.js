fullscreen = document.querySelector(".song-fullscreen");
songContainer = document.querySelector(".song-content");

fullscreen.addEventListener("click", () => {
	songContainer.requestFullscreen();
});
