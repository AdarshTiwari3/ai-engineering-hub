from pathlib import Path


def load_text_file(file_name: str) -> str:
    """
    Load a text file from the chunking directory and return its contents.
    """
    base_dir = Path(__file__).parent
    file_path = base_dir / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return file_path.read_text(encoding="utf-8")
