import sys
import PyPDF2

def merge_pdfs(pdf_file_names, output_file_name="merged.pdf"):
    """merges pdf files provided in parameters"""
    try:
        # Init a PDF merger
        merger = PyPDF2.PdfMerger()

        for file_name in pdf_file_names:
            try:
                # Open each PDF file
                with open(file_name, 'rb') as pdf_file:
                    # Append the PDF pages to the merger
                    merger.append(pdf_file)
            except FileNotFoundError:
                print(f"File not found: {file_name}")
            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")

        # Check if there are pages to merge
        if merger.pages > 0:
            # Write the merged PDF to the output file
            with open(output_file_name, 'wb') as output_pdf:
                merger.write(output_pdf)
            print(f"PDF files merged into {output_file_name}")
        else:
            print("No valid PDF pages to merge.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Check if there are command-line arguments
    if len(sys.argv) < 2:
        print("No files to merge found")
    else:
        # Call the merge_pdfs function with the provided PDF file names
        merge_pdfs(sys.argv[1:])
