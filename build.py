import re, os
D = os.path.join(os.path.dirname(__file__), 'src') + os.sep
OUT = os.path.join(os.path.dirname(__file__), 'index.html')

css = open(D + '01_style.css').read()
js = ''.join(open(D + f).read() + '\n' for f in [
    '02_core.js', '03_eer.js', '04_import.js', '05a_content.js',
    '05b_topics.js', '05c_topics.js', '06_views1.js', '07_views2.js', '08_views3.js'
])
assert '</script' not in js.lower()

logo = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="19" r="2.5"/><circle cx="19" cy="19" r="2.5"/><path d="M12 7.5v5M12 12.5 6 17M12 12.5l6 4.5"/></svg>'

html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>Generalization &amp; Specialization Visualizer · EER Lab</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<div class="shell"><aside class="side" id="side"><div class="brand"><div class="logo">{logo}</div><div>EER Lab<small>Generalization &amp; Specialization</small></div></div><nav class="nav" id="nav" aria-label="Main"></nav></aside>
<div style="min-width:0"><header class="top"><button class="btn sm" data-act="menu" aria-label="Open menu">☰ Menu</button><b>EER Lab</b></header><main class="main" id="view"></main></div></div>
<script>
{js}
boot();
</script></body></html>'''

open(OUT, 'w').write(html)
print(f'Built {OUT} ({len(html):,} bytes)')
