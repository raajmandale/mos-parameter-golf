<p align="center">
  <img src="docs/assets/mos_banner.png" width="100%">
</p>

<h1 align="center">M-OS — Parameter Golf Branch</h1>

<p align="center">
<b>Pattern Runtime × Context Reconstruction</b><br>
Small-model robustness through structured context control
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-experimental-blue">
  <img src="https://img.shields.io/badge/runtime-pattern--graph-green">
  <img src="https://img.shields.io/badge/AI-CRS%20%7C%20PME-purple">
  <img src="https://img.shields.io/badge/track-parameter--golf-orange">
</p>

---

# 🧠 What This Repo Is

This is an **experimental branch of M-OS**, exploring:

> **Can we improve model behavior by controlling context instead of increasing parameters?**

Instead of scaling models, this repo investigates:

- structured context
- controlled retrieval
- noise resistance

---

# ⚡ Core Insight

Traditional systems assume:

> More parameters = better intelligence

This work explores:

> **Wrong context causes failure more than missing knowledge**

---

# 🧩 System Overview


Query
→ Entity Extraction
→ Pattern Map (PME)
→ Retrieval
→ Context Selection (CRS)
→ TinyLM
→ Prediction


---

# 🔬 CRS-Core (Experimental System)

**CRS-Core = TinyLM + PME + Context Control**

### Components

- **PME (Pattern Map Engine)**  
  → stores structured relations  

- **CRS (Context Reconstruction System)**  
  → filters and selects relevant context  

- **TinyLM**  
  → produces output from controlled input  

---

# 📊 What It Demonstrates

- Small models can perform well  
- Performance is **context-sensitive**  
- Correct context → stable output  
- Wrong context → collapse  

---

# 📈 Results

## Accuracy

| Mode | Accuracy |
|------|----------|
| Baseline | 100% |
| Raw Context | 100% |
| CRS | 100% |
| Noisy Context | **25%** |

---

## 🧠 Key Insight

> Models fail not because they don’t know  
> but because they are given **bad context**

---

## 🔥 Interpretation

- Clean context → stable predictions  
- Noisy context → **severe degradation**  

---

# 🧪 Ablation

| Setup | Accuracy |
|------|----------|
| TinyLM only | 100% |
| TinyLM + raw retrieval | 100% |
| TinyLM + CRS | 100% |

### Conclusion

CRS does not improve memorized tasks.

It is critical for:

> **protecting models from bad or misleading inputs**

---

# 🎯 Example

**Query**

what is capital of france


**CRS Context**

france capital paris


**Prediction**

paris


---

# 🚀 Run Locally

## Install
```bash
pip install -r requirements.txt
Train
python train.py
Demo
python demo.py
Evaluate
python eval/evaluate.py
Full Comparison
python eval/compare.py
python eval/ablation.py
📁 Project Structure
mos-parameter-golf/
│
├── model/        # TinyLM
├── crs/          # PME + CRS logic
├── data/         # dataset
├── eval/         # evaluation
├── results/      # experiment outputs
├── competition/  # submission notes
💡 Why This Matters

Most efficiency work focuses on:

model compression
architecture optimization

This repo explores:

Controlling what the model sees

🔗 Relation to M-OS

M-OS defines:

Pattern-based execution systems

This branch applies that idea to AI:

Pattern-based context control for inference stability

⚠️ Scope

This project is:

🧪 experimental
🧱 small-scale
🎯 focused on factual QA

This project is NOT:

❌ a GPT replacement
❌ a production system
❌ a large-scale model
🧠 One Line

Small models don’t just need knowledge —
they need the right context

🗺 Positioning
🧠 M-OS experimental branch
🏁 Parameter Golf submission
🔍 Context robustness demo
🚀 Foundation for future systems
👤 Author

Raaj Mandale
Founder — ERANEST Technoware Pvt Ltd

📄 License

MIT License