import os
import cv2
import pickle
import sqlite3
from insightface.app import FaceAnalysis

DATASET = "dataset"

# Load DB (ID → Name mapping)
conn = sqlite3.connect("users_face.db")
cursor = conn.cursor()
cursor.execute("SELECT id, name FROM People")
id_to_name = {str(row[0]): row[1] for row in cursor.fetchall()}
conn.close()

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0, det_size=(640, 640))

embeddings = []
names = []

for file in os.listdir(DATASET):
    if not file.lower().endswith(".jpg"):
        continue

    try:
        person_id = file.split(".")[1]   # User.1.3.jpg → "1"
        name = id_to_name.get(person_id)
        if name is None:
            continue
    except:
        continue

    img_path = os.path.join(DATASET, file)
    img = cv2.imread(img_path)
    if img is None:
        continue

    faces = app.get(img)
    if len(faces) == 0:
        print(f"[WARN] No face in {file}")
        continue

    embeddings.append(faces[0].embedding)
    names.append(name)

print(f"[INFO] Trained on {len(embeddings)} images")

with open("encodings_insightface.pkl", "wb") as f:
    pickle.dump({"embeddings": embeddings, "names": names}, f)

print("[INFO] Model saved successfully")
 














