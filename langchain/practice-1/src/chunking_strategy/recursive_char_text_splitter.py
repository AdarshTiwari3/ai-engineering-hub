from langchain_text_splitters import RecursiveCharacterTextSplitter
from chunking_strategy.data_loader import load_text_file


def run_recursive_splitter(
    file_name: str = "sample_text.txt",
    chunk_size: int = 200,
    chunk_overlap: int = 50,
    separators: list[str] | None = None,
):
    """
    Load a text file and split it into chunks using RecursiveCharacterTextSplitter.

    Args:
        file_name: Input text file name.
        chunk_size: Maximum size of each chunk (in characters).
        chunk_overlap: Number of overlapping characters between chunks.
        separators: Optional list of separators used for recursive splitting.
                    Default uses LangChain's built-in separator hierarchy.
    """

    text = load_text_file(file_name)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=separators,
    )

    chunks = splitter.split_text(text)

    print("====================================================")
    print("RECURSIVE SPLITTER")
    print("====================================================")
    print("Input file:", file_name)
    print("Total chunks:", len(chunks))

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {index} ({len(chunk)} characters) ---")
        print(chunk)

    return chunks


if __name__ == "__main__":
    run_recursive_splitter(separators=["\n\n", "\n", " "])

# Recursive splitting strategy:
# 1. The splitter first attempts to split text using "\n\n" (paragraph boundaries).
# 2. If any resulting chunk exceeds the configured chunk_size, that chunk is
#    recursively split using the next separator ("\n").
# 3. If the chunk is still too large, it is further split using the next separator (" ").
# 4. This continues until all chunks satisfy the size constraint.
# Smaller chunks are preserved and not re-split unnecessarily.
