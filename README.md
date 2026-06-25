# ⚙️ Static Site Generator

> A zero-dependency Markdown-to-HTML static site generator, built from scratch in Python.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Dependencies](https://img.shields.io/badge/dependencies-none-lightgrey)

---

## Overview

This project is a fully custom static site generator written in pure Python — no third-party markdown libraries, no template engines, no build toolchain. It implements the complete Markdown parsing pipeline from scratch: raw text is split into discrete blocks, each block is classified by type, inline syntax is tokenised into a tree of `TextNode` objects, and the entire structure is rendered as a recursive `HTMLNode` tree before being injected into a shared HTML template. The output is a set of deployable HTML files under `docs/` that mirror the directory structure of `content/`.

---

## Key Features

- 📝 **Full Block-Level Markdown Parser** — Headings (h1–h6), paragraphs, fenced code blocks (` ``` `), blockquotes (`>`), ordered lists, and unordered lists (`-`)
- ✨ **Inline Syntax Engine** — Parses bold (`**`), italic (`_`), inline code (`` ` ``), hyperlinks `[text](url)`, and embedded images `![alt](url)` within any block type
- 🌲 **Recursive HTML Node Tree** — A three-class hierarchy (`HTMLNode` → `LeafNode` / `ParentNode`) models the DOM and renders to an HTML string via recursive `to_html()` calls
- 📂 **Recursive Page Generation** — Walks the entire `content/` directory, converting every `.md` file to a corresponding `.html` file in `docs/` at the same relative path
- 🧩 **Template Injection** — Merges generated HTML and the extracted `# H1` page title into `template.html` via `{{ Title }}` and `{{ Content }}` placeholders; supports a configurable base path for subdirectory deployments (e.g. GitHub Pages)
- 🧹 **Clean Build** — Wipes and fully regenerates the `docs/` output directory on every run, with recursive copying of `static/` assets (images, CSS)
- 🧪 **Comprehensive Test Suite** — 40+ unit tests across all parsing stages: block splitting, block type detection, inline delimiter splitting, link/image extraction, node rendering, and full Markdown-to-HTML integration

---

## Tech Stack

| Technology | Role |
|---|---|
| Python 3 | Primary language |
| `os`, `shutil`, `pathlib` | File system traversal and output management |
| `re` | Regex-based inline link and image extraction |
| `enum` | `BlockType` and `TextType` constants |
| `unittest` | Test framework |

**No third-party packages are required.**

---

## Installation

**Prerequisites:** Python 3.x

```bash
# Clone the repository
git clone https://github.com/your-username/static-site-generator.git
cd static-site-generator
```

---

## Usage

**Generate the site (for local development):**
```bash
python3 src/main.py
```

**Generate for GitHub Pages deployment (with custom base path):**
```bash
bash build.sh
# Equivalent to: python3 src/main.py "/static-site-generator/"
```

**Generate and serve locally:**
```bash
bash main.sh
# Generates site, then serves docs/ at http://localhost:8888
```

**Run the full test suite:**
```bash
bash test.sh
# Equivalent to: python3 -m unittest discover -s src
```

**Adding new content:** Create a `.md` file anywhere inside `content/`. The generator will recursively discover it and produce a matching `.html` under `docs/` with the same directory structure. Every Markdown file **must** contain at least one `# H1 heading`, which is extracted as the page `<title>`.

**Adding static assets:** Place images, CSS, or other static files in `static/`. They are copied verbatim to `docs/` on every build, preserving subdirectory structure.

---

## Project Structure

```
static-site-generator/
├── src/
│   ├── main.py                  # Entry point: clean+copy static, generate pages recursively
│   ├── markdowntohtmlnode.py    # Top-level converter: Markdown string → ParentNode("div")
│   ├── markdowntoblocks.py      # Splits raw Markdown on double newlines into block strings
│   ├── blocktypes.py            # BlockType enum + block_to_block_type() classifier
│   ├── texttotextnodes.py       # Inline parsing pipeline: images → links → code → bold → italic
│   ├── splitdelimeter.py        # Splits TextNode list on a delimiter (bold, italic, code)
│   ├── extractmarkdown.py       # Regex extraction + node splitting for images and links
│   ├── textnode.py              # TextNode class + TextType enum + text_node_to_html_node()
│   ├── htmlnode.py              # Base HTMLNode: tag, value, children, props
│   ├── leafnode.py              # LeafNode: renders self-contained HTML tags (no children)
│   ├── parentnode.py            # ParentNode: renders tags with recursive child rendering
│   ├── test_blocktypes.py
│   ├── test_extractmarkdown.py
│   ├── test_htmlnode.py
│   ├── test_leafnode.py
│   ├── test_markdowntoblocks.py
│   ├── test_markdowntohtmlnode.py
│   ├── test_parentnode.py
│   ├── test_splitdelimeter.py
│   ├── test_textnode.py
│   └── test_texttotextnodes.py
│
├── content/                     # Markdown source (mirrored to docs/ on build)
│   ├── index.md                 # Home page
│   └── blog/
│       ├── arch/index.md
│       ├── contact/index.md
│       └── frontend/index.md
│
├── docs/                        # Generated HTML output — do not edit manually
│
├── static/                      # Assets copied verbatim to docs/ on every build
│   ├── index.css
│   └── images/
│
├── template.html                # HTML shell with {{ Title }} and {{ Content }} placeholders
├── build.sh                     # Production build (GitHub Pages base path)
├── main.sh                      # Dev: build + serve docs/ on localhost:8888
└── test.sh                      # Runs full unittest suite from src/
```

---

## Parsing Pipeline

The core transformation happens in three stages:

**1. Block Parsing** (`markdowntoblocks.py` + `blocktypes.py`)
Raw Markdown is split on `\n\n` into blocks. Each block is classified as one of: `PARAGRAPH`, `HEADING`, `CODE`, `QUOTE`, `UNORDERED_LIST`, or `ORDERED_LIST`.

**2. Inline Parsing** (`texttotextnodes.py` → `splitdelimeter.py` + `extractmarkdown.py`)
Block text is passed through a sequential pipeline that splits `TextNode` lists on images, links, code backticks, bold `**`, and italic `_` markers, producing a flat list of typed `TextNode` objects.

**3. HTML Rendering** (`htmlnode.py` / `leafnode.py` / `parentnode.py`)
Each `TextNode` is converted to a `LeafNode`. Block-level nodes wrap their children in a `ParentNode` (e.g. `<p>`, `<h2>`, `<ul>`). The entire page is wrapped in a `ParentNode("div")`, which renders itself via recursive `to_html()` calls. The resulting HTML string is injected into `template.html`.

---

## Contributing

To add support for a new Markdown feature, implement parsing logic in the appropriate module (`blocktypes.py` for block-level, `splitdelimeter.py` or `extractmarkdown.py` for inline), add a corresponding rendering case in `markdowntohtmlnode.py`, and cover the change with tests in the matching `test_*.py` file. Run `bash test.sh` to verify all tests pass before submitting a pull request.

---
