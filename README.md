# Curriculum Vitae — Moisés Pérez Espinosa

🇬🇧 [English](#english) · 🇪🇸 [Español](#español)

---

## English

This repository contains my CV in **Markdown** format with an automated system to generate a **PDF** using GitHub Actions.

### 📄 Download CV

Download the latest PDF version here: **[cv.pdf](cv.pdf)**

### 🚀 Tech stack

- **Markdown** — CV content
- **Pandoc** — Markdown to PDF conversion
- **GitHub Actions** — automated PDF generation

### 🔧 Generate PDF locally

Make sure you have Pandoc and XeLaTeX installed, then run from the repo root:

```sh
pandoc cv.md -o cv.pdf --pdf-engine=xelatex -V geometry:margin=1in
```

The PDF is also regenerated automatically on every push to `main`.

### 📢 Contact

- 📧 [moises.perez.esp@gmail.com](mailto:moises.perez.esp@gmail.com)
- 💼 [linkedin.com/in/moisesperezespinosa](https://www.linkedin.com/in/moisesperezespinosa/)
- 🖥️ [github.com/zeferino90](https://github.com/zeferino90)

---

## Español

Este repositorio contiene mi currículum en formato **Markdown** con un sistema automatizado para generar un **PDF** utilizando GitHub Actions.

### 📄 Descargar CV

Descarga la versión más reciente en PDF aquí: **[cv.pdf](cv.pdf)**

### 🚀 Tecnologías utilizadas

- **Markdown** — contenido del CV
- **Pandoc** — conversión de Markdown a PDF
- **GitHub Actions** — generación automática del PDF

### 🔧 Generar el PDF manualmente

Asegúrate de tener Pandoc y XeLaTeX instalados y ejecuta desde la raíz del repositorio:

```sh
pandoc cv.md -o cv.pdf --pdf-engine=xelatex -V geometry:margin=1in
```

El PDF también se regenera automáticamente en cada push a `main`.

### 📢 Contacto

- 📧 [moises.perez.esp@gmail.com](mailto:moises.perez.esp@gmail.com)
- 💼 [linkedin.com/in/moisesperezespinosa](https://www.linkedin.com/in/moisesperezespinosa/)
- 🖥️ [github.com/zeferino90](https://github.com/zeferino90)
