# backend/memory/firestore.py

from google.cloud import firestore


class FirestoreMemory:
    def __init__(self):
        self.db = firestore.Client()
        self.collection = "user_memory"

    def get_memory(self, user_id: str) -> dict:
        doc = self.db.collection(self.collection).document(user_id).get()
        if doc.exists:
            return doc.to_dict()
        return {"user_id": user_id, "corrections": {}, "style_notes": [], "past_notes_embeddings": []}

    def save_memory(self, user_id: str, data: dict):
        self.db.collection(self.collection).document(user_id).set(data, merge=True)

    def get_style_notes(self, user_id: str) -> list:
        memory = self.get_memory(user_id)
        return memory.get("style_notes", [])
