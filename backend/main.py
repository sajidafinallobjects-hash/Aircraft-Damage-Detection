from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

model = YOLO("yolov8n.pt")


@app.post("/upload")
async def upload_image(
    file: UploadFile = File(...)
):

    path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(path, "wb") as f:
        f.write(
            await file.read()
        )

    results = model(path)

    output = results[0].save()

    return {

        "saved": True,

        "processed": True,

        "image": file.filename
    }