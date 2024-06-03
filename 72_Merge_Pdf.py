# Write a program to merge multipe pdf file in one file using pypdf module

from pypdf import PdfWriter
import os


merger = PdfWriter()

pdfs = "E:/Python/Python/100-Days-of-Python-Programming/data/pdf/"
for pdf in os.listdir(pdfs):
    merger.append(pdfs + pdf)

merger.write("merged_data.pdf")
merger.close()