from pathlib import Path
from PIL import Image
from pypdf import PdfReader

def read_file_signature(file_path: str) -> bytes:
    path = Path(file_path)

    # Check whether the path exists.
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    # Check whether it is a file rather than a folder.
    if not path.is_file():
        raise ValueError(f"Expected a file, but received: {path}")

    # An empty file has no content to inspect.
    if path.stat().st_size == 0:
        raise ValueError(f"File is empty: {path}")

    # Read the first 16 bytes after all checks pass.
    with path.open("rb") as document:
        return document.read(16)
def detect_file_type(file_path: str) -> str:
    signature = read_file_signature(file_path)

    # Check for a PDF header.
    if signature.startswith(b"%PDF-"):
        return "PDF"

    # Check for a JPEG header.
    if signature.startswith(b"\xff\xd8\xff"):
        return "JPEG"
        # Standard TIFF supports two byte orders.
    if signature.startswith((b"II\x2a\x00", b"MM\x00\x2a")):
        return "TIFF"

    # No supported signature matched.
    return "Unknown"
def check_file_extension(file_path: str) -> dict:
    # Identify the format from the starting bytes.
    detected_type = detect_file_type(file_path)

    # Get the filename extension in lowercase.
    extension = Path(file_path).suffix.lower()

    allowed_extensions = {
        "PDF": [".pdf"],
        "JPEG": [".jpg", ".jpeg"],
        "TIFF": [".tif", ".tiff"],
    }

    # Return all findings, including the inspected file's path.
    return {
        "file_path": file_path,
        "detected_type": detected_type,
        "extension": extension,
        "matches": extension in allowed_extensions.get(detected_type, []),
        "size_bytes": Path(file_path).stat().st_size,
    }
    # Stop if the supplied path does not exist.
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    # Stop if the path points to a folder rather than a file.
    if not path.is_file():
        raise ValueError(f"Expected a file, but received: {path}")
    
def inspect_image(file_path: str) -> dict:
    # Open the image and read its properties.
     with Image.open(file_path) as image:
        details = {
            "format": image.format,
            "width": image.width,
            "height": image.height,
            "color_mode": image.mode,
        }

        # Decode the current frame to check that its pixels can be read.
        image.load()

     return details

def inspect_pdf(file_path: str) -> dict:
    # Open the PDF and keep its file handle managed.
    with open(file_path, "rb") as document:
        reader = PdfReader(document)

        # Report encryption without attempting to unlock the document.
        if reader.is_encrypted:
            return {
                "encrypted": True,
                "page_count": None,
            }

        return {
            "encrypted": False,
            "page_count": len(reader.pages),
        }    