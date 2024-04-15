from PyPDF2 import PdfFileWriter, PdfFileReader
out=PdfFileWriter()
file=PdfFileReader("encrypt_decrypt_pdf/encrypted_pdf.pdf")
password="123sam"
if file.isEncrypted:
    file.decrypt(password)
    for idx in range(file.numPages):
        page=file.getPage(idx)
        out.addPage(page)
    with open("encrypt_decrypt_pdf/decrypted_pdf.pdf","wb") as f:
        out.write(f)   
    print("File decrypted successfully!")
else:
    print("File already decrypted!")