import os
from docx import Document
import json

from docx.shared import RGBColor

def is_bold(paragraph):
    # Check if any run is bold in the paragraph
    for run in paragraph.runs:
        if run.bold:
            return True
    return False

def extract_text_by_sections(doc_path):
    doc = Document(doc_path)
    sections = []
    current_section_title = None
    current_text = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            # Empty paragraph signals section break if text exists
            if current_section_title and current_text:
                sections.append({
                    "section": current_section_title,
                    "content": "\n".join(current_text).strip()
                })
                current_section_title = None
                current_text = []
            continue

        # Check for heading style
        if para.style.name.startswith('Heading') and text:
            if current_section_title:
                sections.append({
                    "section": current_section_title,
                    "content": "\n".join(current_text).strip()
                })
            current_section_title = text
            current_text = []
        # Or check if paragraph is bold, treat as section title
        elif is_bold(para):
            if current_section_title:
                sections.append({
                    "section": current_section_title,
                    "content": "\n".join(current_text).strip()
                })
            current_section_title = text
            current_text = []
        else:
            if not current_section_title:
                current_section_title = "Introduction"
            current_text.append(text)

    if current_section_title and current_text:
        sections.append({
            "section": current_section_title,
            "content": "\n".join(current_text).strip()
        })

    return sections

def chunk_text(text, max_words=300):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i+max_words])
        chunks.append(chunk)
    return chunks

def process_docs(doc_dir):
    all_docs_data = []
    for filename in os.listdir(doc_dir):
        if filename.endswith(".docx"):
            doc_path = os.path.join(doc_dir, filename)
            print(f"Processing {doc_path}...")
            sections = extract_text_by_sections(doc_path)
            chunk_id = 1
            for section in sections:
                chunks = chunk_text(section["content"])
                for chunk in chunks:
                    all_docs_data.append({
                        "document": filename,
                        "section": section["section"],
                        "chunk_id": chunk_id,
                        "content": chunk
                    })
                    chunk_id += 1
    return all_docs_data

if __name__ == "__main__":
    doc_directory = r"app\src\static"  # Your path here, raw string to avoid escape issues

    data = process_docs(doc_directory)

    with open("processed_hoi_documents.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Processed data saved to processed_hoi_documents.json")
