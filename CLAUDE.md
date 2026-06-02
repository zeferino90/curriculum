# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Markdown CV that auto-generates a PDF via GitHub Actions on every push to `main`. The source of truth is `cv.md`; `cv.pdf` is a committed artifact regenerated automatically.

## File Structure

- `cv.md` — CV content (edit this)
- `cv.pdf` — Generated PDF (do not edit directly; committed by CI)
- `.github/workflows/generate_pdf.yml` — GitHub Actions workflow

## PDF Generation

**Automated:** Pushes to `main` trigger the workflow, which runs Pandoc and commits `cv.pdf` back.

**Local (manual preview):**
```sh
pandoc cv.md -o cv.pdf --pdf-engine=xelatex -V geometry:margin=1in
```
Requires Pandoc and `texlive-xetex` installed locally.

## GitHub Actions Workflow

- Triggered on push to `main` or manual `workflow_dispatch`
- Installs `pandoc` and `texlive-xetex` via apt
- Commits and pushes the generated `cv.pdf` using the `GH_Personal_Access_Token` secret
- The secret must be configured in the repo's Settings → Secrets as `GH_Personal_Access_Token` with `contents: write` permission

## Editing the CV

All content lives in `cv.md`. Pushing to `main` is sufficient to regenerate the PDF — no manual PDF commits needed.
