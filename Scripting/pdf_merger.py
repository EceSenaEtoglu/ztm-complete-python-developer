import sys
import PyPDF2
def merge_pdfs(pdf_file_names):
    """merges pdf files provided in parameters"""
    merger = PyPDF2.PdfMerger()

    for file_name in pdf_file_names:
        # parameter specifies path to file
        merger.append(file_name)
    # create new pdf
    merger.write("merged.pdf")

merge_pdfs(sys.argv[1:])