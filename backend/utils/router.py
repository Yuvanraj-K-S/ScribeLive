# backend/utils/router.py


class ActionRouter:
    """
    Simple rule-based router.
    Maps frontend action strings to backend service handlers.
    """

    def route(self, action: str) -> str:
        """
        Returns the service name based on user action.
        """

        action = action.lower().strip()

        if action == "generate_slides":
            return "slides"

        elif action == "generate_diagram":
            return "diagram"

        elif action == "make_flashcards":
            return "flashcards"

        elif action == "generate_summary":
            return "summary"

        elif action == "explain":
            return "explanation"

        else:
            raise ValueError(f"Unknown action: {action}")