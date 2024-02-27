import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import time

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    filename = Path(filepath).stem
    invoice_number = filename.split("-")[0]

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=9, txt=f"Invoice #{invoice_number}", ln=1)

    pdf.set_font(family="Times", size=16)
    pdf.cell(w=50, h=9, txt=f"From {time.strftime("%b %d, %Y")}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    headers = df.columns
    headers = [item.replace("_", " ").title() for item in headers]

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt=headers[0], border=1)
    pdf.cell(w=70, h=8, txt=headers[1], border=1)
    pdf.cell(w=40, h=8, txt=headers[2], border=1)
    pdf.cell(w=30, h=8, txt=headers[3], border=1)
    pdf.cell(w=25, h=8, txt=headers[4], border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=25, h=8, txt=str(row["total_price"]), border=1, ln=1)





    pdf.output(f"pdfs/invoice-{invoice_number}.pdf")
