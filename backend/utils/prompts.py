# backend/utils/prompts.py


# ==========================================
# 1️⃣ Vision Extraction Prompt
# ==========================================

VISION_EXTRACTION_PROMPT = """
You are an academic note extraction system.

Your task:
Extract structured academic content from the provided handwritten image.

Return STRICT JSON.
Do NOT include commentary.
Do NOT include markdown.
Do NOT explain anything.
Return valid JSON only.

Rules:
- Preserve hierarchy.
- Separate equations into the "equations" array.
- Extract bullet points separately.
- Extract definitions separately.
- Extract formulas separately.
- Keep mathematical expressions clean and readable.

Follow this exact schema:

{
  "title": "",
  "sections": [
    {
      "heading": "",
      "content": "",
      "equations": [],
      "bullet_points": []
    }
  ],
  "definitions": [
    {
      "term": "",
      "meaning": ""
    }
  ],
  "formulas": [
    {
      "name": "",
      "expression": "",
      "description": ""
    }
  ]
}
"""


# ==========================================
# 2️⃣ Summary Prompt
# ==========================================

SUMMARY_PROMPT = """
You are an academic summarization assistant.

Generate a concise, structured academic summary.

Rules:
- Bullet format only
- Clear and formal tone
- Avoid repetition
- Highlight key concepts and formulas
- Maximum 10 bullets

Return JSON:

{
  "summary": []
}
"""


# ==========================================
# 3️⃣ Flashcard Prompt
# ==========================================

FLASHCARD_PROMPT = """
You are a study assistant.

Generate flashcards from the structured academic content.

Rules:
- Mix conceptual and formula recall questions
- Avoid trivial questions
- Encourage deep understanding
- Answers should be precise

Return JSON:

{
  "flashcards": [
    {
      "question": "",
      "answer": ""
    }
  ]
}
"""


# ==========================================
# 4️⃣ Diagram Prompt
# ==========================================

DIAGRAM_PROMPT = """
Generate a conceptual diagram in Mermaid format.

Rules:
- Choose appropriate diagram_type (flowchart, sequence, graph, etc.)
- Return valid Mermaid syntax
- Do not include explanations
- Return JSON only

{
  "diagram_type": "",
  "mermaid_code": ""
}
"""


# ==========================================
# 5️⃣ Slide Generator Prompt
# ==========================================

SLIDE_PROMPT = """
Generate academic presentation slides.

Rules:
- Each slide max 6 bullet points
- Clear slide titles
- Logical progression
- Avoid paragraphs

Return JSON:

{
  "slides": [
    {
      "title": "",
      "points": []
    }
  ]
}
"""


# ==========================================
# 6️⃣ Explanation Prompt
# ==========================================

EXPLANATION_PROMPT = """
Explain the following section in simple and intuitive terms.

Rules:
- Beginner-friendly
- Use analogies if useful
- Preserve technical correctness
- Do not oversimplify equations

Return plain text explanation only.
"""


# ==========================================
# 7️⃣ Style Adaptation Injection Template
# ==========================================

def build_style_injection(style_notes: list[str]) -> str:
    """
    Dynamically inject user handwriting/style characteristics
    before Vision extraction prompt.
    """
    if not style_notes:
        return ""

    style_text = "\n".join([f"- {note}" for note in style_notes])

    injection = f"""
The user has the following handwriting characteristics:

{style_text}

Interpret carefully and contextually.
Preserve meaning over literal character recognition.
"""

    return injection