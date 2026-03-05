# backend/gemini/text.py

import json
from google import genai
from utils.prompts import SUMMARY_PROMPT, FLASHCARD_PROMPT, DIAGRAM_PROMPT, SLIDE_PROMPT, EXPLANATION_PROMPT


class GeminiText:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def _call(self, prompt: str, content: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt + "\n\n" + content
        )
        raw = response.text.strip()
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        return raw

    def generate_summary(self, content: str) -> dict:
        return json.loads(self._call(SUMMARY_PROMPT, content))

    def generate_flashcards(self, content: str) -> dict:
        return json.loads(self._call(FLASHCARD_PROMPT, content))

    def generate_diagram(self, content: str) -> dict:
        return json.loads(self._call(DIAGRAM_PROMPT, content))

    def generate_slides(self, content: str) -> dict:
        return json.loads(self._call(SLIDE_PROMPT, content))

    def explain(self, content: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=EXPLANATION_PROMPT + "\n\n" + content
        )
        return response.text.strip()
