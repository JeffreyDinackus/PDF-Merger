#!/usr/bin/python3

# Importing the required modules
import time
import fitz  # PyMuPDF

def merge_pdfs(input_paths, output_path):
    pdf_writer = fitz.open()

    for path in input_paths:
        pdf_reader = fitz.open(path)
        pdf_writer.insert_pdf(pdf_reader)
        pdf_reader.close()

    pdf_writer.save(output_path)
    pdf_writer.close()

def main():
    print("Welcome to PDF Merger!")
    time.sleep(1)
    print("Make sure that the PDFs you want to merge are in the same folder as this program.")
    time.sleep(1)
    print("Please enter the names of the PDFs you want to merge, in the order you want them to be merged.")
    print("For example, if you want to merge 'file1.pdf' and 'file2.pdf' with 'file1.pdf' first, enter 'file1.pdf file2.pdf'.")
    time.sleep(1)

    file1 = input("Enter the name of the first PDF: ")
    file2 = input("Enter the name of the second PDF: ")
    input_files = [file1, file2]
    output_file = "merged_output.pdf"

    merge_pdfs(input_files, output_file)
    print("Merged PDF saved as 'merged.pdf'.")
    time.sleep(1)
    print("Thank you for using PDF Merger!")
    print("Exiting...")
    exit()

if __name__ == "__main__":
    main()
   