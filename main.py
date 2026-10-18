from file_inspector import check_file_extension, inspect_image, inspect_pdf
import json

# Run this block when we launch main.py directly.
if __name__ == "__main__":
    file_path = input("Enter the file path: ")

    try:
        result = check_file_extension(file_path)

        # Choose the inspector using the detected format.
        if result["detected_type"] in ("JPEG", "TIFF"):
            result["image_details"] = inspect_image(file_path)
        elif result["detected_type"] == "PDF":
            result["pdf_details"] = inspect_pdf(file_path)

        print(f"Detected format: {result['detected_type']}")
        print(f"File extension: {result['extension']}")

        # Save the inspection results as a JSON report.
        with open("inspection_report.json", "w", encoding="utf-8") as report:
            json.dump(result, report, indent=4)

        print("Report saved to inspection_report.json")
        print(f"File size: {result['size_bytes']} bytes")
        if result["matches"]:
            print("PASS: File extension matches the detected format.")
        else:
            print("REVIEW: Extension mismatch or unrecognized format.")
    except (OSError, ValueError) as error:
        # Show a readable message instead of a traceback.
        print(f"Could not inspect file: {error}")