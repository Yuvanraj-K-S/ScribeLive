# backend/models/schemas.py

from typing import List, Dict, Optional
from pydantic import BaseModel


# =========================
# Structured Extraction
# =========================

class Section(BaseModel):
    heading: str
    content: str
    equations: List[str] = []
    bullet_points: List[str] = []


class Definition(BaseModel):
    term: str
    meaning: str


class Formula(BaseModel):
    name: str
    expression: str
    description: str


class StructuredExtraction(BaseModel):
    title: str
    sections: List[Section]
    definitions: List[Definition] = []
    formulas: List[Formula] = []


# =========================
# Summary + Flashcards
# =========================

class SummaryResponse(BaseModel):
    summary: List[str]


class Flashcard(BaseModel):
    question: str
    answer: str


class FlashcardResponse(BaseModel):
    flashcards: List[Flashcard]


# =========================
# Diagram
# =========================

class DiagramResponse(BaseModel):
    diagram_type: str
    mermaid_code: str


# =========================
# Slides
# =========================

class Slide(BaseModel):
    title: str
    points: List[str]


class SlideResponse(BaseModel):
    slides: List[Slide]


# =========================
# Explanation
# =========================

class ExplanationResponse(BaseModel):
    explanation: str


# =========================
# Firestore Memory
# =========================

class MemorySchema(BaseModel):
    user_id: str
    corrections: Dict[str, str] = {}
    style_notes: List[str] = []
    past_notes_embeddings: List[List[float]] = []