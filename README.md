<p align="center">
  <img src="crs_lm/assets/banner.svg" width="100%">
</p>

<h1 align="center">mos-parameter-golf</h1>

<p align="center">
<b>Context-aware efficiency experiments for small language models</b><br>
Active system: <code>crs_lm</code>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-experimental-blue">
  <img src="https://img.shields.io/badge/focus-small--model--efficiency-green">
  <img src="https://img.shields.io/badge/method-SACR-orange">
  <img src="https://img.shields.io/badge/track-parameter--golf-purple">
</p>

---

## 🧠 What this repository is

`mos-parameter-golf` is a research repo exploring one core question:

> Can small language models become more efficient by improving input structure instead of only shrinking model size?

The current active direction is:

# 🚀 CRS-LM  
## Context Reconstruction for Language Models

This system lives in:

```text
crs_lm/
⚡ Core idea

Instead of only optimizing model size, CRS-LM explores a different path:

compress context while preserving structure

The idea is simple:

not all tokens are equally useful
sequence structure matters
cleaner input may help small models learn more efficiently
🔬 Current direction

CRS-LM focuses on:

🧩 structure-aware context reduction
🧠 token efficiency in tiny language models
📉 compression vs loss tradeoff
⚙️ lightweight preprocessing before the LM
📊 Result snapshot

From the current controlled tiny-LM sweep:

Mode	Tokens	Loss	Time (s)
Baseline	81	0.1873	0.4465
SACR (0.75)	76	0.1824	0.4036
🔥 Takeaway

A light, structure-aware reduction step reduced token count while preserving, and in this tiny setup slightly improving, final loss.

🧩 Active project layout
mos-parameter-golf/
└── crs_lm/
    ├── assets/
    ├── crs/
    ├── data/
    ├── docs/
    ├── model/
    ├── compare.py
    ├── train.py
    ├── requirements.txt
    └── README.md
▶️ Quick start
cd crs_lm
pip install -r requirements.txt
python compare.py
📄 Where to go next

For the actual project details, open:

crs_lm/README.md

For the experiment write-up, open:

crs_lm/docs/CRS_LM_EXPERIMENT.md
🧭 Positioning

This repository is:

🧪 an experimental research workspace
🧠 a context-first efficiency exploration
⚙️ a lightweight LM preprocessing direction
🚧 an evolving system, not a final benchmark claim
👤 Author

Raaj Mandale
Founder — ERANEST Technoware Pvt Ltd

📄 License

MIT License