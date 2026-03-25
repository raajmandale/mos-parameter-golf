<p align="center">
  <img src="crs-lm/assets/banner.svg" width="100%">
</p>

<h1 align="center">mos-parameter-golf</h1>

<p align="center">
<b>Context-aware efficiency experiments for small language models</b><br>
Active system: <code>crs-lm</code>
</p>

---

## 🧠 What this repo is

This repository explores a simple question:

> Can small language models become more efficient by improving input structure instead of only shrinking model size?

---

# 🚀 CRS-LM  
**Context Reconstruction for Language Models**

Located in:

```text
crs-lm/
⚡ Core idea

Instead of increasing parameters:

compress context while preserving structure

📊 Result snapshot
Mode	Tokens	Loss
Baseline	81	0.1873
SACR (0.75)	76	0.1824

👉 Fewer tokens, similar or better loss

▶️ Run
cd crs-lm
pip install -r requirements.txt
python compare.py
📁 Structure
mos-parameter-golf/
└── crs-lm/   # active project

👤 Author

Raaj Mandale
Eranest Technoware Pvt Ltd

📄 License

MIT License