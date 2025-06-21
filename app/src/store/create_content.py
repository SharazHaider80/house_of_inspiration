import os
from docx import Document
import json

def get_full_text(doc_path):
    doc = Document(doc_path)
    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():
            full_text.append(para.text.strip())
    return "\n".join(full_text)

def process_docs_raw(doc_dir):
    all_docs_data = []
    for filename in os.listdir(doc_dir):
        if filename.endswith(".docx"):
            doc_path = os.path.join(doc_dir, filename)
            print(f"Processing {doc_path}...")
            content = get_full_text(doc_path)
            all_docs_data.append({
                "document": filename,
                "content": content
            })
    return all_docs_data

if __name__ == "__main__":
    doc_directory = r"app\src\static"  # Adjust path if needed

    data = process_docs_raw(doc_directory)

    with open("processed_docs_full_content.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Processed full content saved to processed_docs_full_content.json")
