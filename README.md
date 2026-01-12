# 🎯 Face Recognition from Video using YOLOv8 & InsightFace

This project performs **real-time face recognition from video footage** by combining:
- **YOLOv8** for person detection
- **InsightFace / Face Recognition** for identity matching
- **SQLite** for user metadata storage

It is designed for **CCTV-style video analysis**.

---

## 🚀 Features

- Detects people using YOLOv8
- Extracts faces from detected persons
- Matches faces with trained dataset
- Displays name, age, gender, and confidence
- Supports multiple images per person
- Works on CPU (no GPU required)

---

## 📁 Project Structure

face-trainer-project/
│
├── dataset/ # Face images
├── database.py # SQLite database creation
├── insert_users.py # Insert users into database
├── train_model.py # Train face encodings
├── recognize.py # Video face recognition
├── requirements.txt
└── README.md


## 🖼️ Dataset Format

Images must be named like:

Example:
User.1.1.jpg
User.1.2.jpg
User.2.1.jpg


Minimum **5 images per person** recommended.

---

## Result

![WhatsApp Image 2026-01-12 at 1 55 20 PM](https://github.com/user-attachments/assets/3e03272a-f0c8-4ce4-bd46-37f4c336a8c4)




## 📊 Confidence Explanation

Confidence is based on face embedding similarity, not detection quality.

50–60% → Acceptable match

65–75% → Strong match

80%+ → Very strong match

Lower confidence in videos is normal due to lighting, motion blur, and angle differences.

## 🛠️ Tech Stack

Python

OpenCV

YOLOv8 (Ultralytics)

InsightFace

SQLite

NumPy

📌 Notes

GPU is optional

Video files are not included in this repository

Dataset images are not included for privacy reasons

## 📜 License

This project is for educational and research purposes.
