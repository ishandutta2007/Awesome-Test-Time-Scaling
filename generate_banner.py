import os

assets_dir = 'assets'
os.makedirs(assets_dir, exist_ok=True)

# Generate dynamic SVG banner
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%" height="100%">
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#4a00e0;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8e2de2;stop-opacity:1" />
            <animate attributeName="x1" values="0%;100%;0%" dur="10s" repeatCount="indefinite" />
            <animate attributeName="y1" values="0%;100%;0%" dur="10s" repeatCount="indefinite" />
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#grad1)" rx="15" />
    <text x="50%" y="45%" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-family="Arial, sans-serif" font-size="48" font-weight="bold">
        Awesome Test-Time Scaling
        <animate attributeName="opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite" />
    </text>
    <text x="50%" y="70%" dominant-baseline="middle" text-anchor="middle" fill="#dddddd" font-family="Arial, sans-serif" font-size="20">
        Pipeline Parallelism in AI: History, Variants &amp; Applications
    </text>
</svg>"""

with open(os.path.join(assets_dir, 'banner.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_content)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Add banner at the top if not exists
if "![Banner]" not in readme:
    readme = "![Banner](./assets/banner.svg)\n\n" + readme

# Add emojis to headings
replacements = {
    "# Awesome-Test-Time-Scaling": "# 🚀 Awesome-Test-Time-Scaling",
    "## Pipeline Parallelism in AI: History, Progression, Variants, & Applications": "## 🧠 Pipeline Parallelism in AI: History, Progression, Variants, & Applications",
    "## 1. The Macro Chronological Evolution": "## ⏳ 1. The Macro Chronological Evolution",
    "## 2. Core Scheduling & Architectural Variants": "## ⚙️ 2. Core Scheduling & Architectural Variants",
    "## 3. The Pipelined Communication & Bubble Matrix": "## 📡 3. The Pipelined Communication & Bubble Matrix",
    "## 4. Production Engineering Challenges & Hardware Solutions": "## 🛠️ 4. Production Engineering Challenges & Hardware Solutions",
    "## 5. Frontier Real-World AI Industrial Applications": "## 🌍 5. Frontier Real-World AI Industrial Applications",
    "## References": "## 📚 References"
}

for old, new in replacements.items():
    readme = readme.replace(old, new)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("Banner created and emojis added to README.")
