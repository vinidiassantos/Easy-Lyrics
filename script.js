document.getElementById("search").addEventListener("input", function () {
  const term = this.value.toLowerCase();
  const songs = document.querySelectorAll("#song-list li");

  songs.forEach(song => {
    const text = song.innerText.toLowerCase();
    song.style.display = text.includes(term) ? "block" : "none";
  });
});
