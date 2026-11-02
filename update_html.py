import re

with open('/app/index.html', 'r') as f:
    html = f.read()

# Add CSS
css = """
        /* Music Toggle */
        .music-toggle { position: fixed; bottom: 20px; right: 20px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 10px; border-radius: 50%; cursor: pointer; font-size: 1.2rem; transition: 0.3s; z-index: 999;}
        .music-toggle:hover { background: rgba(255,255,255,0.2); }
"""
html = html.replace('</style>', css + '\n    </style>')

# Add HTML
html = html.replace('<body>', '<body>\n    <button class="music-toggle" id="music-btn">🎵</button>\n    <audio id="bg-music" loop>\n        <source src="https://assets.mixkit.co/music/preview/mixkit-beautiful-dream-493.mp3" type="audio/mpeg">\n    </audio>')

# Add JS
js = """
        // Music Logic
        const musicBtn = document.getElementById('music-btn');
        const bgMusic = document.getElementById('bg-music');
        let isPlaying = false;

        musicBtn.addEventListener('click', () => {
            if (isPlaying) {
                bgMusic.pause();
                musicBtn.innerText = '🎵';
            } else {
                bgMusic.play();
                musicBtn.innerText = '⏸️';
            }
            isPlaying = !isPlaying;
        });
"""

html = re.sub(r'(document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{)', r'\1\n' + js, html)

with open('/app/index.html', 'w') as f:
    f.write(html)
