from PyPDF2 import PdfWriter, PdfReader

num = int(input("Enter page number you want combine from multiple documents ")) - 1
pdf_writer = PdfWriter()

for pdf_file in ['birds.pdf', 'birdspic.pdf']:
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        pdf_writer.add_page(reader.pages[num])

with open('output.pdf', 'wb') as output:
    pdf_writer.write(output)