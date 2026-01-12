import cv2
import pickle
import sqlite3
import numpy as np
from ultralytics import YOLO
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity

# Models
yolo = YOLO("yolov8n.pt")
face_app = FaceAnalysis(name="buffalo_l")
face_app.prepare(ctx_id=0, det_size=(640, 640))

# Load embeddings
with open("encodings_insightface.pkl", "rb") as f:
    data = pickle.load(f)

known_embeddings = np.array(data["embeddings"])
known_names = data["names"]

# DB
conn = sqlite3.connect("users_face.db")
cursor = conn.cursor()

def recognize_face(embedding):
    sims = cosine_similarity([embedding], known_embeddings)[0]
    best = np.argmax(sims)
    if sims[best] > 0.45:   # VIDEO SAFE THRESHOLD
        return known_names[best], sims[best]
    return "Unknown", 0

video = cv2.VideoCapture("video3.mp4")

while True:
    ret, frame = video.read()
    if not ret:
        break

    results = yolo(frame, conf=0.4)[0]

    for box in results.boxes:
        if yolo.names[int(box.cls)] != "person":
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        if x2 - x1 < 80 or y2 - y1 < 80:
            continue

        crop = frame[y1:y2, x1:x2]
        faces = face_app.get(crop)

        for face in faces:
            name, score = recognize_face(face.embedding)

            label = name
            if name != "Unknown":
                cursor.execute("SELECT age, sex FROM People WHERE name=?", (name,))
                row = cursor.fetchone()
                if row:
                    label = f"{name}, {row[0]}, {row[1]} ({int(score*100)}%)"

            fx1, fy1, fx2, fy2 = map(int, face.bbox)
            fx1 += x1; fx2 += x1
            fy1 += y1; fy2 += y1

            color = (0,255,0) if name != "Unknown" else (0,0,255)
            cv2.rectangle(frame, (fx1,fy1), (fx2,fy2), color, 2)
            cv2.putText(frame, label, (fx1, fy1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("InsightFace Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
conn.close()













