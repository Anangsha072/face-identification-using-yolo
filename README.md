# 🎯 Face Recognition from Video using YOLOv8 & InsightFace

This project performs **real-time face recognition from video footage** by combining:
- **YOLOv8** for person detection
- **InsightFace / Face Recognition** for identity matching
- **SQLite** for user metadata storage
This project demonstrates a face recognition system using YOLO (You Only Look Once) for detecting faces. It performs the following tasks:

Dataset Preparation – A small dataset of 15 images is used to train the system( 5 images per person).

Database Creation – Stores name, age, and gender of each person in the dataset.

Face Detection on Video – Detects faces from a video input and retrieves the corresponding information from the database in real-time.

It is designed for **CCTV-style video analysis**, also ideal for applications like attendance systems, security monitoring, and personalized video analytics, providing instant recognition and metadata display for each detected face..

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

<img width="356" height="253" alt="image" src="https://github.com/user-attachments/assets/465d9551-2df6-4001-aaaa-306a9775e7ba" />



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

![ezgif com-crop (1)](https://github.com/user-attachments/assets/27728e93-d7b9-4deb-a4fd-edf63678acab)





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
