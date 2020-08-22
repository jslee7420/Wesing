fullscreen = document.querySelector(".song-fullscreen");
songPrint = document.querySelector(".song-print");
songContainer = document.querySelector(".song-content");

fullscreen.addEventListener("click", () => {
	songContainer.requestFullscreen();
});

songPrint.addEventListener("click", () => {
	window.print();
});
