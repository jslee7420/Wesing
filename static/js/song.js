var player = document.getElementById("song-audio");
var lyricDiv = document.querySelector(".song-lyrics");
var imgDiv = document.querySelector(".song-img");

const tripElement = (e) => {
	var c = [];
	for (var a in e) c.push(e[a].trim());
	return c;
};

lyrics = tripElement(lyrics);
photos = tripElement(photos);
timeLine = tripElement(timeLine);

const deterTimeLine = (time) => {
	for (var i in timeLine) if (timeLine[i] > time) return i - 1;
};

const manageAudio = () => {
	var currentTime = player.currentTime;
	var order = deterTimeLine(currentTime);

	if (typeof lyrics[order] == "undefined") lyricDiv.innerHTML = "";
	else lyricDiv.innerHTML = lyrics[order];

	if (typeof photos[order] == "undefined") imgDiv.innerHTML = "";
	else {
		var src = images[photos[order]];
		var img = `<img src="/${src}">`;
		imgDiv.innerHTML = img;
	}
};

player.ontimeupdate = function () {
	manageAudio();
};
