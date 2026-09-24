# 🔍 ImageTextOCR — Image & Text Recognition System

### Project 4 | Decode Labs AI Internship | Batch 2026

> *"Optical Character Recognition (OCR) enables computers to understand text contained within images, transforming visual information into machine-readable data."*

---

## 📌 Project Overview

**ImageTextOCR** is an image-to-text recognition system built as **Project 4** of the Decode Labs AI Internship (Batch 2026).

The project demonstrates how computer vision and Optical Character Recognition can be combined to detect and extract text from images.

The system uses **OpenCV** for image preprocessing and **Tesseract OCR** through **Pytesseract** for text extraction.

The OCR pipeline converts the input image into a grayscale representation, applies Gaussian blur to reduce noise, performs Otsu's thresholding to create a high-contrast binary image, and then passes the processed image to Tesseract for recognition.

| Field                  | Details                                       |
| ---------------------- | --------------------------------------------- |
| **Intern**             | Devesh Marathe                                |
| **Track**              | Artificial Intelligence (AI)                  |
| **Company**            | Decode Labs (`decodelabs.tech`)               |
| **Mode**               | Remote / Virtual                              |
| **Language**           | Python 3.14.3                                 |
| **Project**            | Project 4 — Image & Text Recognition          |
| **Libraries**          | OpenCV, Pytesseract, NumPy                    |
| **OCR Engine**         | Tesseract OCR 5.5.3                           |
| **Image Processing**   | Grayscale + Gaussian Blur + Otsu Thresholding |
| **Recognition Method** | Optical Character Recognition (OCR)           |

---

## 🎯 Project Objective

The main objective of this project is to build a simple OCR pipeline capable of:

* 🖼️ Reading text from an image
* 🔧 Preprocessing the image for improved recognition
* 🔤 Extracting machine-readable text
* 📊 Calculating OCR confidence
* 💾 Saving processed image versions
* 🧪 Automatically generating a test image
* 🤖 Using Tesseract OCR through Python

---

## 🏗️ Architecture — The OCR Pipeline

```text
INPUT IMAGE
     │
     ▼
┌─────────────────────┐
│  Load Image         │
│  OpenCV             │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Convert to Grayscale │
│ cvtColor()           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Gaussian Blur        │
│ Noise Reduction      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Otsu Thresholding    │
│ Binary Image         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Tesseract OCR        │
│ Pytesseract          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Extracted Text       │
│ + Confidence Score   │
└─────────────────────┘
```

---

## 🔬 Image Processing Pipeline

The project uses several preprocessing techniques before sending the image to Tesseract.

### 1. Image Loading

OpenCV loads the image using:

```python
image = cv2.imread(image_path)
```

If the image cannot be loaded, the program raises an error:

```text
ValueError: Could not load image
```

---

### 2. Grayscale Conversion

The original color image is converted into grayscale:

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Instead of processing three color channels (BGR), OCR works with a single intensity channel.

```text
COLOR IMAGE
   │
   ▼
BGR Channels
   │
   ▼
GRAYSCALE
```

---

### 3. Gaussian Blur

A Gaussian blur is applied to reduce small image noise:

```python
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
```

The `(5, 5)` kernel smooths the image before thresholding.

---

### 4. Otsu Thresholding

The blurred grayscale image is converted into a binary image:

```python
_, thresh = cv2.threshold(
    blurred,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
```

Otsu's method automatically determines a threshold value to separate foreground text from the background.

```text
Grayscale Image
       │
       ▼
 Otsu Thresholding
       │
       ▼
Black Text + White Background
```

This produces an OCR-friendly image.

---

## 🤖 Tesseract OCR

The project uses **Pytesseract** as the Python interface to the Tesseract OCR engine.

```python
text = pytesseract.image_to_string(
    thresh,
    config=custom_config
)
```

The project uses:

```python
custom_config = r'--oem 3 --psm 6'
```

### Configuration

| Parameter | Meaning                                 |
| --------- | --------------------------------------- |
| `--oem 3` | Use Tesseract's default OCR engine mode |
| `--psm 6` | Assume a single uniform block of text   |

This configuration works well for the simple text block generated by the test image.

---

## 📊 OCR Confidence Score

The program also extracts word-level OCR information:

```python
data = pytesseract.image_to_data(
    thresh,
    output_type=pytesseract.Output.DICT
)
```

