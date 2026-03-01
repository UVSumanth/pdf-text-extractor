# PDF Text Extractor Project Documentation

## Project Overview

This project extracts text from **text-based PDF documents** using
Python and saves the extracted content into a `.txt` file.

It uses the `pdfplumber` library to parse the PDF structure and
reconstruct readable text.

---

## Project Flow

**Input → Process → Output**

1.  Accept PDF file path as input
2.  Open PDF using pdfplumber
3.  Iterate through each page
4.  Extract text from each page
5.  Save extracted text into a `.txt` file

---

## Core Concepts Learned

### 1. PDF is a Visual Format

PDF files store: - Characters - Coordinates (x, y positions) - Font
information

They do NOT store: - Paragraph meaning - Mathematical structure - Semantic information

This is why math formatting may break during extraction.

---

### 2. Why We Use pdfplumber

Normal Python file reading cannot extract meaningful text from PDFs
because PDFs are binary structured files.

`pdfplumber`: - Parses PDF objects - Reads positioned text - Reconstructs reading order - Returns text as a string

---

## How the Code Works

### Step 1: Import Libraries

-   `os` → Handles file paths
-   `pdfplumber` → Extracts text from PDF

### Step 2: Open PDF

The script opens the PDF using:

    with pdfplumber.open(pdf_path) as pdf:

This reads the internal PDF structure.

### Step 3: Iterate Pages

    for page in pdf.pages:

Each page is processed individually.

### Step 4: Extract Text

    text = page.extract_text()

This reconstructs visible text from character positions.

### Step 5: Write Output

The extracted text is written into a `.txt` file using UTF-8 encoding.

---

## Limitations

1.  ❌ Does NOT support scanned PDFs (image-only PDFs)
2.  ❌ Mathematical expressions may lose formatting
3.  ❌ Superscripts and subscripts become normal characters
4.  ❌ Fractions may not render properly
5.  ❌ Multi-column layouts may merge text incorrectly
6.  ❌ Tables are not reconstructed structurally

---

## Example of Math Limitation

Original PDF: - 1² - √2 - 1/2

Extracted Output: - 12 - √ 2 - 1 2

Reason: PDF stores visual positioning, not semantic math structure.

---

## Key Takeaways

-   PDF extraction is reconstruction, not perfect copying.
-   Text-based PDFs work well.
-   Complex formatting degrades naturally.
-   Libraries are required for structured file formats.
-   Proper file handling and encoding are important.

---

## Confidence Summary

This project demonstrates understanding of:

-   File handling in Python
-   Structured binary formats
-   Library usage and limitations
-   Unicode handling
-   Real-world data imperfections
-   Clean program structure

