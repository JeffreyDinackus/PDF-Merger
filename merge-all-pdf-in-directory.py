import os
import fitz  # PyMuPDF


def merge_pdfs_in_directory(input_dir, output_file):
    pdf_files = get_pdf_files(input_dir)
    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    pdf_writer = fitz.open()

    for pdf_file in pdf_files:
        pdf_doc = fitz.open(pdf_file)
        pdf_writer.insert_pdf(pdf_doc)
        pdf_doc.close()

    # Create the output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    pdf_writer.save(output_file)
    pdf_writer.close()

    print(f"All PDFs merged successfully into '{output_file}'.")


def get_pdf_files(directory):
    pdf_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files


if __name__ == "__main__":
    input_directory = "/home/blackjack/Desktop/git/pdf/input"  # Replace this with the desired input directory
    output_file_path = "/home/blackjack/Desktop/git/pdf/output/output.pdf"  # Replace this with the desired output file path

    print("Input Directory:", input_directory)
    print("Output File Path:", output_file_path)

    merge_pdfs_in_directory(input_directory, output_file_path)