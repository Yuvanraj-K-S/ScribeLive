# backend/services/pdf.py

import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Preformatted


class PDFService:
    """
    Converts LaTeX-style formatted text into a PDF using reportlab.
    """

    def generate_pdf(self, latex_text: str, output_path: str) -> str:
        """
        Generates a PDF file from formatted text.
        Returns the file path.
        """

        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        doc = SimpleDocTemplate(output_path)
        elements = []

        styles = getSampleStyleSheet()

        normal_style = styles["Normal"]
        heading_style = styles["Heading1"]

        code_style = ParagraphStyle(
            name="CodeStyle",
            parent=styles["Normal"],
            fontName="Courier",
            fontSize=10,
            textColor=colors.black,
        )

        lines = latex_text.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                elements.append(Spacer(1, 0.2 * inch))
                continue

            # Section
            if line.startswith("\\section*"):
                title = line.replace("\\section*{", "").replace("}", "")
                elements.append(Paragraph(title, heading_style))
                elements.append(Spacer(1, 0.3 * inch))

            # Subsection
            elif line.startswith("\\subsection*"):
                subtitle = line.replace("\\subsection*{", "").replace("}", "")
                elements.append(Paragraph(subtitle, styles["Heading2"]))
                elements.append(Spacer(1, 0.2 * inch))

            # Equation
            elif "\\begin{equation}" in line or "\\end{equation}" in line:
                continue

            elif line.startswith("\\item"):
                bullet_text = line.replace("\\item", "").strip()
                elements.append(Paragraph(f"• {bullet_text}", normal_style))

            elif line.startswith("\\textbf"):
                clean = line.replace("\\textbf{", "").replace("}", "")
                elements.append(Paragraph(f"<b>{clean}</b>", normal_style))

            else:
                elements.append(Paragraph(line, normal_style))

        doc.build(elements)

        return output_path