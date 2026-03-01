# Basic Idea
# -----------------------------
# Take a PDF file path as input
# Extract text
# Print or save text to a .txt file
# -----------------------------
import os
import pdfplumber

def extract_text_from_pdf(pdf_path, output_path):
    """
    Extracts text from a text-based PDF and writes it to a .txt file.
    """
    extracted_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Total Pages Found: {len(pdf.pages)}")

            for page_number, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()

                if text:
                    extracted_text += f"\n----- Page {page_number} -----\n"
                    extracted_text += text + "\n"
                else:
                    print(f"Warning: Page {page_number} contains no extractable text.")

        # Writing extracted text to output file
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(extracted_text)

        print(f"\n✅ Text successfully extracted and saved to:\n{output_path}")

    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":

    # Absolute folder path (your provided path)
    base_folder = r"C:\Users\uppal\PycharmProjects\pdf-text-extractor\Sample PDFs"

    # Ask user for PDF file name only
    pdf_filename = input("Enter PDF file name (example: sample.pdf): ")

    # Construct full PDF path safely
    pdf_path = os.path.join(base_folder, pdf_filename)

    # Output file in same folder
    output_path = os.path.join(base_folder, "output.txt")

    # Validate PDF existence
    if not os.path.exists(pdf_path):
        print("❌ File not found. Please check the file name.")
    else:
        extract_text_from_pdf(pdf_path, output_path)
