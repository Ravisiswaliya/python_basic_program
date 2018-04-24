import fpdf
from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial', 'B',24)

pdf.cell(40,10, 'This is pdf using python')
pdf.output('f.pdf', 'F')
