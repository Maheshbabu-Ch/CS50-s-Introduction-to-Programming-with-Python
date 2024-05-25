from fpdf import FPDF
from fpdf.enums import Align

class ShirtificatePDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", format="A4")

    def generate(self, name):
        self.add_page()
        self.set_font("Arial", size=50)
        self.cell(200, 40, txt="CS50 Shirtificate", ln=True, align='C')
        self.image("shirtificate.png", x= Align.C, w=190)
        self.set_font("Arial", size=24)
        self.set_text_color(255, 255, 255)
        self.set_y(120)
        self.cell(0, txt=f"{name} took CS50", align='C')
        self.output("shirtificate.pdf")

if __name__ == "__main__":
    shirt_pdf = ShirtificatePDF()
    shirt_pdf.generate(input("Name: "))
