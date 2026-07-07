from pathlib import Path
docs_path = Path("sample_data/docs")
documents = {}

for file in docs_path.glob("*.md"):
    documents[file.stem] = file.read_text(encoding="utf-8")

chunks = []

for file, content in documents.items():
    document_title = ""
    current_heading = ""
    current_content = []

    lines = content.splitlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("##"):
            if current_heading:
                chunks.append({
                    "document" : document_title,
                    "title" : current_heading,
                    "content" : "\n".join(current_content)
                })
            current_heading = line[2:].strip()
            current_content = []

        elif line.startswith("#"):
            document_title = line[1:].strip()
        else:
            current_content.append(line)    

    if current_heading:
        chunks.append({
            "document" : document_title,
            "title" : current_heading,
            "content" : "\n".join(current_content)
        })

if __name__ == "__main__":
    for chunk in chunks:
        print("=" * 60)
        print("Document :", chunk["document"])
        print("Title    :", chunk["title"])
        print("\nContent:")
        print(chunk["content"])
