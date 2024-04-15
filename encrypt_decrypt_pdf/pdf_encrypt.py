from PyPDF2 import PdfFileWriter, PdfFileReader

out=PdfFileWriter()
file=PdfFileReader("encrypt_decrypt_pdf/test_pdf.pdf")
num=file.numPages
for idx in range(num):
    page=file.getPage(idx)
    # page.encrypt("123sam")
    out.addPage(page)

password="123sam"
out.encrypt(password)
with open("encrypt_decrypt_pdf/encrypted_pdf.pdf","wb") as f:
    out.write(f)