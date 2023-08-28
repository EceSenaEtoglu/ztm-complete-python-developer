import PyPDF2

def water_marker(input_file_name, watermark_file_name):
    # Create readers
    with open(input_file_name, "rb") as file:
        template = PyPDF2.PdfReader(file)

        with open(watermark_file_name, "rb") as file1:
            watermark = PyPDF2.PdfReader(file1)

            # Create writer
            output = PyPDF2.PdfWriter()

            for i in range(len(template.pages)):
                curr_page = template.pages[i]
                # Add the watermark to curr_page
                curr_page.merge_page(watermark.pages[0])  # Use merge_page instead of mergePage

                output.add_page(curr_page)

            # Create watermarked pdf
            with open("watermarked.pdf", "wb") as file2:
                output.write(file2)

original_file_name = input("Enter your original pdf file name: ")
watermark_file_name = input("Enter your watermark pdf file name: ")
print("Watermarking pages and creating a copy...")
water_marker(original_file_name, watermark_file_name)