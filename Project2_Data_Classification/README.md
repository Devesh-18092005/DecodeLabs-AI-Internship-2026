# 🤖 DecoClassifier — Data Classification Using AI

### Project 2 | Decode Labs AI Internship | Batch 2026

> *"Machine learning transforms data into knowledge by discovering patterns and using them to make predictions."*
> — Decode Labs Industrial Training Kit

---

## 📌 Project Overview

**DecoClassifier** is a Machine Learning-based Data Classification system built as **Project 2** of the Decode Labs AI Internship (Batch 2026).

This project demonstrates the **Classification Engine** using the **K-Nearest Neighbors (KNN)** algorithm on the **Iris Benchmark Dataset**.

The system loads the dataset, scales the features, splits the data into training and testing sets, trains a KNN model, generates predictions, and evaluates the results using **Accuracy, F1 Score, Confusion Matrix, and Classification Report**.

| Field         | Details                         |
| ------------- | ------------------------------- |
| **Intern**    | Devesh Marathe                  |
| **Track**     | Artificial Intelligence (AI)    |
| **Company**   | Decode Labs (`decodelabs.tech`) |
| **Mode**      | Remote / Virtual                |
| **Language**  | Python 3.x                      |
| **Algorithm** | K-Nearest Neighbors (KNN)       |
| **Dataset**   | Iris Benchmark                  |
| **Split**     | 80% Training / 20% Testing      |

---

## 🏗️ Architecture — The ML Pipeline

```text
INPUT  →  PROCESS  →  OUTPUT
  │           │           │
Dataset    Scaling     Evaluation
Loading    + Split     + Prediction
            + KNN
```

### Phase 1 — Dataset Loading

The Iris dataset is loaded using `scikit-learn`.

```python
iris = load_iris()

X = iris.data
y = iris.target

names = iris.target_names
feats = iris.feature_names
```

The dataset contains:

```text
150 Samples
4 Features
3 Classes
```

The three classes are:

```text
0 → Setosa
1 → Versicolor
2 → Virginica
```

The four features are:

```text
1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width
```

### Phase 2 — Feature Scaling

Before training the KNN model, the features are standardized using `StandardScaler`.

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Standardization transforms the features so they have approximately:

```text
Mean = 0
Variance = 1
```

Feature scaling is important for KNN because the algorithm relies on distance calculations.

### Phase 3 — Train-Test Split

The scaled dataset is divided into training and testing data.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)
```

The split produces:

```text
120 Training Samples
30 Testing Samples
```

### Phase 4 — KNN Training & Prediction

The project uses **K-Nearest Neighbors with K = 5**.

```python
model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

KNN classifies a new sample by finding its nearest training samples and assigning the class based on the majority of its neighbors.

```text
New Sample
     │
     ▼
Find 5 Nearest Neighbors
     │
     ▼
Compare Their Classes
     │
     ▼
Majority Vote
     │
     ▼
Predicted Class
```

---

## ✅ Project 2 — Classification Pipeline Checklist

| Requirement          | Status | Implementation            |
| -------------------- | ------ | ------------------------- |
| **DATASET**          | ✅      | Iris Benchmark Dataset    |
| **DATA LOADING**     | ✅      | `load_iris()`             |
| **FEATURES**         | ✅      | 4 numerical features      |
| **CLASSES**          | ✅      | 3 flower species          |
| **SCALING**          | ✅      | `StandardScaler()`        |
| **TRAIN-TEST SPLIT** | ✅      | 80/20 split               |
| **REPRODUCIBILITY**  | ✅      | `random_state=42`         |
| **ALGORITHM**        | ✅      | K-Nearest Neighbors       |
| **K VALUE**          | ✅      | `K=5`                     |
| **MODEL TRAINING**   | ✅      | `.fit()`                  |
| **PREDICTION**       | ✅      | `.predict()`              |
| **CONFUSION MATRIX** | ✅      | `confusion_matrix()`      |
| **ACCURACY**         | ✅      | `accuracy_score()`        |
| **F1 SCORE**         | ✅      | Weighted F1 Score         |
| **CLASSIFICATION**   | ✅      | `classification_report()` |

---

## 🌸 Iris Dataset Classes

| Class          | Label | Description     |
| -------------- | ----- | --------------- |
| **Setosa**     | `0`   | Iris Setosa     |
| **Versicolor** | `1`   | Iris Versicolor |
| **Virginica**  | `2`   | Iris Virginica  |

---

## 📊 Model Evaluation

### Accuracy

Accuracy measures the percentage of correctly classified test samples.

```python
acc = accuracy_score(y_test, y_pred)
```

The result is displayed as:

```text
Accuracy : XX.XX%
```

### F1 Score

The project calculates the weighted F1 score:

```python
f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)
```

F1 score combines **Precision** and **Recall** into a single metric.

