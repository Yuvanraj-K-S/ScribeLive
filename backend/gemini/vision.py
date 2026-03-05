# backend/gemini/vision.py

import google.generativeai as genai
import json
import base64
from utils.prompts import VISION_EXTRACTION_PROMPT, build_style_injection


class GeminiVision:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def extract_from_image(self, image_bytes: bytes, style_notes: list[str] = []) -> dict:
        style_injection = build_style_injection(style_notes)
        full_prompt = style_injection + VISION_EXTRACTION_PROMPT

        image_part = {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(image_bytes).decode("utf-8")
        }

        response = self.model.generate_content([full_prompt, image_part])
        raw = response.text.strip()

        # Clean markdown fences if present
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]

        return json.loads(raw)
