from langchain_text_splitters import CharacterTextSplitter
from chunking_strategy.data_loader import load_text_file


def run_character_splitter(
    file_name: str = "sample_text.txt",
    chunk_size: int = 300,
    chunk_overlap: int = 50,
    separator: str = "\n",
):
    """
    Load a text file and split it into chunks using CharacterTextSplitter.

    Args:
        file_name: Input text file name.
        chunk_size: Maximum size of each chunk (in characters).
        chunk_overlap: Number of overlapping characters between chunks.
        separator: Character used to split text.
    """

    text = load_text_file(file_name)

    splitter = CharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separator=separator,
    )

    chunks = splitter.split_text(text)

    print("====================================================")
    print("CHARACTER SPLITTER")
    print("====================================================")
    print("Input file:", file_name)
    print("Total chunks:", len(chunks))

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {index} ({len(chunk)} characters) ---")
        print(chunk)

    return chunks


if __name__ == "__main__":
    run_character_splitter()
