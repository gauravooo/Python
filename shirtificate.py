# Program that generates a PDF "shirtificate" for a user who has taken CS50, using the fpdf library to create the PDF and add text and an image to it.
from fpdf import FPDF

name = input("Name: ")

class PDF(FPDF):
    def __init__(self, name):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 45)
        pdf.cell(0, 60, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=0, y=70)
        pdf.set_font_size(30)
        pdf.set_text_color(255,255,255)
        pdf.text(x=45, y=140, txt=f"{name} took CS50")
        pdf.output("shirtificate.pdf")

pdf = PDF(name)