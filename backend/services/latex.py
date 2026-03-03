# backend/services/latex.py

from models.schemas import StructuredExtraction


class LaTeXService:
    """
    Converts structured extracted notes into LaTeX-style formatted text.
    This is intermediate representation before PDF generation.
    """

    def generate_latex(self, data: StructuredExtraction) -> str:
        """
        Convert StructuredExtraction into LaTeX formatted string.
        """

        latex_content = []

        # Title
        latex_content.append(f"\\section*{{{data.title}}}\n")

        # Sections
        for section in data.sections:
            latex_content.append(f"\\subsection*{{{section.heading}}}\n")

            if section.content:
                latex_content.append(section.content + "\n")

            # Bullet Points
            if section.bullet_points:
                latex_content.append("\\begin{itemize}")
                for point in section.bullet_points:
                    latex_content.append(f"  \\item {point}")
                latex_content.append("\\end{itemize}\n")

            # Equations
            for equation in section.equations:
                latex_content.append("\\begin{equation}")
                latex_content.append(equation)
                latex_content.append("\\end{equation}\n")

        # Definitions
        if data.definitions:
            latex_content.append("\\section*{Definitions}")
            for definition in data.definitions:
                latex_content.append(f"\\textbf{{{definition.term}}}: {definition.meaning} \\\\")

        # Formulas
        if data.formulas:
            latex_content.append("\n\\section*{Formulas}")
            for formula in data.formulas:
                latex_content.append(f"\\textbf{{{formula.name}}}")
                latex_content.append("\\begin{equation}")
                latex_content.append(formula.expression)
                latex_content.append("\\end{equation}")
                latex_content.append(f"{formula.description} \n")

        return "\n".join(latex_content)