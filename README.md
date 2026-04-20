# 🤖 AI Learning

A personal learning repository documenting my journey into AI and Large Language Models (LLMs) — built from the ground up, concept by concept.

---

## 📚 What This Is

This repo tracks my hands-on experiments as I learn the internals of how modern AI systems like GPT work. Each lecture folder corresponds to a topic I've studied and implemented in code.

---

## 🗂️ Repository Structure

```
AI Learning/
│
├── Lec-07/                    # Tokenization fundamentals
│   ├── the-verdict.txt        # Sample corpus used for tokenization experiments
│   ├── SimpleTokenizer.py     # Custom tokenizer implementations (V1 & V2)
│   └── tokenization.py        # Step-by-step tokenization walkthrough script
│
└── Lec-08/                    # Byte Pair Encoding (BPE)
    └── bpe.py                 # BPE tokenizer (in progress)
```

---

## 🧠 Lecture Breakdown

### Lecture 07 — Tokenization

> **Core Concept:** How raw text is broken down into tokens and mapped to integer IDs — the first step in any LLM pipeline.

**What I built:**

- **`SimpleTokenizerV1`** — A basic regex-based tokenizer that:
  - Splits text on punctuation, whitespace, and special characters
  - Builds a `str → int` vocabulary from a corpus
  - Encodes text to token IDs and decodes them back

- **`SimpleTokenizerV2`** — An improved version that:
  - Handles **unknown tokens** (`<unk>`) for words not seen during vocabulary building
  - Supports special tokens like `<endoftext>` to separate documents

**Key experiments in `tokenization.py`:**
1. Loaded `the-verdict.txt` (~20KB short story) as a real-world corpus
2. Explored progressively better regex splitting patterns
3. Built a vocabulary of ~1,100 unique tokens
4. Tested encoding/decoding round-trips on sample sentences
5. Demonstrated multi-document handling using `<endoftext>` separator

---

### Lecture 08 — Byte Pair Encoding (BPE)

> **Core Concept:** The subword tokenization algorithm used by GPT-2/GPT-3/GPT-4. Unlike simple word-level tokenizers, BPE handles unknown words gracefully by merging frequent character pairs.

**Status:** 🚧 Work in progress — `bpe.py` is the next thing to implement.

---

## 🛣️ Learning Roadmap

- [x] Basic regex tokenization
- [x] Vocabulary building from a corpus
- [x] Special tokens (`<unk>`, `<endoftext>`)
- [ ] Byte Pair Encoding (BPE)
- [ ] Embeddings (token + positional)
- [ ] Attention mechanism (self-attention)
- [ ] Transformer block
- [ ] GPT architecture
- [ ] Pre-training loop
- [ ] Fine-tuning / Instruction tuning

---

## 🔧 Requirements

Plain Python 3 — no external libraries needed for the tokenization lectures. Just the standard `re` module.

```bash
python Lec-07/tokenization.py
```

---

## 📖 Reference

Loosely following the concepts from **"Build a Large Language Model (From Scratch)"** by Sebastian Raschka, with my own experiments and notes layered on top.

---

*Learning in public. Every line of code here is something I actually understand (or am actively trying to).*
