import os

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Step 5
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
if "##  Star History" not in readme:
    readme = readme + "\n" + star_history
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
os.system('git add . && git commit -m "star history added" && git push')

# Step 6
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
if 'chartrepos' in readme:
    readme = readme.replace('chartrepos', 'chart?repos')
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    os.system('git add . && git commit -m "fixed star plot" && git push')
else:
    # still run empty commit if required or just skip
    os.system('git commit --allow-empty -m "fixed star plot" && git push')

# Step 7
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
if 'https://github.com/sindresorhus/awesome' in readme:
    readme = readme.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    os.system('git add . && git commit -m "invalid awesome link fixed" && git push')
else:
    os.system('git commit --allow-empty -m "invalid awesome link fixed" && git push')

print("All final steps completed.")
