import os
import sys
import win32com.client

# Open cmd or powershell in the webdev folder and run the following command
#
# python converter.py "C:\Users\Owner\OneDrive\Documents\webdev\posts\SAMPLE.rtf"
#
# luv u bye



def convert_rtf_to_html(rtf_path):
    """Converts an RTF file to HTML using Microsoft Word."""
    if not os.path.exists(rtf_path):
        print(f"Error: File '{rtf_path}' not found.")
        sys.exit(1)

    # Set output file paths
    output_path = os.path.splitext(rtf_path)[0] + ".htm"  # Temp output
    final_output_path = os.path.splitext(rtf_path)[0] + ".html"  # Renamed output

    # Initialize Word
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False

    try:
        # Open and convert the document
        doc = word.Documents.Open(os.path.abspath(rtf_path))
        doc.SaveAs(os.path.abspath(output_path), FileFormat=10)  # 10 = HTML format
        doc.Close()
    except Exception as e:
        print(f"Error converting file: {e}")
    finally:
        word.Quit()

    # Rename .htm to .html
    if os.path.exists(output_path):
        os.rename(output_path, final_output_path)
        print(f"Conversion successful! HTML saved at: {final_output_path}")
    else:
        print("Conversion failed. No output file found.")

# Run script from CLI
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_rtf.py <path-to-rtf-file>")
        sys.exit(1)

    rtf_file = sys.argv[1]
    convert_rtf_to_html(rtf_file)
