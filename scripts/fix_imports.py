import os

# 1. Fix src/vite-env.d.ts
vite_env = """/// <reference types="vite/client" />
declare module '*.css';
declare module 'leaflet';
declare module 'react-leaflet';
declare module 'canvas-confetti';
"""
with open('src/vite-env.d.ts', 'w', encoding='utf-8') as f:
    f.write(vite_env)

# 2. Fix src/pages/DashboardPage.tsx imports
with open('src/pages/DashboardPage.tsx', 'r', encoding='utf-8') as f:
    dash_content = f.read()

dash_content = dash_content.replace("../../context/AppContext", "../context/AppContext")
dash_content = dash_content.replace("../../context/LanguageContext", "../context/LanguageContext")
dash_content = dash_content.replace("../../components/visualizer/ClosedLoopVisualizer", "../components/visualizer/ClosedLoopVisualizer")
dash_content = dash_content.replace("../../components/visualizer/RiskScoreCard", "../components/visualizer/RiskScoreCard")

with open('src/pages/DashboardPage.tsx', 'w', encoding='utf-8') as f:
    f.write(dash_content)

# 3. Fix src/components/map/GISMap.tsx
with open('src/components/map/GISMap.tsx', 'r', encoding='utf-8') as f:
    map_content = f.read()

map_content = map_content.replace("import 'leaflet/dist/leaflet.css';", "// leaflet css via html")

with open('src/components/map/GISMap.tsx', 'w', encoding='utf-8') as f:
    f.write(map_content)

# 4. Add leaflet.css link in index.html as standard
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

if 'leaflet.css' not in html_content:
    html_content = html_content.replace('</head>', '  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />\n  </head>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Vite env, DashboardPage imports, and Leaflet CSS fixed successfully!")
