import re

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Test-Time-Scaling&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Test-Time-Scaling&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Test-Time-Scaling&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Test-Time-Scaling&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

# Step 5: Add Star History at the bottom
if "##  Star History" not in readme:
    readme = readme + "\n" + star_history

# Step 6: Replace chartrepos with chart?repos
readme = readme.replace('chartrepos', 'chart?repos')

# Step 7: Replace awesome link
readme = readme.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("Star History, chartrepos fix, and awesome link fix applied.")
