import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import time

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_number = filename.split("-")[0]

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=9, txt=f"Invoice #{invoice_number}", ln=1)

    pdf.set_font(family="Times", size=16)
    pdf.cell(w=50, h=9, txt=f"From {time.strftime("%b %d %Y")}")


    pdf.output(f"pdfs/invoice-{invoice_number}.pdf")
