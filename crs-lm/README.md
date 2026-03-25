<p align="center">
  <img src="assets/banner.svg" width="100%">
</p>

# CRS-LM  
### Context Reconstruction for Language Models

---

## 🧠 Problem

Small language models process flat token streams.

This causes:
- unnecessary tokens  
- weak structure awareness  
- inefficient learning  

---

## ⚡ Idea

> Not all tokens are equally useful

CRS-LM reduces tokens while preserving sequence structure.

---

## 🧩 Method

**SACR — Structure-Aware Context Reduction**

- keeps important tokens  
- preserves local neighbors  
- maintains sequence continuity  
- removes low-signal tokens  

---

## ⚙️ Pipeline

```text
Raw Tokens
   ↓
SACR (filter)
   ↓
Compact Sequence
   ↓
TinyLM
   ↓
Loss / Output
📊 Results
Mode	Tokens	Loss
Baseline	81	0.1873
SACR (0.75)	76	0.1824
🔥 Insight
light reduction works
aggressive reduction fails
structure matters more than raw token count
▶️ Run
pip install -r requirements.txt
python train.py
python compare.py
📁 Structure
crs-lm/
├── assets/
├── crs/
├── data/
├── docs/
├── model/
├── compare.py
├── train.py
└── requirements.txt
💡 One line

Efficiency is not just smaller models — it is better input.