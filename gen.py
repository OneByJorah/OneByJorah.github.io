#!/usr/bin/env python3
"""Generate the OneByJorah GitHub Pages portal: index.html + sitemap.xml + robots.txt.
Pulls live repo data from the GitHub API so the portal stays current."""
import json, urllib.request, html, datetime, os

OWNER = "OneByJorah"
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = f"https://{OWNER.lower()}.github.io"

def api(url):
    req = urllib.request.Request(url, headers={"User-Agent": OWNER, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

print("Fetching repos...")
repos = api(f"https://api.github.com/users/{OWNER}/repos?per_page=100&sort=updated")
repos = [r for r in repos if not r["fork"] and not r["private"]]
repos.sort(key=lambda r: (r["stargazers_count"], r["pushed_at"]), reverse=True)

def esc(s): return html.escape(s or "", quote=True)

cards = []
for r in repos:
    topics = " ".join(f'<a class="topic" href="{BASE}/#{t}">#{esc(t)}</a>' for t in r["topics"][:8])
    desc = esc(r["description"]) or "No description provided."
    lang = esc(r["language"]) if r["language"] else ""
    cards.append(f'''
    <article class="card" id="{esc(r['name'])}">
      <h2><a href="{esc(r['html_url'])}" rel="noopener">{esc(r['name'])}</a></h2>
      <p class="desc">{desc}</p>
      <div class="meta">
        <span title="stars">&#9733; {r['stargazers_count']}</span>
        <span title="language">{lang}</span>
        <span title="forks">&#10547; {r['forks_count']}</span>
        <span title="open issues">&#9678; {r['open_issues_count']}</span>
      </div>
      <div class="topics">{topics}</div>
      <a class="repo-link" href="{esc(r['html_url'])}" rel="noopener">View on GitHub &rarr;</a>
    </article>''')

all_topics = sorted({t for r in repos for t in r["topics"]})
topic_cloud = " ".join(f'<a class="tag" href="#{t}">#{esc(t)}</a>' for t in all_topics)

now = datetime.datetime.utcnow().strftime("%Y-%m-%d")

itemlist = ", ".join(
    '{"@type":"ListItem","position":%d,"url":"%s","name":"%s"}' % (i + 1, esc(r["html_url"]), esc(r["name"]))
    for i, r in enumerate(repos)
)
jsonld = (
    '{'
    '"@context":"https://schema.org",'
    '"@type":"Person",'
    '"name":"%s",'
    '"url":"https://github.com/%s",'
    '"sameAs":["https://github.com/%s"],'
    '"jobTitle":"Network Security Administrator",'
    '"mainEntity":{'
    '"@type":"ItemList",'
    '"numberOfItems":%d,'
    '"itemListElement":[%s]'
    '}'
    '}'
) % (esc(OWNER), OWNER, OWNER, len(repos), itemlist)

index = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(OWNER)} — Open-Source Projects &amp; Tools</title>
<meta name="description" content="{esc(OWNER)} builds {len(repos)} open-source projects: AI agents, network security, Active Directory tooling, Docker stacks, monitoring dashboards and more. Browse all repositories.">
<meta name="author" content="{esc(OWNER)}">
<link rel="canonical" href="{BASE}/">
<meta property="og:title" content="{esc(OWNER)} — Open-Source Projects">
<meta property="og:description" content="Browse all {len(repos)} repositories by {esc(OWNER)}: AI, security, sysadmin and dev-tooling projects.">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}/">
<link rel="sitemap" href="{BASE}/sitemap.xml">
<script type="application/ld+json">
{jsonld}
</script>
<style>
:root{{--bg:#0d1117;--fg:#e6edf3;--muted:#8b949e;--accent:#58a6ff;--card:#161b22;--border:#30363d}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
header{{padding:48px 24px 24px;text-align:center;border-bottom:1px solid var(--border)}}
header h1{{margin:0;font-size:2.4rem}}
header p{{color:var(--muted);max-width:640px;margin:12px auto}}
a{{color:var(--accent);text-decoration:none}}
a:hover{{text-decoration:underline}}
.cloud{{max-width:1000px;margin:24px auto;padding:0 24px;text-align:center}}
.tag,.topic{{display:inline-block;background:var(--card);border:1px solid var(--border);border-radius:999px;padding:4px 12px;margin:4px;font-size:.85rem;color:var(--muted)}}
.grid{{max-width:1000px;margin:0 auto;padding:24px;display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}}
.card{{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;display:flex;flex-direction:column;gap:8px}}
.card h2{{margin:0;font-size:1.2rem}}
.desc{{color:var(--muted);font-size:.92rem;margin:0;flex:1}}
.meta{{display:flex;gap:14px;flex-wrap:wrap;font-size:.82rem;color:var(--muted)}}
.topics{{font-size:.8rem}}
.repo-link{{font-size:.9rem;font-weight:600}}
footer{{text-align:center;color:var(--muted);padding:32px;border-top:1px solid var(--border);font-size:.85rem}}
</style>
</head>
<body>
<header>
  <h1>{esc(OWNER)}</h1>
  <p>Network Security Administrator &amp; open-source builder. {len(repos)} public repositories spanning AI agents, security tooling, Active Directory automation, Docker stacks and monitoring dashboards.</p>
</header>
<section class="cloud">{topic_cloud}</section>
<main class="grid">{''.join(cards)}</main>
<footer>
  <p>Generated {now} &middot; All projects hosted on <a href="https://github.com/{OWNER}" rel="noopener">GitHub</a> &middot; This portal is auto-generated from the live GitHub API.</p>
</footer>
</body>
</html>'''

# sitemap.xml
urls = [f"  <url><loc>{BASE}/</loc><changefreq>daily</changefreq></url>"]
urls += [f"  <url><loc>{esc(r['html_url'])}</loc><changefreq>weekly</changefreq></url>" for r in repos]
sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>'''

robots = f"""User-agent: *
Allow: /

Sitemap: {BASE}/sitemap.xml
"""

with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f: f.write(index)
with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as f: f.write(sitemap)
with open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8") as f: f.write(robots)

print(f"Wrote index.html, sitemap.xml, robots.txt for {len(repos)} repos")
