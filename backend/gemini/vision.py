# backend/gemini/vision.py

import json
import base64
from google import genai
from google.genai import types
from utils.prompts import VISION_EXTRACTION_PROMPT, build_style_injection


class GeminiVision:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def extract_from_image(self, image_bytes: bytes, style_notes: list[str] = []) -> dict:
        style_injection = build_style_injection(style_notes)
        full_prompt = style_injection + VISION_EXTRACTION_PROMPT

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
                full_prompt
            ]
        )

        raw = response.text.strip()

        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]

        return json.loads(raw)
