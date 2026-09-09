# OneByJorah GitHub Pages Portal

A dynamic portal that showcases all 32 open-source projects by OneByJorah, including AI agents, network security tools, Active Directory utilities, Docker stacks, and monitoring dashboards.

![GitHub stars](https://img.shields.io/github/stars/OneByJorah/VirtOffice?style=flat-square) ![GitHub forks](https://img.shields.io/github/forks/OneByJorah/VirtOffice?style=flat-square) ![Projects](https://img.shields.io/badge/32%20projects-orange) ![Live%20Portal](https://img.shields.io/website/http/onebyjorah.github.io?style=flat-square)

## Overview

This repository hosts the **OneByJorah GitHub Pages portal** (`onebyjorah.github.io`), an auto‑generated website that displays all public repositories from the `OneByJorah` GitHub account. The portal is rebuilt weekly from live GitHub API data to ensure it always shows the latest project information.

### Key Features

- **Live Repository Data**: Pulls real-time information from GitHub API (stars, forks, language, topics, etc.)
- **Automatic Updates**: Runs weekly on GitHub Actions to regenerate `index.html`, `sitemap.xml`, and `robots.txt`
- **Project Classification**: Topics and tags help users discover related projects
- **SEO Optimized**: Includes structured data (JSON‑LD) and XML sitemap
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  GitHub API     │────▶│   gen.py        │────▶│ GitHub Pages    │
│  (Live Data)    │     │  (Python Script)│     │  (Static Site)  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                ▲
                                │
                    ┌─────────────────┐
                    │ GitHub Actions  │
                    │ (weekly cron)   │
                    └─────────────────┘
```

### Components

1. **gen.py** - Python script that:
   - Fetches repository data from GitHub API
   - Generates `index.html` with project cards
   - Creates `sitemap.xml` for SEO
   - Generates `robots.txt`

2. **GitHub Actions** (`.github/workflows/update-portal.yml`) - Automated workflow that:
   - Runs every Monday (06:17 UTC)
   - Regenerates the portal using `gen.py`
   - Pings IndexNow for fast indexing

3. **GitHub Pages** - Static site hosting via GitHub Pages

## Installation & Usage

### Running Locally

To generate the portal locally (useful for testing):

```bash
python3 gen.py
```

This will create:
- `index.html` - The main portal page
- `sitemap.xml` - XML sitemap for search engines
- `robots.txt` - Robots exclusion directives

### GitHub Actions Workflow

The portal updates automatically via GitHub Actions:

1. Visit the [Actions tab](https://github.com/OneByJorah/OneByJorah.github.io/actions)
2. Run the "Update Portal & Ping IndexNow" workflow manually if needed
3. Watch the portal update on Mondays (06:17 UTC)

## Portal Features

### Project Cards

Each project card displays:
- **Name** with link to GitHub repository
- **Description** (or "No description provided")
- **Metadata**: stars, language, forks, open issues
- **Topics/Tags** for easy filtering and discovery
- **Quick GitHub link** "View on GitHub →"

### Topic Filter

The portal includes a floating tag cloud that allows users to:
- Browse projects by category (e.g., `#ai`, `#docker`, `#security`)
- Click tags to jump directly to projects with those topics
- Discover related projects through shared topics

### SEO & Accessibility

- Schema.org structured data for better search engine understanding
- Semantic HTML5 markup
- Screen reader friendly navigation
- Mobile-responsive design

## Projects

The portal currently showcases **32 repositories** across various categories:

### AI & Machine Learning
- [AIStack](https://github.com/OneByJorah/AIStack)
- [ChatForge](https://github.com/OneByJorah/ChatForge)
- [BenchDash](https://github.com/OneByJorah/BenchDash)
- And more...

### Network Security & Infrastructure
- [VirtOffice](https://github.com/OneByJorah/VirtOffice)
- [TeleOps](https://github.com/OneByJorah/TeleOps)
- [NexusCore](https://github.com/OneByJorah/NexusCore)
- And more...

### Development Tools
- [StackForge](https://github.com/OneByJorah/StackForge)
- [CommandDesk](https://github.com/OneByJorah/CommandDesk)
- [ForgeDash](https://github.com/OneByJorah/ForgeDash)
- And more...

View all projects on the [live portal](https://onebyjorah.github.io/)

## Technology Stack

- **Frontend**: HTML5, CSS (custom variables), JavaScript
- **Backend**: Python 3.11+
- **API**: GitHub REST API
- **Deployment**: GitHub Pages
- **Automation**: GitHub Actions
- **SEO**: XML Sitemap, JSON-LD, IndexNow

## Maintenance

### GitHub Token (for local runs)

If you plan to run the generator locally, you'll need to authenticate with the GitHub API:

```bash
# Create a personal access token with public_repo scope
# Store it in a file named .git_token or set GITHUB_TOKEN environment variable
export GITHUB_TOKEN="your_token_here"
python3 gen.py
```

### Common Commands

```bash
# Test the generator locally
python3 gen.py

# Check what changed in generated files
git diff

# Run the workflow manually (requires authentication)
gitub-actions run update-portal.yml
```

## License

This portal is part of the OneByJorah organization. All individual projects have their own licenses accessible on their respective GitHub repositories.

## Contact

For issues with this portal:
- Open an issue in this repository
- Contact OneByJorah via GitHub profile

[View All Projects](https://onebyjorah.github.io/) • [GitHub Organization](https://github.com/OneByJorah)
