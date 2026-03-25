<p align="center">
  <img src="crs_lm/assets/banner.svg" width="100%">
</p>

<h1 align="center">mos-parameter-golf</h1>

<p align="center">
<b>Context-aware efficiency experiments for small language models</b><br>
Active system: <code>crs_lm</code>
</p>

---

## What this repo is

This repository explores a simple question:

> Can small language models become more efficient by improving input structure instead of only shrinking model size?

The current active project is:

## CRS-LM
**Context Reconstruction for Language Models**

Located in:

```text
crs_lm/
Core idea

Instead of increasing parameters, CRS-LM explores:

compressing context while preserving structure

Current result

In a controlled tiny-LM setup:

Mode	Tokens	Loss
Baseline	81	0.1873
CRS (0.75)	76	0.1824

This suggests that light, structure-aware filtering can reduce token load while preserving or slightly improving learning quality in a tiny setup.

Start here
cd crs_lm
pip install -r requirements.txt
python compare.py
Repository layout
mos-parameter-golf/
└── crs_lm/   # active project
Author

Raaj Mandale
Founder — ERANEST Technoware Pvt Ltd

License

MIT License