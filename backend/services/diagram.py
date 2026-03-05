# backend/services/diagram.py

class DiagramService:
    def build_diagram(self, diagram_data: dict) -> dict:
        return {
            "diagram_type": diagram_data.get("diagram_type", "flowchart"),
            "mermaid_code": diagram_data.get("mermaid_code", "")
        }
