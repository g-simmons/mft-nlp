import subprocess
import os
from pathlib import Path

# pdftoppm -png -f 1 -l 1 assets/pdf/moral_foundations_reddit_corpus.pdf assets/img/preview/moral_foundations_reddit_corpus

def make_preview(pdf_path, preview_path, start_page: int, stop_page: int):
    cmd = ["pdftoppm", "-png", "-f", str(start_page), "-l", str(stop_page), pdf_path, preview_path]
    subprocess.run(cmd)

def main():
    pdf_paths = list(Path("../assets/pdf").glob("*.pdf"))
    for pdf_path in pdf_paths:
        print(pdf_path)
        preview_path = Path("../assets/img/preview") / pdf_path.stem
        print(preview_path)
        if not (preview_path / "-01.png").exists():
            make_preview(str(pdf_path), str(preview_path), 1, 1)
    
if __name__ == "__main__":
    main()

