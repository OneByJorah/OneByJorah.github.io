# OneByJorah.github.io

> GitHub Pages portal that indexes every public OneByJorah repository — auto-generated from the live GitHub API on a weekly cron, so the project index never goes stale.

[![License](https://img.shields.io/github/license/OneByJorah/OneByJorah.github.io?style=for-the-badge&color=FFB300&labelColor=0a0a09)](https://github.com/OneByJorah/OneByJorah.github.io)
[![Top Language](https://img.shields.io/github/languages/top/OneByJorah/OneByJorah.github.io?style=for-the-badge&color=FFB300&labelColor=0a0a09)](https://github.com/OneByJorah/OneByJorah.github.io)
[![Stars](https://img.shields.io/github/stars/OneByJorah/OneByJorah.github.io?style=for-the-badge&color=FFB300&labelColor=0a0a09)](https://github.com/OneByJorah/OneByJorah.github.io/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/OneByJorah/OneByJorah.github.io?style=for-the-badge&color=FFB300&labelColor=0a0a09)](https://github.com/OneByJorah/OneByJorah.github.io/commits)

![Portal screenshot](docs/screenshots/main.viewport.png)

## What This Is

This repo powers [onebyjorah.github.io](https://onebyjorah.github.io), a static portal listing every public, non-fork OneByJorah project with its description, language, stars, forks, open issues, and topics. A Python generator pulls live GitHub API data and rebuilds the site on schedule. Built for anyone who wants a single URL that shows everything the org ships.

## Quick Start

```bash
git clone https://github.com/OneByJorah/OneByJorah.github.io.git
cd OneByJorah.github.io
python3 gen.py
```

Regenerates `index.html`, `sitemap.xml`, and `robots.txt` in place. Preview with `python3 -m http.server 8000`.

## Features

- Live repo data from the GitHub API — stars, forks, language, topics, open issues
- Weekly auto-regeneration via GitHub Actions (Monday 06:17 UTC, plus manual dispatch)
- Topic tag cloud linking related projects
- JSON-LD structured data and XML sitemap for search engines
- IndexNow ping after each build for fast indexing
- Zero-runtime static output served by GitHub Pages

## Architecture

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#0a0a09','primaryTextColor':'#FFB300','lineColor':'#FFB300'}}}%%
graph LR
    A[GitHub Actions - weekly cron] --> B[gen.py]
    C[GitHub API] -->|live repo data| B
    B --> D[index.html + sitemap.xml + robots.txt]
    D --> E[GitHub Pages]
    B --> F[IndexNow ping]
```

`gen.py` calls the public API unauthenticated; set `GITHUB_TOKEN` locally to raise rate limits.

## Stack

Python 3.11+, GitHub REST API, HTML5, CSS, JavaScript, GitHub Pages, GitHub Actions, IndexNow

## Contributing

Issues and improvements are welcome — [open an issue](https://github.com/OneByJorah/OneByJorah.github.io/issues).

## License

MIT — see [LICENSE](LICENSE).
