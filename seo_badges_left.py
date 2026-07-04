import re

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

badges_and_seo = """
<div align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
<a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
<!-- BADGES_RIGHT -->
</div>

**A curated collection of resources, papers, architectures, and variants focusing on Pipeline Parallelism in AI, model sharding, and trillion-parameter foundation models training.**
"""

readme = readme.replace("# 🚀 Awesome-Test-Time-Scaling", "# 🚀 Awesome-Test-Time-Scaling\n" + badges_and_seo)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
print("SEO and badges added.")
