# 🤖 DecodeLabs AI Engineering Internship — 2026

A complete portfolio of 4 hands-on AI projects built during the **DecodeLabs AI Engineering Internship (Batch 2026)** — progressing from rule-based logic to supervised learning, recommendation systems, and computer vision.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Internship-Completed-success)
![Projects](https://img.shields.io/badge/Projects-4%2F4-brightgreen)

---

## 📋 Project Index

| # | Project | Core Concept | Tech Stack |
| --- | --- | --- | --- |
| 1 | [DecoBot — Rule-Based Chatbot](./Project1_RuledBased_Chatbot) | Control flow & dictionary-based intent matching | Python, Dictionaries |
| 2 | [DecoClassifier — Data Classification](./Project2_Data_Classification) | Supervised learning (KNN) | Scikit-Learn, Iris Dataset |
| 3 | [DecoRecommender — AI Tech Stack Recommender](./Project3_Recommendation) | Content-based filtering | TF-IDF, Cosine Similarity |
| 4 | [ImageTextOCR — Image & Text Recognition](./Project4_Image_Text_Recognition) | Computer vision & OCR | OpenCV, Tesseract, Pytesseract, NumPy |

---

## 🗂️ Project Details

### 1️⃣ DecoBot — Rule-Based AI Chatbot

**Goal:** Build a chatbot that responds using pure control flow — no ML involved.

- Continuous `while True` input loop with a clean exit strategy (`exit`, `quit`, `bye`, `goodbye`, `q`)
- Input sanitization (`.lower().strip()`)
- 30+ intent knowledge base (`RESPONSES` dictionary — O(1) average lookup)
- Multi-word phrase matching (`KEYWORD_MAP`) with longest-match-first, plus single-word fallback scanning
- Fallback response for unknown inputs + graceful `KeyboardInterrupt` handling
- Demonstrates: **Control flow, dictionary-based intent resolution, basic AI concepts**

📁 [`Project1_RuledBased_Chatbot/`](./Project1_RuledBased_Chatbot) → `chatbot.py`

---

### 2️⃣ DecoClassifier — Data Classification Using AI

**Goal:** Train a supervised classification model on a real dataset and evaluate it properly.

- **Dataset:** Iris (150 samples, 3 classes — Setosa / Versicolor / Virginica, 4 features)
- **Pipeline:** `StandardScaler` feature scaling → 80/20 Train/Test split (`random_state=42`) → `KNeighborsClassifier` (K=5)
- **Evaluation:** Confusion matrix, accuracy, weighted F1 score, full classification report
- Modular design: `load_data()`, `process()`, `output()` functions
- Demonstrates: **Data handling, supervised learning basics, model training**

📁 [`Project2_Data_Classification/`](./Project2_Data_Classification) → `classify.py`

---

### 3️⃣ DecoRecommender — AI Tech Stack Recommender

**Goal:** Build a content-based recommendation engine matching user skills to tech career paths.

- **Dataset:** `raw_skills.csv` — 15 job roles × 116 unique skill tags (self-built)
- **Algorithm:** TF-IDF vectorization (penalizes generic skills, rewards specific ones) + Cosine Similarity (magnitude-invariant matching)
- **Pipeline:** 4-Step Ranking — Ingestion → Scoring → Sorting → Filtering (Top-3 output with % score, matched skills, and full ranking table)
- Minimum 3-skill input validation + Cold Start detection for zero-similarity input
- Demonstrates: **Logic building, pattern matching, recommendation concepts**

📁 [`Project3_Recommendation/`](./Project3_Recommendation) → `recommend.py`, `raw_skills.csv`

---

### 4️⃣ ImageTextOCR — Image & Text Recognition

**Goal:** Extract machine-readable text from images using a full OCR pipeline.

- **Pre-processing pipeline:** Grayscale (`cvtColor`) → Gaussian Blur (`(5,5)` kernel) → Otsu's Adaptive Threshold (`THRESH_BINARY + THRESH_OTSU`)
- **OCR Engine:** Tesseract OCR (v5.5.3) via Pytesseract with `--oem 3 --psm 6` config (single uniform block of text)
- **Confidence scoring:** word-level confidence via `image_to_data()` averaged with NumPy (~90% on generated test scans)
- Automatically generates a test image (`test_image.jpg` → "Hello Decode Labs! AI Internship 2026") and saves grayscale + threshold versions
- Demonstrates: **Using AI libraries, understanding model outputs, image preprocessing**

📁 [`Project4_Image_Text_Recognition/`](./Project4_Image_Text_Recognition) → `ocr_recognition.py`

---

## 🛠️ Tech Stack

| Category | Tools |
| --- | --- |
| Language | Python 3.12 |
| ML / Data | Scikit-Learn, Pandas, NumPy |
| Computer Vision | OpenCV, Tesseract OCR (`pytesseract`) |
| Concepts | Control Flow, Supervised Learning (KNN), TF-IDF + Cosine Similarity, Optical Character Recognition (OCR) |

---

## 🚀 Getting Started

Each project folder is self-contained with its own `README.md` and run instructions. General setup:

```bash
git clone https://github.com/Devesh-18092005/DecodeLabs-AI-Internship-2026.git
cd DecodeLabs-AI-Internship-2026

# Install shared dependencies
pip install scikit-learn pandas numpy opencv-python pytesseract

# System dependency for Project 4 (OCR engine)
sudo apt-get install tesseract-ocr   # Linux
# brew install tesseract              # Mac
# or download from: https://github.com/UB-Mannheim/tesseract/wiki  (Windows)
```

Then `cd` into any project folder and follow its individual `README.md`.

---

## 🎓 Learning Journey

This internship moved progressively from **deterministic logic** → **statistical learning** → **similarity-based matching** → **perceptual AI**:

```javascript
Project 1            Project 2              Project 3                Project 4
Rule-Based     →     Supervised      →      Content-Based      →     Computer Vision
(Intent Engine)      Learning (KNN)         Filtering (TF-IDF)        (OCR)
```

Each milestone builds directly on the last — from teaching a machine to follow explicit rules, to teaching it to recognize patterns in structured data, to matching unstructured preferences, to finally interpreting raw pixels and scanned documents.

---

*Completed as part of the DecodeLabs Artificial Intelligence Industrial Training Program, Batch 2026.*
