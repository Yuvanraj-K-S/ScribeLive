# backend/main.py

import os
import json
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from dotenv import load_dotenv

from gemini.vision import GeminiVision
from gemini.text import GeminiText
from services.latex import LaTeXService
from services.pdf import PDFService
from services.slides import SlideService
from services.diagram import DiagramService
from models.schemas import StructuredExtraction

load_dotenv()

app = FastAPI(title="ScribeLive API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("GEMINI_API_KEY")

vision = GeminiVision(API_KEY)
text_ai = GeminiText(API_KEY)
latex_svc = LaTeXService()
pdf_svc = PDFService()
slide_svc = SlideService()
diagram_svc = DiagramService()


@app.get("/")
def root():
    return {"status": "ScribeLive API running"}


@app.post("/extract")
async def extract(file: UploadFile = File(...), user_id: str = Form(default="default")):
    image_bytes = await file.read()
    extracted = vision.extract_from_image(image_bytes)
    return JSONResponse(content=extracted)


@app.post("/generate-pdf")
async def generate_pdf(file: UploadFile = File(...)):
    image_bytes = await file.read()
    extracted = vision.extract_from_image(image_bytes)
    data = StructuredExtraction(**extracted)
    latex_text = latex_svc.generate_latex(data)
    output_path = "/tmp/output/notes.pdf"
    pdf_svc.generate_pdf(latex_text, output_path)
    return FileResponse(output_path, media_type="application/pdf", filename="notes.pdf")


@app.post("/summary")
async def summary(file: UploadFile = File(...)):
    image_bytes = await file.read()
    extracted = vision.extract_from_image(image_bytes)
    result = text_ai.generate_summary(json.dumps(extracted))
    return JSONResponse(content=result)


@app.post("/flashcards")
async def flashcards(file: UploadFile = File(...)):
    image_bytes = await file.read()
    extracted = vision.extract_from_image(image_bytes)
    result = text_ai.generate_flashcards(json.dumps(extracted))
    return JSONResponse(content=result)


@app.post("/diagram")
async def diagram(file: UploadFile = File(...)):
    image_bytes = await file.read()
    extracted = vision.extract_from_image(image_bytes)
    result = text_ai.generate_diagram(json.dumps(extracted))
    diagram_data = diagram_svc.build_diagram(result)
    return JSONResponse(content=diagram_data)


@app.post("/slides")
async def slides(file: UploadFile = File(...)):
    image_bytes = await file.read()
    extracted = vision.extract_from_image(image_bytes)
    result = text_ai.generate_slides(json.dumps(extracted))
    output_path = "/tmp/output/slides.pptx"
    slide_svc.generate_pptx(result, output_path)
    return FileResponse(output_path, filename="slides.pptx")


@app.post("/explain")
async def explain(file: UploadFile = File(...)):
    image_bytes = await file.read()
    extracted = vision.extract_from_image(image_bytes)
    result = text_ai.explain(json.dumps(extracted))
    return JSONResponse(content={"explanation": result})
```

---

### FILE 7 — `backend/requirements.txt` (create this new file)
```
fastapi
uvicorn
python-dotenv
google-generativeai
google-cloud-firestore
reportlab
python-pptx
python-multipart
```

---

### FILE 8 — `.env` (create at root, **never commit this**)
```
GEMINI_API_KEY=your_api_key_here
