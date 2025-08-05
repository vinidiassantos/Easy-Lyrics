<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Easy Lyrics</title>
  <style>
    body {
      font-family: sans-serif;
      padding: 20px;
      background: #f2f2f2;
    }

    h1 {
      text-align: center;
    }

    textarea, input, button, select {
      width: 100%;
      margin-bottom: 10px;
      padding: 10px;
      font-size: 16px;
    }

    .viewer {
      height: 300px;
      overflow-y: auto;
      white-space: pre-wrap;
      background: white;
      padding: 20px;
      border: 1px solid #ccc;
      margin-top: 20px;
    }

    .controls {
      display: flex;
      gap: 10px;
    }

    .controls button, .controls select {
      flex: 1;
    }
  </style>
</head>
<body>
  <h1>🎸 Easy Lyrics</h1>

  <input type="text" id="title" placeholder="Título da música" />
  <textarea id="lyrics" rows="10" placeholder="Cole aqui a cifra/letra..."></textarea>
  <button onclick="saveSong()">Salvar Cifra</button>

  <div class="controls">
    <button onclick="startScroll()">▶️ Scroll</button>
    <button onclick="stopScroll()">⏹️ Parar</button>
    <select id="speedSelect">
      <option value="50">Rápido</option>
      <option value="100" selected>Médio</option>
      <option value="150">Devagar</option>
    </select>
  </div>

  <div class="viewer" id="viewer"></div>

  <script>
    const viewer = document.getElementById('viewer');
    const lyricsInput = document.getElementById('lyrics');
    const titleInput = document.getElementById('title');
    const speedSelect = document.getElementById('speedSelect');
    let scrollInterval;

    function saveSong() {
      const title = titleInput.value.trim();
      const lyrics = lyricsInput.value;
      if (!title || !lyrics) {
        alert('Digite o título e a cifra!');
        return;
      }

      localStorage.setItem('easyLyrics_' + title, lyrics);
      viewer.innerText = lyrics;
      viewer.scrollTop = 0;
    }

    function startScroll() {
      const speed = parseInt(speedSelect.value);
      stopScroll(); // garantir que só tenha 1 scroll ativo
      scrollInterval = setInterval(() => {
        viewer.scrollTop += 1;
      }, speed);
    }