### Confusion Matrix

```python
cm = confusion_matrix(y_test, y_pred)
```

The confusion matrix shows how many samples were correctly and incorrectly classified for each class.

```text
                 Predicted
              Setosa  Versicolor  Virginica
Actual Setosa
Actual Versicolor
Actual Virginica
```

Correct predictions appear on the diagonal of the matrix.

### Classification Report

```python
report = classification_report(
    y_test,
    y_pred,
    target_names=class_names
)
```

The report provides:

| Metric        | Purpose                                  |
| ------------- | ---------------------------------------- |
| **Precision** | Correctness of positive predictions      |
| **Recall**    | Ability to identify actual class samples |
| **F1-Score**  | Balance between precision and recall     |
| **Support**   | Number of samples in each class          |

---

## 🚀 How to Run

### Requirements

* Python 3.6 or above
* Scikit-learn

### Install Dependency

```bash
pip install scikit-learn
```

### Clone the Repository

```bash
git clone https://github.com/DeveshAi/DecoClassifier-Data-Classification.git
cd DecoClassifier-Data-Classification
```

### Run the Classifier

```bash
python classifier.py
```

---

## 📂 Project Structure

```text
project2_classification/
│
├── classifier.py        # Main KNN classification program
├── README.md            # Project documentation
└── screenshots/         # Demo screenshots
```

---

## 🔬 Key Concepts Demonstrated

| Concept                        | Where Used                             |
| ------------------------------ | -------------------------------------- |
| **Dataset Loading**            | `load_iris()`                          |
| **Feature Scaling**            | `StandardScaler()`                     |
| **Train-Test Split**           | `train_test_split()`                   |
| **Supervised Learning**        | Labeled Iris dataset                   |
| **Multi-Class Classification** | Three Iris classes                     |
| **K-Nearest Neighbors**        | `KNeighborsClassifier()`               |
| **Model Training**             | `model.fit()`                          |
| **Prediction**                 | `model.predict()`                      |
| **Accuracy**                   | `accuracy_score()`                     |
| **F1 Score**                   | `f1_score()`                           |
| **Confusion Matrix**           | `confusion_matrix()`                   |
| **Classification Report**      | `classification_report()`              |
| **Reproducibility**            | `random_state=42`                      |
| **Modular Programming**        | `load_data()`, `process()`, `output()` |

---

## 📐 Why Feature Scaling?

KNN uses distance to determine which samples are closest to each other.

If features have very different ranges, a feature with larger numerical values can have a greater influence on the distance calculation.

`StandardScaler` helps put all features on a comparable scale.

```text
Raw Iris Data
     │
     ▼
StandardScaler
     │
     ▼
Scaled Features
     │
     ▼
KNN Distance Calculation
     │
     ▼
Classification
```

---

## 🧠 Why KNN?

K-Nearest Neighbors is a simple supervised learning algorithm that classifies samples based on nearby training examples.

For this project:

```text
K = 5
```

The model considers the **5 nearest training samples** when predicting the class of a test sample.

```text
              New Sample
                   ●
                /  |  \
              ●    ●    ●
             /     |     \
            ●      ●
          Nearest Neighbors

              ↓

          Majority Vote

              ↓

        Predicted Class
```

---

## 📸 Screenshots

> *See `/screenshots` folder in this repo.*

Recommended screenshots:

```text
screenshots/
├── phase1_dataset.png
├── phase2_training.png
└── phase3_results.png
```

---

## 🎓 Learning Outcomes

* ✅ Understood the fundamentals of supervised machine learning
* ✅ Loaded and explored the Iris dataset
* ✅ Worked with numerical machine learning features
* ✅ Applied feature scaling using `StandardScaler`
* ✅ Created an 80/20 train-test split
* ✅ Implemented K-Nearest Neighbors classification
* ✅ Used K=5 for classification
* ✅ Trained a machine learning model
* ✅ Generated predictions for unseen test data
* ✅ Calculated classification accuracy
* ✅ Calculated weighted F1 score
* ✅ Generated a confusion matrix
* ✅ Generated a classification report
* ✅ Practiced modular Python programming
* ✅ Built an end-to-end machine learning classification pipeline

---

## 🔄 Complete Pipeline

```text
Iris Dataset
     ↓
Load Data
     ↓
Feature Scaling
     ↓
80/20 Train-Test Split
     ↓
KNN Model (K=5)
     ↓
Model Training
     ↓
Test Prediction
     ↓
┌───────────────┐
│   Evaluation  │
├───────────────┤
│ Accuracy      │
│ F1 Score      │
│ Confusion     │
│ Matrix        │
│ Classification│
│ Report        │
└───────────────┘
```

---

*Project 2 of 4 — Data Classification Using AI | Decode Labs AI Internship 2026*
