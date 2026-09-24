"""
Project 4: Image & Text Recognition (OCR)
Decode Labs AI Internship - Batch 2026
Libraries: OpenCV, Pytesseract
"""

import cv2
import pytesseract
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_image(image_path):
    """Pre-process image for better OCR accuracy"""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image: {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return image, gray, thresh


def extract_text(image_path):
    """Extract text from image using Tesseract OCR"""
    print("=" * 50)
    print("📄 OCR TEXT EXTRACTION")
    print("=" * 50)
    
    original, gray, thresh = preprocess_image(image_path)
    print(f"\n🖼️  Processing: {image_path}")
    
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresh, config=custom_config)
    
    data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
    confidences = [int(conf) for conf in data['conf'] if int(conf) > 0]
    avg_confidence = np.mean(confidences) if confidences else 0
    
    print(f"\n📝 Extracted Text:")
    print("-" * 50)
    print(text if text.strip() else "[No text detected]")
    print("-" * 50)
    print(f"\n📊 Average Confidence: {avg_confidence:.2f}%")
    
    # Save processed images
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    cv2.imwrite(f"{base_name}_gray.jpg", gray)
    cv2.imwrite(f"{base_name}_threshold.jpg", thresh)
    print(f"💾 Saved: {base_name}_gray.jpg, {base_name}_threshold.jpg")
    
    return text, avg_confidence


def create_test_image():
    """Create a simple test image with text"""
    img = np.ones((200, 600, 3), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'Hello Decode Labs!', (50, 80), font, 1.5, (0, 0, 0), 3)
    cv2.putText(img, 'AI Internship 2026', (50, 150), font, 1.2, (255, 0, 0), 2)
    cv2.imwrite('test_image.jpg', img)
    print("✅ Created test image: test_image.jpg")
    return 'test_image.jpg'


def main():
    print("=" * 50)
    print("🔍 IMAGE TEXT RECOGNITION (OCR)")
    print("=" * 50)
    print("\n⚠️  Install Tesseract OCR engine first!")
    print("   Linux: sudo apt-get install tesseract-ocr")
    print("   Mac: brew install tesseract")
    print("   Windows: https://github.com/UB-Mannheim/tesseract/wiki")
    
    test_image = create_test_image()
    extract_text(test_image)
    
    print("\n" + "=" * 50)
    print("🎉 PROJECT 4 COMPLETED SUCCESSFULLY!")
    print("=" * 50)


if __name__ == "__main__":
    main()