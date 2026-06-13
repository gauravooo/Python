# Program that generates a PDF "shirtificate" for a user who has taken CS50, using the fpdf library to create the PDF and add text and an image to it.
from fpdf import FPDF


class Shirtificate(FPDF):
    """Generate a CS50 shirtificate PDF for a given student name."""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def generate(self): # Function to generate the shirtificate PDF
        """Create and output the shirtificate PDF."""
        self.add_page()
        self.set_font("helvetica", "B", 45)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.image("shirtificate.png", x=0, y=70)
        self.set_font_size(30)
        self.set_text_color(255, 255, 255)
        self.text(x=45, y=140, txt=f"{self.name} took CS50")
        self.output("shirtificate.pdf")


if __name__ == "__main__":
    name = input("Name: ")
    shirtificate = Shirtificate(name)
    shirtificate.generate()