Confidence values are collected and averaged:

```python
confidences = [
    int(conf)
    for conf in data['conf']
    if int(conf) > 0
]

avg_confidence = (
    np.mean(confidences)
    if confidences
    else 0
)
```

The final result is displayed as:

```text
📊 Average Confidence: XX.XX%
```

A higher confidence value generally indicates that Tesseract was more certain about the recognized text.

---

## 🧪 Automatic Test Image

The project automatically generates a test image so that OCR can be demonstrated without requiring an external image.

The image contains:

```text
Hello Decode Labs!
AI Internship 2026
```

The image is created using OpenCV:

```python
img = np.ones((200, 600, 3), dtype=np.uint8) * 255
```

Text is then rendered using:

```python
cv2.putText()
```

The resulting file is:

```text
test_image.jpg
```

---

## 📥 Input → Processing → Output

```text
INPUT
│
└── test_image.jpg
        │
        ▼
PREPROCESSING
│
├── Grayscale
├── Gaussian Blur
└── Otsu Thresholding
        │
        ▼
OCR
│
└── Tesseract OCR
        │
        ▼
OUTPUT
│
├── Extracted Text
├── Average Confidence
├── test_image_gray.jpg
└── test_image_threshold.jpg
```

---

## ✅ Project 4 Checklist

| Requirement                | Status | Implementation               |
| -------------------------- | ------ | ---------------------------- |
| **Image input**            | ✅      | OpenCV `imread()`            |
| **Image preprocessing**    | ✅      | Grayscale + Blur + Threshold |
| **OCR implementation**     | ✅      | Pytesseract + Tesseract      |
| **Text extraction**        | ✅      | `image_to_string()`          |
| **OCR confidence**         | ✅      | `image_to_data()`            |
| **Test image generation**  | ✅      | OpenCV `putText()`           |
| **Processed image output** | ✅      | `cv2.imwrite()`              |
| **Error handling**         | ✅      | Invalid image detection      |
| **Command-line execution** | ✅      | Python script                |

---

## 📊 Sample Output

Running:

```bash
python ocr_recognition.py
```

produces output similar to:

```text
==================================================
🔍 IMAGE TEXT RECOGNITION (OCR)
==================================================

🖼️  Processing: test_image.jpg

==================================================
📄 OCR TEXT EXTRACTION
==================================================

📝 Extracted Text:
--------------------------------------------------
Hello Decode Labs!
AI Internship 2026
--------------------------------------------------

📊 Average Confidence: 90.00%

💾 Saved: test_image_gray.jpg, test_image_threshold.jpg

==================================================
🎉 PROJECT 4 COMPLETED SUCCESSFULLY!
==================================================
```

> **Note:** The exact confidence percentage may vary depending on the installed Tesseract version and image-processing environment.

---

## 🚀 How to Run

### Requirements

Make sure Python is installed:

```bash
python --version
```

The project requires:

* Python 3.x
* OpenCV
* Pytesseract
* NumPy
* Tesseract OCR Engine

---

### Install Python Dependencies

```bash
pip install opencv-python pytesseract numpy
```

Or:

```bash
python -m pip install opencv-python pytesseract numpy
```

---

## 🪟 Windows — Tesseract Installation

Tesseract OCR is a separate program from the Python `pytesseract` package.

Install the Windows version of Tesseract OCR and make sure the executable is available.

Typical installation location:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

This project explicitly configures the executable path:

```python
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

Verify the installation:

```powershell
& "C:\Program Files\Tesseract-OCR\tesseract.exe" --version
```

Example:

```text
tesseract v5.5.3
```

---

## ▶️ Run the Project

Clone or download the project and navigate to the project directory:

```bash
cd Project4_Image_Text_Recognition
```

Run:

```bash
python ocr_recognition.py
```

The program will automatically:

1. Create a test image
2. Preprocess the image
3. Run OCR
4. Extract text
5. Calculate average confidence
6. Save processed images
7. Display the final result

---

## 📂 Project Structure

```text
Project4_Image_Text_Recognition/
│
├── ocr_recognition.py
├── test_image.jpg
├── test_image_gray.jpg
├── test_image_threshold.jpg
├── README.md
└── screenshots/
    └── demo.png
