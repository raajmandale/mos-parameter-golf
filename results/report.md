# CRS-Core Experimental Report

## Project
CRS-Core — Context Reconstruction for Small Models

## Objective
Test whether a very small model can improve factual prediction using compact structured context reconstruction from a Pattern Map Engine (PME).

## Setup
- Model: TinyLM
- Knowledge Layer: PME (Pattern Map Engine)
- Retrieval Layer: relation-aware retrieval
- Reconstruction Layer: scored compact context builder

## Evaluation Modes
1. **Baseline**
   - query only

2. **Raw Retrieval**
   - query + retrieved context without strong scoring

3. **CRS**
   - query + scored compact reconstructed context

4. **Noisy Context**
   - query + misleading irrelevant context

## Expected Result Format

| Mode | Accuracy |
|------|----------|
| Baseline | XX% |
| Raw Retrieval | XX% |
| CRS | XX% |
| Noisy Context | XX% |

## Key Claim
CRS improves small-model factual prediction by injecting minimal relevant structured context instead of increasing parameter count.

## Example Cases

### Example 1
- Query: `what is capital of france`
- Baseline: `...`
- CRS Context: `france capital paris`
- CRS Output: `paris`

### Example 2
- Query: `who wrote hamlet`
- Baseline: `...`
- CRS Context: `hamlet author shakespeare`
- CRS Output: `shakespeare`

### Example 3
- Query: `what is formula of water`
- Baseline: `...`
- CRS Context: `water formula h2o`
- CRS Output: `h2o`

## Limitations
- small dataset
- single-token factual answers
- narrow benchmark domain
- not a replacement for large language models

## Conclusion
CRS-Core is a narrow experiment showing that parameter efficiency can be improved by reducing internal knowledge dependency and using compact external structure.