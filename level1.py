# Basic Idea
# -----------------------------
# Take a PDF file path as input
# Extract text
# Print or save text to a .txt file
# -----------------------------
import os
import pdfplumber


def extract_text_from_pdf(pdf_path, output_path):
    extracted_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Total Pages Found: {len(pdf.pages)}")

            for page_number, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()

                if text:
                    extracted_text += f"\n----- Page {page_number} -----\n"
                    extracted_text += text + "\n"

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(extracted_text)

        print(f"\n✅ Text saved to: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":

    # Get project root directory dynamically
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Sample PDFs folder inside project
    sample_folder = os.path.join(BASE_DIR, "Sample PDFs")

    # Output folder inside project
    output_folder = os.path.join(BASE_DIR, "output")

    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    pdf_filename = input("Enter PDF file name (example: sample.pdf): ")

    pdf_path = os.path.join(sample_folder, pdf_filename)
    output_path = os.path.join(output_folder, "output.txt")

    if not os.path.exists(pdf_path):
        print("❌ File not found inside Sample PDFs folder.")
    else:
        extract_text_from_pdf(pdf_path, output_path)