```

### File Description

| File                       | Purpose                            |
| -------------------------- | ---------------------------------- |
| `ocr_recognition.py`       | Main OCR implementation            |
| `test_image.jpg`           | Automatically generated test image |
| `test_image_gray.jpg`      | Grayscale version                  |
| `test_image_threshold.jpg` | Binary threshold version           |
| `README.md`                | Project documentation              |
| `screenshots/`             | Project demonstration screenshots  |

---

## 🔬 Key Concepts Demonstrated

| Concept                    | Where Used                 |
| -------------------------- | -------------------------- |
| **Computer Vision**        | OpenCV image processing    |
| **Image Preprocessing**    | Grayscale, blur, threshold |
| **OCR**                    | Tesseract OCR              |
| **Python OCR Integration** | Pytesseract                |
| **Noise Reduction**        | Gaussian Blur              |
| **Automatic Thresholding** | Otsu Thresholding          |
| **Confidence Measurement** | `image_to_data()`          |
| **Image Generation**       | OpenCV `putText()`         |
| **File Handling**          | `os.path` + OpenCV         |
| **Error Handling**         | Invalid image detection    |

---

## 🧠 Why Image Preprocessing Matters

Raw images may contain:

* Noise
* Shadows
* Uneven lighting
* Colored backgrounds
* Low contrast
* Blurred characters

OCR accuracy can be affected by these conditions.

This project therefore performs:

```text
Original Image
      │
      ▼
Grayscale
      │
      ▼
Gaussian Blur
      │
      ▼
Otsu Threshold
      │
      ▼
Tesseract OCR
```

The goal is to provide Tesseract with a cleaner representation of the text.

---

## ⚙️ Important Tesseract Configuration

The project uses:

```python
custom_config = r'--oem 3 --psm 6'
```

### OCR Engine Mode

```text
--oem 3
```

Uses Tesseract's default engine selection.

### Page Segmentation Mode

```text
--psm 6
```

Treats the image as a single uniform block of text.

This is suitable for the project's generated test image.

For different image layouts, other PSM modes may be more appropriate.

---

## 📈 Possible Improvements

The current project provides a basic OCR pipeline. It can be extended with:

* 📷 Real-time webcam OCR
* 📄 PDF text extraction
* 🌐 Multi-language OCR
* 🧾 Receipt/invoice recognition
* 🪪 ID card text extraction
* 🔢 Handwritten text recognition
* 🔍 Automatic image rotation
* ✂️ Text-region detection
* 🎨 Adaptive thresholding
* 🖥️ GUI interface
* 🌐 Web-based OCR application
* 📱 Mobile OCR integration

---

## ⚠️ Limitations

The current implementation is designed primarily for clear printed text.

OCR performance may decrease with:

* Handwritten text
* Very small fonts
* Low-resolution images
* Heavy image noise
* Complex backgrounds
* Strong perspective distortion
* Rotated text
* Unusual fonts

The `--psm 6` configuration is also optimized for a block-like text layout rather than every possible image layout.

---

## 🎓 Learning Outcomes

Through this project, the following concepts were implemented:

* ✅ Understanding Optical Character Recognition
* ✅ Integrating Tesseract with Python
* ✅ Using Pytesseract for OCR
* ✅ Loading and processing images with OpenCV
* ✅ Converting images to grayscale
* ✅ Applying Gaussian Blur
* ✅ Applying Otsu's thresholding
* ✅ Extracting text from images
* ✅ Measuring OCR confidence
* ✅ Saving processed images
* ✅ Generating test images programmatically
* ✅ Building a complete image-processing pipeline

---

## 🏁 Final Result

The project successfully demonstrates a complete OCR workflow:

```text
IMAGE
  ↓
OPENCV
  ↓
PREPROCESSING
  ↓
TESSERACT OCR
  ↓
EXTRACTED TEXT
  ↓
CONFIDENCE SCORE
```

The implementation combines **Computer Vision + OCR** into a simple Python-based image text recognition system.

---

## 👨‍💻 Internship Project

**Project 4 of 4 — Image & Text Recognition (OCR)**

**Decode Labs AI Internship — Batch 2026**

**Track:** Artificial Intelligence (AI)

**Technologies:** Python • OpenCV • Pytesseract • Tesseract OCR • NumPy

---

*Project 4 of 4 — Image & Text Recognition | Decode Labs AI Internship 2026*
