#!/usr/bin/python3

# Importing the required modules
import time
import PyPDF2

def merge_pdfs(input_files, output_file):
    pdf_merger = PyPDF2.PdfMerger()

    for file in input_files:
        with open(file, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_file, 'wb') as merged_pdf:
        pdf_merger.write(merged_pdf)

def main():
  print("Welcome to PDF Merger!")
  time.sleep(1)
  print("Make sure that the PDFs you want to merge are in the same folder as this program.")
  time.sleep(1)
  print("Please enter the names of the PDFs you want to merge, in the order you want them to be merged.")
  print("For example, if you want to merge 'file1.pdf' and 'file2.pdf' with 'file1.pdf' first, enter 'file1.pdf file2.pdf'.")
  time.sleep(1)

  fiel1 = input("Enter the name of the file you want to go first in the merged PDF: ")
  file2 = input("Enter the name of the file you want to go second in the merged PDF: ")

  merge_pdfs([fiel1, file2], output_file="merged.pdf")
  print("Merged PDF saved as 'merged.pdf'.")
  time.sleep(1)
  print("Thank you for using PDF Merger!")
  print("Exiting...")
  exit()

if __name__ == "__main__":
    main()
   